---
title: "Đóng gói AMI & Tạo Launch Template"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.4.2. </b> "
---

### Các bước thực hiện

#### Bước 1: Gán Tag & Đóng gói AMI
1. Gán Tag định danh cho game server.
2. Chọn Actions -> Image and templates -> **Create image** (`FightingGameServer-AMI`).

![Tạo AMI](/images/5-Workshop/img_B/image5.png)

---

#### Bước 2: Tạo Launch Template Spot Fleet
1. Vào mục **Launch Templates** -> Bấm **Create launch template**:
   - Chọn AMI vừa tạo (`FightingGameServer-AMI`).
   - Cấu hình tùy chọn mua tài nguyên: **Spot Instances**.

![Tạo Launch Template Spot](/images/5-Workshop/img_B/image6.png)
