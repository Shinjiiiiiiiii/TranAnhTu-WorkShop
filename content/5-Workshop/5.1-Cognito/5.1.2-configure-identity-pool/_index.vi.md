---
title: "Cấu hình App Client & Identity Pool"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.1.2. </b> "
---

### Các bước thực hiện

#### Bước 1: Cấu hình App Client
1. Vào mục **Applications** -> **App clients**.
2. Chọn client `FightingGame` và bấm Edit.
3. Tại **Authentication flows**, tích chọn `ALLOW_USER_PASSWORD_AUTH`.
4. Bấm **Save changes**.
   - **App Client ID**: `73ipqvvo7h3u0j3elfqlj23jo3`

![Cấu hình App Client](/images/5-Workshop/img_A/image12.png)
![Cho phép Password Auth](/images/5-Workshop/img_A/image14.png)

---

#### Bước 2: Tạo Cognito Identity Pool
1. Quay lại trang Cognito và chọn **Identity pools**.
2. Chọn **Create identity pool**.
3. Chọn **Authenticated access** -> **Amazon Cognito user pool**.

![Tạo Identity Pool](/images/5-Workshop/img_A/image17.png)
![Thiết lập Nhà cung cấp xác thực](/images/5-Workshop/img_A/image19.png)

4. Tại **Configure permissions**:
   - Tạo mới IAM Role với tên: `FightingGameAuthenticatedRole`.
5. Tại **Connect identity providers**:
   - Nhập User Pool ID (`ap-southeast-1_phYoaMUPC`) và App Client ID (`73ipqvvo7h3u0j3elfqlj23jo3`).
6. Đặt tên Pool: `FightingGameIdentityPool`.
7. Chọn **Create identity pool**.
   - **Identity Pool ID**: `ap-southeast-1:a5d743b9-e4a4-45d2-9cb1-9d214cee574c`

![Tạo Identity Pool thành công](/images/5-Workshop/img_A/image23.png)
