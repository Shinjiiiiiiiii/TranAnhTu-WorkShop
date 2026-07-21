---
title: "Xác thực người dùng với Amazon Cognito"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

# Xác thực người dùng với Amazon Cognito

### Tổng quan
Trong phần này, bạn sẽ thực hành cấu hình **Amazon Cognito User Pools** và **Cognito Identity Pools** để xử lý đăng ký, đăng nhập và cấp quyền IAM ngắn hạn cho client tải tài nguyên game.

---

### Các bước thực hiện

#### Bước 1: Chọn Region AWS
1. Chuyển đổi vùng làm việc trên AWS Management Console sang **Singapore (ap-southeast-1)**.

![Chọn Region Singapore](/images/5-Workshop/img_A/image1.png)

---

#### Bước 2: Tạo Cognito User Pool
1. Tìm kiếm **Cognito** trên thanh tìm kiếm của AWS Console.
2. Chọn **Get started for free**.
3. Chọn loại ứng dụng **Single-page application (SPA)** và điền tên: `FightingGame`.

![Cognito Console](/images/5-Workshop/img_A/image4.png)
![Cấu hình SPA](/images/5-Workshop/img_A/image6.png)

4. Tại mục **Configure options**:
   - Tích chọn **Username** cho phép người dùng tự đăng ký (Enable Self-registration).
   - Mụcs **Required attributes**: Chọn `email` phục vụ khôi phục mật khẩu.

![Cấu hình lựa chọn](/images/5-Workshop/img_A/image7.png)

5. Bấm **Create user directory**.
   - **User Pool ID**: `ap-southeast-1_phYoaMUPC`

---

#### Bước 3: Cấu hình App Client
1. Vào mục **Applications** -> **App clients**.
2. Chọn client `FightingGame` và bấm Edit.
3. Tại **Authentication flows**, tích chọn `ALLOW_USER_PASSWORD_AUTH`.
4. Bấm **Save changes**.
   - **App Client ID**: `73ipqvvo7h3u0j3elfqlj23jo3`

![Cấu hình App Client](/images/5-Workshop/img_A/image12.png)
![Cho phép Password Auth](/images/5-Workshop/img_A/image14.png)

---

#### Bước 4: Tạo Cognito Identity Pool
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

---

#### Bước 5: Kiểm tra giao diện đăng ký/đăng nhập người chơi
1. Mở giao diện frontend ứng dụng game.
2. Đăng ký tài khoản người chơi thử nghiệm.

![Giao diện Đăng ký người dùng](/images/5-Workshop/img_A/image99.png)
