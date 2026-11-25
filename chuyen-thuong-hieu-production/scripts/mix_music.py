"""Mix the approved climax music at -20 dB into a video with narration.

Requires ffmpeg and ffprobe in PATH. Outputs a new MP4, with picture stream copy,
AAC stereo audio and a decoded true-peak check. Input pictures are not rendered.
"""

import argparse
import json
import math
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


DEFAULT_MUSIC = Path(__file__).resolve().parents[1] / "assets/nhac-nen-blockbuster-trailer.m4a"


def run(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr[-5000:])
    return result


def probe(path):
    return json.loads(run([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)
    ]).stdout)


def music_filter(duration, start, loop_end, fade, gain):
    segment = loop_end - start
    if duration <= segment:
        return (
            f"[1:a:0]atrim=start={start}:duration={duration},asetpts=PTS-STARTPTS,"
            f"aresample=48000,aformat=channel_layouts=stereo,volume={gain}dB[music]"
        )
    count = math.ceil((duration - fade) / (segment - fade))
    labels = "".join(f"[part{i}]" for i in range(count))
    filters = [
        f"[1:a:0]atrim=start={start}:end={loop_end},asetpts=PTS-STARTPTS,"
        f"aresample=48000,aformat=channel_layouts=stereo,asplit={count}{labels}"
    ]
    previous = "part0"
    for index in range(1, count):
        current = f"joined{index}"
        filters.append(
            f"[{previous}][part{index}]acrossfade=d={fade}:c1=tri:c2=tri[{current}]"
        )
        previous = current
    filters.append(f"[{previous}]atrim=duration={duration},volume={gain}dB[music]")
    return ";".join(filters)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--music", type=Path, default=DEFAULT_MUSIC)
    parser.add_argument("--start", type=float, default=48.08)
    parser.add_argument("--loop-end", type=float, default=74.78)
    parser.add_argument("--crossfade", type=float, default=0.08)
    parser.add_argument("--gain-db", type=float, default=-20)
    args = parser.parse_args()
    for binary in ("ffmpeg", "ffprobe"):
        if not shutil.which(binary):
            parser.error(f"{binary} is required in PATH.")
    for path in (args.input, args.music):
        if not path.is_file():
            parser.error(f"File is missing: {path}")
    if args.output.exists() or args.output.resolve() == args.input.resolve():
        parser.error("Choose a new output path.")
    values = (args.start, args.loop_end, args.crossfade, args.gain_db)
    if not all(math.isfinite(value) for value in values):
        parser.error("Music values must be finite numbers.")
    music_info = probe(args.music)
    music_duration = float(music_info["format"]["duration"])
    if not 0 <= args.start < args.loop_end <= music_duration:
        parser.error("The loop region must be inside the music file.")
    if not 0 < args.crossfade < (args.loop_end - args.start) / 2:
        parser.error("Crossfade must be positive and shorter than half the loop.")
    source = probe(args.input)
    video = next((stream for stream in source["streams"] if stream["codec_type"] == "video"), None)
    audio = next((stream for stream in source["streams"] if stream["codec_type"] == "audio"), None)
    if video is None or audio is None:
        parser.error("The input must contain picture and narration audio.")
    duration = float(video.get("duration", source["format"]["duration"]))
    if not math.isfinite(duration) or duration <= 0:
        parser.error("The picture duration is invalid.")
    output_parent = args.output.resolve().parent
    output_parent.mkdir(parents=True, exist_ok=True)
    voice_layout = "aformat=channel_layouts=stereo"
    if audio.get("channels") == 1:
        voice_layout = "pan=stereo|FL=c0|FR=c0"
    filters = (
        f"[0:a:0]aresample=48000,{voice_layout},"
        f"apad=whole_dur={duration},atrim=duration={duration}[voice];"
        + music_filter(duration, args.start, args.loop_end, args.crossfade, args.gain_db)
        + f";[voice][music]amix=inputs=2:duration=first:normalize=0,atrim=duration={duration}[mix]"
    )
    with tempfile.TemporaryDirectory(prefix="music-mix-", dir=output_parent) as temporary:
        staged = Path(temporary) / "video.mp4"
        run([
            "ffmpeg", "-nostdin", "-v", "error", "-i", str(args.input), "-i", str(args.music),
            "-filter_complex", filters, "-map", "0:v:0", "-map", "[mix]", "-map_metadata", "0",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", str(staged)
        ])
        report = run([
            "ffmpeg", "-nostdin", "-hide_banner", "-nostats", "-i", str(staged),
            "-map", "0:a:0", "-af", "ebur128=peak=true", "-f", "null", "-"
        ]).stderr
        match = re.search(r"True peak:\s*Peak:\s*([-\d.]+)\s*dBFS", report)
        if match is None:
            raise RuntimeError("True peak could not be read from the exported audio.")
        peak = float(match.group(1))
        if peak >= 0:
            raise RuntimeError(f"Mixed true peak is {peak:.1f} dBFS. Review the narration level and mix.")
        rendered = probe(staged)
        rendered_audio = next(stream for stream in rendered["streams"] if stream["codec_type"] == "audio")
        if abs(float(rendered_audio["duration"]) - duration) > 0.03:
            raise RuntimeError("Mixed audio does not cover the picture duration.")
        # Exclusive destination creation protects a file appearing during rendering.
        with args.output.open("xb") as destination, staged.open("rb") as completed:
            shutil.copyfileobj(completed, destination)
    print(f"{args.output}\nDuration {duration:.3f}s, music gain {args.gain_db:g} dB, true peak {peak:.1f} dBFS")


if __name__ == "__main__":
    main()
