---
title: "Cấu hình EC2 Game Server & ASG Warm Pool"
date: 2026-07-21
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

### Tổng quan
Trong phần này, bạn sẽ khởi tạo máy chủ game mẫu trên **Amazon EC2**, đóng gói **AMI**, thiết lập **Launch Template**, cấu hình **Auto Scaling Group (ASG) Warm Pool** và khởi tạo **S3 Asset Bucket**.

---

### Các bước thực hiện

#### Bước 1: Khởi tạo EC2 Instance gốc
1. Vào **Amazon EC2** console -> Chọn **Launch Instance**.
2. Name: `FightingGameServer`.
3. AMI: **Ubuntu Server 24.04 LTS**.
4. Instance Type: `t3.medium`.
5. Storage: 8 GB gp3.

![Khởi tạo EC2 Instance](/images/5-Workshop/img_A/image86.png)

---

#### Bước 2: Thiết lập môi trường Game Server Node.js
1. Kết nối SSH vào EC2 instance.
2. Cài đặt Node.js runtime và các gói phụ thuộc.
3. Khởi chạy ứng dụng game server và kiểm thử kết nối cổng thành công.

![Cấu hình Node.js Game Server](/images/5-Workshop/img_A/image91.png)
![Kiểm thử kết nối Game Server](/images/5-Workshop/img_A/image97.png)

---

#### Bước 3: Gán Tag, Đóng gói AMI & Tạo Launch Template
1. Gán Tag định danh cho game server.
2. Chọn Actions -> Image and templates -> **Create image** (`FightingGameServer-AMI`).

![Tạo AMI](/images/5-Workshop/img_B/image5.png)

3. Vào mục **Launch Templates** -> Bấm **Create launch template**:
   - Chọn AMI vừa tạo (`FightingGameServer-AMI`).
   - Cấu hình tùy chọn mua tài nguyên: **Spot Instances**.

![Tạo Launch Template Spot](/images/5-Workshop/img_B/image6.png)

---

#### Bước 4: Cấu hình Auto Scaling Group (ASG) Warm Pool
1. Tạo Auto Scaling Group: `FightingGameServerASG`.
2. Gắn Launch Template vừa tạo.
3. Cấu hình **Warm Pool** để duy trì các instance khởi động sẵn (warm), đáp ứng việc gán phòng tức thì khi có trận đấu mới.

![Cấu hình ASG Warm Pool](/images/5-Workshop/img_B/image7.png)

---

#### Bước 5: Tạo Amazon S3 Asset Bucket
1. Tạo S3 Bucket lưu trữ các bản build client, patch và server binary.
2. Cấu hình **Bucket Policy** và quy tắc **CORS**.

![S3 Bucket Policy](/images/5-Workshop/img_B/image10.png)

---

#### Bước 6: Cấu hình IAM Instance Profile
1. Tạo IAM Role `FightingGameServerInstanceRole` cấp quyền truy cập S3.
2. Gắn IAM Instance Profile vào EC2 Launch Template.

![Gắn IAM Role cho EC2](/images/5-Workshop/img_B/image18.png)
