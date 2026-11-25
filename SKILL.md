---
name: chuyen-thuong-hieu-production
description: Viết hook, kịch bản kể chuyện, bản Vbee và caption Facebook, hoặc dựng video phân tích chiến dịch và tin thương hiệu theo phong cách Chuyện Thương Hiệu. Dùng khung cam đỏ ở hook, vùng an toàn TikTok/Reels, phụ đề khớp lời và nhạc cao trào Blockbuster Trailer ở −20 dB.
---

# Chuyện Thương Hiệu — kịch bản và video

Gói độc lập tổng hợp các lựa chọn người dùng đã chốt đến ngày 25/11/2026. Tệp khán giả mặc định 25–54 tuổi. Viết gần gũi, sắc sảo, câu ngắn, giải thích bằng hành động và tình huống dễ hình dung. Yêu cầu mới trong cuộc trò chuyện được ưu tiên.

## Chọn phần việc

- Nghiên cứu chiến dịch, viết hook hoặc thân bài, đọc [nghiên cứu và kể chuyện](chuyen-thuong-hieu-production/references/research-and-scripts.md) cùng [gu hook](chuyen-thuong-hieu-production/references/hooks.md).
- Chuẩn bị lời TTS hoặc tạo MP3, đọc [Vbee và căn lời](chuyen-thuong-hieu-production/references/vbee-and-alignment.md).
- Dựng hoặc sửa video, đọc [quy trình sản xuất](chuyen-thuong-hieu-production/references/video-production.md), [thông số nhận diện](chuyen-thuong-hieu-production/assets/style.json) và [tọa độ an toàn](chuyen-thuong-hieu-production/assets/safe-area.json).
- Viết caption đăng Facebook, đọc [gu caption](chuyen-thuong-hieu-production/references/facebook-captions.md).

Thực hiện phần người dùng đang yêu cầu. Khi người dùng đã giao tạo video từ tư liệu và MP3, tiếp tục đến bản MP4 đã được kiểm tra. Dùng đúng lời đã duyệt và đúng file giọng đọc. Khi chỉ viết caption, lấy đúng video hiện hành của cuộc trò chuyện.

## Những lựa chọn quan trọng

1. Hook đưa tên thương hiệu và hành động khác thường lên sớm. Tìm điểm sáng tạo cụ thể trước khi viết. Phân biệt vấn đề, động lực khách hàng, Big Idea và cách thực hiện. Bài kể thành một mạch, câu sau tiến thêm ý từ câu trước.
2. Mở và kiểm tra nguồn của dữ kiện, công dụng, năm ra mắt và kết quả. Ghi nguồn ngoài lời đọc. Phân biệt năm triển khai với năm nhận giải. Khi tìm thêm chiến dịch, đối chiếu danh sách đã làm và danh sách loại của người dùng.
3. Vbee dùng giọng **HN – Ngọc Huyền, tốc độ 1.1x, MP3**. Ngắt dấu chấm 0,2 giây, phẩy 0,1 giây, chấm phẩy 0,15 giây, xuống dòng 0,25 giây. Thẻ trong bản biên tập là `<break time=0.10s/>`. Riêng bản gửi Vbee chuyển `0.10s` thành `0.1s` theo kinh nghiệm đã kiểm tra. Sau mỗi lần tạo, bấm **Tải xuống** và xác nhận file.
4. Dùng nguyên [khung trống có logo](chuyen-thuong-hieu-production/assets/khung-trong-co-logo-1080x1920.png). Khung cam chỉ ở hook. Cảnh hook chọn cao trào hoặc chi tiết sáng tạo nổi bật của tư liệu. Phóng đồng đều để phủ kín phần hình phía trên, hòa xuống cam qua alpha của PNG.
5. Title trắng, in hoa, căn trái, khoảng cách từ tự nhiên. Xếp dòng gần cân bề rộng, tận dụng hộp title trong vùng an toàn. Chọn cỡ chữ theo nội dung. Giữ cụm tên riêng và nghĩa câu khi xuống dòng.
6. Phần thân dùng hình ngang rõ nét phủ đủ hai mép khung dọc, giữ tỷ lệ nguồn, nền mờ phía trên và dưới. Logo trắng/bạc nhỏ ở góc trên phải từ sau hook đến hết video. Các nội dung chính nằm trong vùng an toàn.
7. Giữ mỗi cảnh quay liên tục ít nhất đến hết một câu thoại. Đặt cắt trong khoảng nghỉ sau câu. Rà cả điểm cắt có sẵn bên trong video nguồn và những thẻ chữ lọt ở đầu hoặc cuối trích đoạn.
8. Nhạc mặc định là [Blockbuster Trailer](chuyen-thuong-hieu-production/assets/nhac-nen-blockbuster-trailer.m4a), bắt đầu tại **48,08 giây** ở đoạn cao trào. Nhạc vào ngay đầu hook và chạy hết video. Gain riêng track nhạc **−20 dB** so với file gốc. Nối lặp theo nhịp khi cần và kiểm tra tổng âm thanh sau xuất.
9. Căn phụ đề theo giọng thực tế, sửa đúng tên thương hiệu và số hiển thị. Mục tiêu karaoke lệch tối đa hai frame ở 30 fps cần được đo trên bản xuất. Kiểm tra một loạt mốc đại diện rồi nêu đúng phạm vi đã kiểm tra.

