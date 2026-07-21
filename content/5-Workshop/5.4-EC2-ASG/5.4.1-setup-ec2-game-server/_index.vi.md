---
title: "Khởi tạo EC2 Game Server Node.js"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.4.1. </b> "
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
