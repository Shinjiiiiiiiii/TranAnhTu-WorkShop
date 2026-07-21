---
title: "Triển khai REST API & Cognito Authorizer"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.3.2. </b> "
---

### Các bước thực hiện

#### Bước 1: Tạo Amazon API Gateway REST API
1. Mở console **API Gateway** -> Chọn **Create API**.
2. Chọn **REST API** -> Bấm Build.
3. Đặt tên API: `FightingGameAPI`.

![Tạo REST API](/images/5-Workshop/img_A/image56.png)

---

#### Bước 2: Khởi tạo Resource `/join` & `/check`
1. Bấm **Create resource**:
   - Resource Name: `join` -> Tạo method `POST` -> Kết nối với `FightingGameMatchmaker` Lambda.
2. Bấm **Create resource**:
   - Resource Name: `check` -> Tạo method `GET` -> Kết nối với `FightingGameMatchmaker` Lambda.

![Tạo Resource /join](/images/5-Workshop/img_A/image61.png)
![Tạo Resource /check](/images/5-Workshop/img_A/image68.png)

---

#### Bước 3: Thêm Cognito Authorizer & Cấu hình CORS
1. Vào mục **Authorizers** -> Bấm **Create authorizer**:
   - Name: `FightinggameCognitoAuthorizer`
   - Type: **Cognito**
   - User Pool: `ap-southeast-1_phYoaMUPC`
2. Gắn `FightinggameCognitoAuthorizer` vào Method Request của `/join` (POST) và `/check` (GET).
3. Bật **Enable CORS** cho cả hai resource `/join` và `/check`.

![Tạo Authorizer Cognito](/images/5-Workshop/img_A/image72.png)
![Enable CORS](/images/5-Workshop/img_A/image78.png)

---

#### Bước 4: Deploy API Gateway
1. Chọn gốc `/` -> Bấm **Deploy API**.
2. Deployment stage: `prod`.
   - **Invoke URL**: `https://6whg1d5qca.execute-api.ap-southeast-1.amazonaws.com/prod`

![Deploy API thành công](/images/5-Workshop/img_A/image84.png)
