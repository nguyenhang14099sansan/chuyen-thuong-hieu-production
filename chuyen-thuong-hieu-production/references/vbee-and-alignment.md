# Vbee và căn lời

## Preset đã chốt

| Thiết lập | Giá trị |
| --- | --- |
| Giọng | HN – Ngọc Huyền |
| Tốc độ | 1.1x |
| Định dạng | MP3, giọng đọc riêng |
| Dấu chấm | 0,2 giây |
| Dấu phẩy | 0,1 giây |
| Dấu chấm phẩy | 0,15 giây |
| Xuống dòng | 0,25 giây |
| Nhạc | Thêm ở bước dựng video |

Kiểm tra lại giọng và tốc độ sau khi tải lại giao diện. Lấy lời hiện hành từ bản đã duyệt hoặc cột Vbee trong ngân hàng nội dung được giao. Khi tên file và chủ đề lệch nhau, nghe và đối chiếu trước khi tiếp tục.

## Bản hiển thị và bản đọc

Giữ tên thương hiệu đúng chính tả trong chữ hiển thị. Khi Vbee đọc sai tên nước ngoài, ghi phiên âm riêng trong bản TTS, kèm ánh xạ về tên gốc cho phụ đề. Viết số theo cách đọc khi cần, giữ dạng số ở phụ đề khi dễ đọc hơn.

Thẻ nghỉ trong bản biên tập dùng dạng `<break time=0.10s/>` và giá trị nhịp đã duyệt. Trước khi gửi Vbee, chuyển riêng `0.10s` thành `0.1s`. Cách này đã xử lý trường hợp giọng đọc phát âm phần thẻ trong tài khoản của người dùng. Công cụ chuẩn hóa chỉ xử lý thẻ, giữ phần văn bản còn lại.

```bash
python scripts/normalize_vbee.py script-vbee.txt script-vbee-submit.txt
```

## Tạo và tải MP3

Dùng kết nối phù hợp khi có hoặc giao diện Vbee đã đăng nhập. Đọc tài liệu công cụ trình duyệt trong phiên làm việc để biết API hỗ trợ. Với yêu cầu tạo hàng loạt, tạo và nghe bài thử trước, rà tên riêng, phần hook, giọng, tốc độ và nhịp nghỉ.

Sau mỗi bài hoàn thành, bấm **Tải xuống** trong Vbee, chờ tải xong rồi xác nhận file có thể mở và thời lượng hợp lý. Đặt tên `NN - Thương hiệu - Chiến dịch.mp3` trong thư mục Chuyện Thương Hiệu vebee được chỉ định. Theo dõi trạng thái từng bài để tiếp tục đúng chỗ khi có lỗi.

Khi người dùng gửi MP3, dùng file đó làm giọng chuẩn cho video. Giữ lời thực tế khi tạo phụ đề. Nếu giọng và bản kịch bản khác nhau, ghi nhận khác biệt và dùng đúng phần đã được người dùng chốt.

## Bóc lời và phát hiện bỏ sót

Đo thời lượng bằng FFprobe. Dùng ASR có tiếng Việt, như Whisper trong môi trường đang có, để tạo lời nháp. Nghe lại các khoảng có năng lượng giọng nhưng chưa có chữ. Bóc riêng những khoảng đó với lề nhỏ hai bên rồi ghép có đối chiếu để tránh lặp.

Sửa lỗi nghe theo âm thanh và nguồn chính tả của tên. Có bản TTS thì tận dụng ánh xạ phiên âm. Một câu mỗi dòng giúp xác định nhịp dựng.

## Căn từng từ

Dùng forced alignment tiếng Việt hoặc công cụ căn từ hiện có, với lời đã được đối chiếu. Wav2vec2 tiếng Việt là một lựa chọn đã dùng trong quy trình cũ. Whisper cung cấp mốc nháp cần kiểm tra tiếp ở đầu câu và tên nước ngoài.

Biểu diễn dữ liệu có thể dùng cấu trúc sau.

```json
{
  "duration": 12.4,
  "words": [
    {"w": "Vaseline", "s": 0.10, "e": 0.72, "score": -0.25},
    {"w": "đem", "s": 0.76, "e": 0.98, "score": -0.12}
  ]
}
```

Với số hoặc tên hiển thị khác cách đọc, có thể biểu diễn trong lời căn như `1990{một_nghìn_chín_trăm_chín_mươi}` hay `TikTok{tích_tốc}`. Nhãn ngoài ngoặc dùng để hiển thị, phần trong ngoặc dùng cho âm đọc.

Rà các từ có điểm căn yếu, mốc trùng bất thường, từ thiếu mốc hoặc khoảng cách quá lớn. Nghe và căn lại đoạn đó. Khi mô hình phải nội suy, giữ dấu hiệu đó trong dữ liệu để rà tiếp.

## Chia phụ đề và nghiệm thu

Chia theo cụm nghĩa vừa hộp an toàn, thường khoảng 4–6 tiếng. Giữ nguyên tên riêng, từ ghép và số–đơn vị. Tránh cụm quá ngắn nhấp nháy hoặc cụm vắt qua dấu chấm. Mốc từng từ điều khiển karaoke, mốc câu điều khiển cắt cảnh.

Rà trên bản MP4 đã mã hóa ở đầu, giữa, cuối và những tên/số khó. Khi người dùng cần karaoke, mục tiêu là lệch tối đa hai frame ở 30 fps sau kiểm tra thực tế. Ghi đúng phạm vi và sai lệch đã đo, rồi sửa các đoạn chưa đạt.
