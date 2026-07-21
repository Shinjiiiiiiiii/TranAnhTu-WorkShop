---
title: "Tạo Cognito User Pool"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.1.1. </b> "
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
