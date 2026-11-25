# Dựng và kiểm tra video

## Môi trường và dự án

FFmpeg và FFprobe cần có trong PATH. FFmpeg có libass để xuất phụ đề ASS. Có thể dùng renderer khác trong môi trường nếu giữ đúng bố cục và thời gian. Pillow hoặc công cụ đo chữ tương đương giúp xếp title. Bóc lời và căn từ dùng mô hình đã có trên máy hoặc công cụ được cung cấp trong phiên.

Giữ lời chuẩn, MP3, dữ liệu căn từng từ, phụ đề, kế hoạch shot, tư liệu và lệnh dựng trong dự án. Mỗi shot ghi nguồn, khoảng cắt, thời gian trên timeline và crop. Độ dài video theo giọng thực tế. Dùng khổ 1080×1920 và 30 fps làm mặc định.

## Vùng an toàn

Các tọa độ ở đây cùng hệ 1080×1920, cạnh phải và dưới của hộp được hiểu là biên ngoài.

| Vùng | Tọa độ |
| --- | --- |
| Hộp an toàn phía trên | x từ 51 đến 1028, y từ 248 đến 861 |
| Hộp an toàn phía dưới | x từ 51 đến 888, y từ 861 đến 1548 |
| Title hook | x từ 72 đến 868, y từ 1176 đến 1528 |
| Logo thân | x 818, y 270, rộng 190, cao 138 |
| Phụ đề thân | x từ 72 đến 868, y từ 1398 đến 1508, tâm x 470 |

Đặt lớp căn PNG trong `assets/` đúng khổ ở track trên cùng khi xem trước. Đưa chữ, dấu, viền, logo và chi tiết quan trọng của chủ thể vào vùng trong suốt. Scale cả đa giác khi đổi kích thước canvas. Khung cam và nền tiếp tục phủ toàn canvas. Ẩn lớp căn trước khi xuất.

## Hook

Dùng nguyên `assets/khung-trong-co-logo-1080x1920.png`. Mảng cam bắt đầu tại y 960, đặc hoàn toàn tại y 1015. Màu từ #F4511D sang #7B180F, logo sẵn có trong khung ở x 72, y 1030, rộng 168, cao 122.

Chọn cao trào hoặc hành động thể hiện ý tưởng trong tư liệu gốc. Giữ cảnh quay liên tục đến hết câu hook. Phóng theo kiểu cover để phủ hình rõ nét lên hình chữ nhật x 0, y 0, rộng 1080, cao 1015. Crop có chủ đích để giữ mặt, sản phẩm và hành động. Ghép PNG theo alpha để mép hình hòa mềm xuống cam.

Title trắng, in hoa, căn trái. Dùng cùng cỡ chữ cho các dòng và giữ khoảng cách từ của font. Chọn xuống dòng để độ dài gần cân, giữ cụm nghĩa và tên riêng. Đo bounding box có cả dấu tiếng Việt trong hộp title. Với nội dung dài, có thể chọn mặt chữ Condensed Bold. Số dòng và cỡ chữ phụ thuộc tiêu đề thực tế.

Helvetica Neue Bold là font tham chiếu, macOS có thể cung cấp trong HelveticaNeue.ttc với index 1. Condensed Bold thường ở index 4. Kiểm tra mặt chữ thực tế trước khi dùng. Trên nền tảng khác, chọn font đậm đủ dấu tiếng Việt với độ rộng phù hợp rồi đo lại.

Chỉ dùng logo sẵn trong khung ở phần hook. Kết thúc khung theo mốc hết lời hook đã được chốt. Người dùng có thể yêu cầu hook đúng ba giây cho một bản riêng, khi đó cần xử lý thời gian đọc và title theo yêu cầu đó.

## Phần thân

Hết hook, chuyển sang hình ngang rõ nét ở giữa khung dọc, giữ tỷ lệ gốc và phủ đủ chiều rộng 1080 px. Nguồn 16:9 tham chiếu rộng 1080, cao 608, đặt tại y 656. Với tỷ lệ khác, tính chiều cao từ tỷ lệ thật. Nền mờ từ tư liệu phủ phần trên và dưới.

