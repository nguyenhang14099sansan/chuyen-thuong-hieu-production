"""Create a Vbee submission copy while preserving wording outside break tags."""

import argparse
import re
from pathlib import Path


BREAK = re.compile(
    r'<break\s+time\s*=\s*["\']?(\d+(?:\.\d+)?)s["\']?\s*/>',
    flags=re.IGNORECASE,
)


def normalize(text):
    def replace(match):
        seconds = match.group(1)
        if seconds == "0.10":
            seconds = "0.1"
        return f"<break time={seconds}s/>"

    return BREAK.sub(replace, text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error("Choose a different output path for the submission copy.")
    text = args.input.read_text(encoding="utf-8")
    result = normalize(text)
    if re.search(r"<break\b", BREAK.sub("", result), flags=re.IGNORECASE):
        parser.error("A break tag has an unsupported format. Check its time and closing />.")
    with args.output.open("x", encoding="utf-8", newline="") as destination:
        destination.write(result)
    print(args.output)


if __name__ == "__main__":
    main()
