---
title: "Cấu hình ASG Warm Pool & S3 Bucket"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.4.3. </b> "
---

### Các bước thực hiện

#### Bước 1: Cấu hình Auto Scaling Group (ASG) Warm Pool
1. Tạo Auto Scaling Group: `FightingGameServerASG`.
2. Gắn Launch Template vừa tạo.
3. Cấu hình **Warm Pool** để duy trì các instance khởi động sẵn (warm), đáp ứng việc gán phòng tức thì khi có trận đấu mới.

![Cấu hình ASG Warm Pool](/images/5-Workshop/img_B/image7.png)

---

#### Bước 2: Tạo Amazon S3 Asset Bucket & Policy
1. Tạo S3 Bucket lưu trữ các bản build client, patch và server binary.
2. Cấu hình **Bucket Policy** và quy tắc **CORS**.

![S3 Bucket Policy](/images/5-Workshop/img_B/image10.png)

---

#### Bước 3: Cấu hình IAM Instance Profile
1. Tạo IAM Role `FightingGameServerInstanceRole` cấp quyền truy cập S3.
2. Gắn IAM Instance Profile vào EC2 Launch Template.

![Gắn IAM Role cho EC2](/images/5-Workshop/img_B/image18.png)