Trước khi scale, kiểm tra dải đen và đệm hai bên có sẵn trong nguồn. Crop bỏ phần đệm được xác định bằng khung hình và chuyển động, giữ khoảng trắng có chủ đích trong thiết kế. Phần hình rõ nét cần chạm đúng cả hai mép canvas.

Logo từ `assets/logo-chuyen-thuong-hieu.png` cắt vùng chữ theo hộp x 0, y 230, phải 1254, dưới 1140 rồi scale về 190×138. Giữ nguyên màu trắng/bạc. Đặt góc trên phải theo hộp an toàn từ sau hook đến hết clip.

Phụ đề căn giữa trong hộp x 72–868, tâm x 470. Chọn cỡ đủ lớn nhưng giữ cả viền và bóng trong hộp. Khi có karaoke, tạo nhịp từ dữ liệu đã căn, giữ màu chữ có tương phản và đọc rõ trên tư liệu. Phần thân chỉ chèn các nội dung người dùng đã yêu cầu. Ghi thông tin nguồn hoặc nhãn cảnh minh họa ở ghi chú/caption khi phù hợp.

## Cắt cảnh

Lấy nhịp câu từ MP3 đã duyệt. Giữ một cảnh liên tục tối thiểu hết một câu rồi cắt trong khoảng nghỉ. Có thể giữ qua nhiều câu. Rà cả các điểm đổi góc máy bên trong video nguồn.

Kiểm tra vài frame ở cả đầu và cuối mỗi đoạn. Thẻ chữ của shot kế trong nguồn dễ lọt vào đuôi và gây lóe. Chọn lại điểm vào/ra, giữ hình hoặc giảm tốc nhẹ có chủ đích để đủ câu. Xem chuyển động sau chỉnh.

## Nhạc và phối âm

Nhạc mặc định là `assets/nhac-nen-blockbuster-trailer.m4a`. Lấy cao trào từ 48,08 giây, vào ngay đầu hook và chạy hết video. Đặt gain track nhạc −20 dB so với tệp gốc. Đây là giảm gain của nhạc, không phải mục tiêu loudness của toàn bản phối.

Tạo bản hình có giọng đã cân mức trước khi dùng công cụ phối nhạc.

```bash
python scripts/mix_music.py video-co-giong.mp4 video-hoan-chinh.mp4
```

Công cụ đọc thời lượng video, lấy đoạn nhạc phù hợp và nối lặp cao trào khi cần. Mốc vòng lặp tham chiếu là 48,08–74,78 giây, hòa mép 0,08 giây. Nghe lại chỗ nối và điều chỉnh theo nhịp nếu nội dung cần vòng lặp dài.

```bash
python scripts/mix_music.py video-co-giong.mp4 video-hoan-chinh.mp4 --start 48.08 --loop-end 74.78 --gain-db -20
```

Khi sửa bản đã có nhạc, lấy bản hình và giọng trước phối để tránh chồng hai lớp nhạc. Công cụ mặc định lấy audio đầu tiên làm giọng, dùng stream copy cho hình và AAC stereo cho bản phối. Nó kiểm tra peak sau mã hóa, báo lỗi nếu vượt 0 dBFS để xử lý phối âm tiếp.

## Kiểm tra bản xuất

- FFprobe xác nhận khổ hình, số frame, thời lượng và audio đúng.
- Xem frame đầu, cuối hook, ngay sau hook, các cảnh ngang và cụm phụ đề dài.
- Bật lớp căn trên bản xem trước để rà dấu tiếng Việt, title, logo và nội dung quan trọng trong footage.
- Phát đoạn quanh các điểm cắt để bắt shot lóe hoặc nhịp quá nhanh.
- Nghe và xem phụ đề tại các mốc đầu, giữa, cuối, tên riêng và số. Kiểm tra karaoke trên file xuất khi dùng.
- Nghe nhạc từ đầu đến cuối, chỗ nối vòng và tiếng thoại. Kiểm tra peak sau mã hóa.
- Khi sửa một phần, đối chiếu các yếu tố đã chốt còn lại trên bản xuất.

Giao MP4 với link mở được. Giữ các nguồn, file căn lời và lệnh dựng để tiếp tục sửa. Báo thông số đã đo và điểm chưa kiểm tra khi có.
