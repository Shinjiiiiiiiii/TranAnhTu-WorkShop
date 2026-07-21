---
title: "Khởi tạo MatchAnalytic Lambda & Kiểm thử Log"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.6.2. </b> "
---

### Các bước thực hiện

#### Bước 1: Tạo `MatchAnalyticLambda` Function
1. Vào **AWS Lambda** console -> Chọn **Create function**.
2. Đặt tên Function: `MatchAnalyticLambda`.
3. Gắn `MatchAnalyticRole` vừa tạo.

![Tạo MatchAnalytic Lambda](/images/5-Workshop/img_B/image39.png)

---

#### Bước 2: Cấu hình Event Source Mapping & Kiểm tra Log Phân tích
1. Thêm Trigger DynamoDB Stream cho `MatchAnalyticLambda`.
2. Kiểm thử kết thúc trận đấu: khi bản ghi trận đấu chuyển sang trạng thái hoàn thành (finished), `MatchAnalyticLambda` tự động bắt sự kiện, tính toán chỉ số và ghi log analytics ngầm.

![Dữ liệu Event từ DynamoDB Stream](/images/5-Workshop/img_B/image40.png)
