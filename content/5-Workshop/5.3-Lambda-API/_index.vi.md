---
title: "Matchmaker Lambda & API Gateway REST API"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# Matchmaker Lambda & API Gateway REST API

### Tổng quan
Trong phần này, bạn sẽ triển khai hàm AWS Lambda **FightingGameMatchmaker** để xử lý yêu cầu tham gia hàng chờ (`POST /join`) và kiểm tra trạng thái trận đấu (`GET /check`), sau đó công khai dịch vụ qua **Amazon API Gateway** tích hợp bảo mật Cognito Authorizer.

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

---

#### Bước 4: Tạo Amazon API Gateway REST API
1. Mở console **API Gateway** -> Chọn **Create API**.
2. Chọn **REST API** -> Bấm Build.
3. Đặt tên API: `FightingGameAPI`.

![Tạo REST API](/images/5-Workshop/img_A/image56.png)

---

#### Bước 5: Khởi tạo Resource `/join` & `/check`
1. Bấm **Create resource**:
   - Resource Name: `join` -> Tạo method `POST` -> Kết nối với `FightingGameMatchmaker` Lambda.
2. Bấm **Create resource**:
   - Resource Name: `check` -> Tạo method `GET` -> Kết nối với `FightingGameMatchmaker` Lambda.

![Tạo Resource /join](/images/5-Workshop/img_A/image61.png)
![Tạo Resource /check](/images/5-Workshop/img_A/image68.png)

---

#### Bước 6: Thêm Cognito Authorizer & Cấu hình CORS
1. Vào mục **Authorizers** -> Bấm **Create authorizer**:
   - Name: `FightinggameCognitoAuthorizer`
   - Type: **Cognito**
   - User Pool: `ap-southeast-1_phYoaMUPC`
2. Gắn `FightinggameCognitoAuthorizer` vào Method Request của `/join` (POST) và `/check` (GET).
3. Bật **Enable CORS** cho cả hai resource `/join` và `/check`.

![Tạo Authorizer Cognito](/images/5-Workshop/img_A/image72.png)
![Enable CORS](/images/5-Workshop/img_A/image78.png)

---

#### Bước 7: Deploy API Gateway
1. Chọn gốc `/` -> Bấm **Deploy API**.
2. Deployment stage: `prod`.
   - **Invoke URL**: `https://6whg1d5qca.execute-api.ap-southeast-1.amazonaws.com/prod`

![Deploy API thành công](/images/5-Workshop/img_A/image84.png)
