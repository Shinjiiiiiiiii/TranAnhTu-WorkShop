---
title: "Xây dựng Matchmaker Lambda Function"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.3.1. </b> "
---

### Các bước thực hiện

#### Bước 1: Tạo AWS Lambda Function
1. Truy cập **AWS Lambda** console -> Chọn **Create function**.
2. Đặt tên Function: `FightingGameMatchmaker`.
3. Runtime: **Node.js 20.x**.

![Tạo Lambda Function](/images/5-Workshop/img_A/image31.png)

---

#### Bước 2: Cấu hình Phân quyền IAM Role & Biến môi trường
1. Tại tab **Configuration** -> **Permissions**, nhấp vào liên kết Role name để chỉnh sửa.
2. Thêm Policy cấp quyền `dynamodb:PutItem`, `dynamodb:GetItem`, `dynamodb:DeleteItem` và `ec2:DescribeInstances`.

![Cấu hình Permission Role](/images/5-Workshop/img_A/image35.png)

3. Tại **Environment variables**, chọn **Edit** và thêm các biến:
   - `MATCHMAKING_QUEUE_TABLE`: `MatchmakingQueue`
   - `ACTIVE_MATCHES_TABLE`: `ActiveMatches`

![Thêm biến môi trường](/images/5-Workshop/img_A/image42.png)

---

#### Bước 3: Deploy & Kiểm thử Lambda Function
1. Dán mã nguồn Node.js của Matchmaker vào trình chỉnh sửa và chọn **Deploy**.
2. Tạo dữ liệu test thử nghiệm cho `Player1` và `Player2`.
3. Kiểm tra thông báo thành công và xác nhận người chơi đã được thêm vào bảng `MatchmakingQueue`.

![Giao diện Code Lambda](/images/5-Workshop/img_A/image44.png)
![Kiểm thử Lambda thành công](/images/5-Workshop/img_A/image47.png)