## Quy trình đầy đủ

### Nhận nội dung và xác nhận đúng đầu vào

Lấy tên thương hiệu, chiến dịch, ý tưởng, hook đã chọn, nội dung hiện hành, MP3 và video nguồn từ yêu cầu hoặc nguồn được chỉ định. Khi tên MP3 và nội dung có dấu hiệu khác nhau, nghe đầu file và đối chiếu toàn bài trước khi dựng. Chú ý các bộ kịch bản có thể trùng số thứ tự.

Nếu người dùng giao làm theo lịch trong bảng, chọn đúng các dòng page Chuyện Thương Hiệu đã được giao rồi dò sang CONTENT BANK để lấy nội dung và voice. Với kế hoạch đăng bài, áp dụng lịch người dùng chỉ định và bỏ Chủ Nhật. Giữ phạm vi số bài và tab được giao.

### Nghiên cứu và viết

Đọc nguồn thương hiệu, agency, phim gốc và hồ sơ giải khi có. Xem hành động thực sự trong clip. Lưu mô tả cơ chế, đối tượng, mốc triển khai, nguồn tư liệu và kết quả có căn cứ. Tách điều quan sát được với nhận định của người viết.

Chọn hook theo hành động sáng tạo, bất tiện đời thường, mong muốn, nghịch lý kinh doanh hoặc đối đầu thương hiệu phù hợp case. Câu đầu thân bài bổ sung diễn biến hoặc hệ quả rõ nhất. Đi từ tình huống sang lựa chọn sáng tạo, cơ chế trải nghiệm và vai trò sản phẩm. Với tin doanh nghiệp, đi theo sự việc và tác động liên quan công việc, chi tiêu hoặc gia đình.

Giữ hook đã được chọn khi sửa phần thân. Độ dài theo yêu cầu và lời đọc thực tế. Khi giao bài phân tích 250–350 từ, làm đủ cấu trúc người dùng yêu cầu. Khi giao video ngắn, tối ưu cho lời nói và thời lượng đã giao. CTA bám câu chuyện và có thể trả lời tự nhiên.

### Chuẩn bị giọng và phụ đề

Giữ ba lớp đối chiếu được theo mã bài, gồm chữ hiển thị, lời TTS có phiên âm và bản MP3. Dùng `scripts/normalize_vbee.py` để tạo bản gửi Vbee từ bản biên tập. Thiết lập lại giọng, tốc độ và ngắt nghỉ trên giao diện trước khi tạo.

