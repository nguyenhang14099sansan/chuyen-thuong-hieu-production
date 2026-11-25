# Chuyện Thương Hiệu

Skill tổng hợp quy trình nghiên cứu chiến dịch, viết hook và kịch bản kể chuyện, chuẩn bị giọng Vbee, dựng video dọc và viết caption Facebook. Cập nhật theo lựa chọn của chủ kênh đến ngày 25/11/2026.

Tải **[chuyen-thuong-hieu-production.zip](chuyen-thuong-hieu-production.zip)** và giải nén thư mục `chuyen-thuong-hieu-production` vào thư mục skills của công cụ bạn dùng. Với Codex, vị trí thông thường là `~/.codex/skills/`. Mở phiên mới để công cụ nhận skill.

Gói chứa `SKILL.md`, tài liệu từng bước, khung cam có logo, logo PNG, lớp căn TikTok/Reels, tọa độ JSON, nhạc Blockbuster Trailer và hai công cụ Python chuẩn hóa thẻ Vbee, ghép nhạc cao trào.

Mặc định dùng giọng HN – Ngọc Huyền 1.1x, title trắng căn trái, khung cam ở hook, hình ngang phủ đủ hai mép ở thân, logo góc phải, cắt cảnh theo câu thoại. Nhạc lấy đoạn cao trào từ 48,08 giây với gain −20 dB và chạy hết clip.

Ví dụ gọi skill trong Codex

```text
Dùng $chuyen-thuong-hieu-production tạo video từ kịch bản, video nguồn và MP3 tôi gửi.
```

Đọc hướng dẫn chính tại **[SKILL.md](SKILL.md)**. Thư mục `chuyen-thuong-hieu-production/` chứa trọn bộ tài liệu và tài nguyên để xem trực tiếp trên GitHub.

Hai công cụ Python đi kèm dùng Python tiêu chuẩn. Ghép nhạc cần FFmpeg và FFprobe trong PATH. Bóc lời, căn từ và dựng video dùng công cụ tương ứng trong môi trường của bạn theo quy trình trong gói. Dựng phụ đề ASS cần FFmpeg có libass và font đủ dấu tiếng Việt.
