---
title: "Dọn dẹp Cognito & DynamoDB"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.7.1. </b> "
---

### Các bước thực hiện

#### Bước 1: Xóa Cognito User Pool
1. Truy cập **Amazon Cognito** console -> **User pools**.
2. Chọn User pool đã tạo và click **Delete**.
3. Xác nhận xóa bằng cách nhập tên pool.

![Xóa Cognito User Pool](/images/5-Workshop/img_C/image1.png)
![Xác nhận xóa User Pool](/images/5-Workshop/img_C/image2.png)

---

#### Bước 2: Xóa Cognito Identity Pool
1. Chọn **Identity pools** trên thanh điều hướng Cognito.
2. Chọn Identity pool đã tạo và click **Delete**.
3. Xác nhận hành động xóa.

![Xóa Cognito Identity Pool](/images/5-Workshop/img_C/image3.png)
![Xác nhận xóa Identity Pool](/images/5-Workshop/img_C/image4.png)

---

#### Bước 3: Xóa Bảng DynamoDB
1. Truy cập **Amazon DynamoDB** console -> **Tables**.
2. Chọn tất cả các bảng đã khởi tạo (`MatchmakingQueue`, `ActiveMatches`).
3. Nhấp **Delete** và xác nhận.

![Xóa Bảng DynamoDB](/images/5-Workshop/img_C/image5.png)
![Xác nhận xóa Bảng](/images/5-Workshop/img_C/image6.png)