Nghe bản thử khi tạo hàng loạt, tải từng file thành công vào thư mục Chuyện Thương Hiệu vebee theo tên `NN - Thương hiệu - Chiến dịch.mp3`. Dùng công cụ kết nối hiện có hoặc giao diện Vbee. Tên và khả năng của API trình duyệt cần lấy từ tài liệu công cụ trong phiên làm việc.

Có lời chuẩn thì dùng để căn chỉnh. Khi chỉ có MP3, bóc lời rồi rà đoạn nói bị sót, tên riêng và từ nhận nhầm. Căn từng từ với âm thanh, chia phụ đề theo cụm nghĩa, giữ tên riêng và số–đơn vị cùng cụm. Dựng karaoke từ mốc từng từ đã rà.

### Chọn tư liệu và dựng

Kiểm tra thời lượng, tỷ lệ, dải đệm đóng sẵn và chất lượng nguồn. Lập shot theo các câu đọc và ghi URL, thời điểm tải, khoảng cắt nguồn, vị trí xuất trên timeline. Khi một cảnh nguồn quá ngắn, tìm cảnh quay liên tục phù hợp hoặc giảm tốc nhẹ có chủ đích. Kiểm tra hành động còn tự nhiên.

Canvas mặc định 1080×1920, 30 fps. Mốc hết hook theo lời đọc. Dùng bố cục trong `references/video-production.md`. Xem hook có title dài nhất, frame ngay sau hook, các cảnh thân và cụm phụ đề dài. Bật lớp căn an toàn khi xem trước rồi ẩn khi xuất.

Xuất bản hình và giọng trước. Có thể dùng `scripts/mix_music.py` để thêm nhạc mặc định vào bản này. Công cụ giữ video bằng stream copy, trộn nhạc riêng ở −20 dB, nối đoạn cao trào khi cần và kiểm tra peak sau mã hóa. Nếu tổng âm thanh vượt 0 dBFS, chỉnh cách phối và kiểm tra lại, giữ lựa chọn âm lượng nhạc của người dùng.

### Kiểm tra và bàn giao

Xem bản MP4 sau xuất tại đầu và cuối hook, các điểm cắt, dòng dài, chủ thể sát mép và những đoạn đã bị báo lỗi. Rà dấu tiếng Việt, vùng an toàn, logo, hai mép hình ngang, tiếng nhạc suốt clip, lời nói và thời lượng.

So phụ đề với giọng thực tế ở các mốc đầu, giữa, cuối và tên/số khó. Mốc từ mô hình là dữ liệu để kiểm tra tiếp. Ghi đúng kết quả đo và phần còn cần rà khi có.

Giao link MP4 dùng được cùng thời lượng. Khi cần tiếp tục chỉnh, giữ kịch bản, bản TTS, lời đã căn, shot plan, nguồn và mã dựng trong dự án. Caption Facebook đi kèm khi người dùng yêu cầu. Lưu sản phẩm vào thư mục được chỉ định hoặc `outputs/` của workspace.

## Tài nguyên và công cụ

Gói có khung cam PNG, logo PNG, lớp căn vùng an toàn, tọa độ JSON, cấu hình nhận diện và nhạc. Tất cả đường dẫn tài nguyên tính từ thư mục skill.

`scripts/normalize_vbee.py` dùng Python tiêu chuẩn. `scripts/mix_music.py` cần FFmpeg và FFprobe trong PATH. Bóc lời và căn từng từ dùng công cụ hiện có của môi trường, với cấu trúc dữ liệu và cách nghiệm thu trong [Vbee và căn lời](chuyen-thuong-hieu-production/references/vbee-and-alignment.md). Dựng phụ đề ASS cần FFmpeg có libass. Dùng font đậm đủ dấu tiếng Việt có sẵn trên máy. Helvetica Neue Bold hoặc Condensed Bold là tham chiếu của bản macOS.
