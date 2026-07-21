---
title: "Xử lý dữ liệu bất đồng bộ sau trận đấu với DynamoDB Streams"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

### Tổng quan
Trong phần này, bạn sẽ bật **DynamoDB Streams** trên bảng `ActiveMatches`, khởi tạo hàm **MatchAnalyticLambda** và thu thập sự kiện kết thúc trận đấu bất đồng bộ để ghi log phân tích mà không gây ảnh hưởng tới độ trễ của hệ thống matchmaking.

---

### Các bước thực hiện

#### Bước 1: Bật DynamoDB Streams
1. Vào **DynamoDB** console -> Chọn bảng `ActiveMatches`.
2. Tại mục **Exports and streams**, bật **DynamoDB stream** (View type: `NEW_AND_OLD_IMAGES`).

![Bật DynamoDB Stream](/images/5-Workshop/img_B/image33.png)

---

#### Bước 2: Tạo IAM Role cho Analytics Lambda
1. Tạo IAM Role `MatchAnalyticRole`.
2. Gắn Policy cho phép đọc dữ liệu từ DynamoDB Streams (`dynamodb:GetRecords`, `dynamodb:GetShardIterator`, `dynamodb:DescribeStream`, `dynamodb:ListStreams`).

![Tạo Role MatchAnalytic](/images/5-Workshop/img_B/image36.png)
![Policy đọc Stream](/images/5-Workshop/img_B/image37.png)

---

#### Bước 3: Tạo `MatchAnalyticLambda` Function
1. Vào **AWS Lambda** console -> Chọn **Create function**.
2. Đặt tên Function: `MatchAnalyticLambda`.
3. Gắn `MatchAnalyticRole` vừa tạo.

![Tạo MatchAnalytic Lambda](/images/5-Workshop/img_B/image39.png)

---

#### Bước 4: Cấu hình Event Source Mapping & Kiểm tra Log Phân tích
1. Thêm Trigger DynamoDB Stream cho `MatchAnalyticLambda`.
2. Kiểm thử kết thúc trận đấu: khi bản ghi trận đấu chuyển sang trạng thái hoàn thành (finished), `MatchAnalyticLambda` tự động bắt sự kiện, tính toán chỉ số và ghi log analytics ngầm.

![Dữ liệu Event từ DynamoDB Stream](/images/5-Workshop/img_B/image40.png)
