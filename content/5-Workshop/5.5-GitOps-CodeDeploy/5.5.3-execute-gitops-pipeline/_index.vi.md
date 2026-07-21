---
title: "Tạo CodeDeploy App & Triển khai Pipeline"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.5.3. </b> "
---

### Các bước thực hiện

#### Bước 1: Tạo AWS CodeDeploy Application & Deployment Group
1. Tạo IAM Role cho CodeDeploy.
2. Tạo CodeDeploy Application: `FightingGameCodeDeployApp`.
3. Tạo Deployment Group cho cụm EC2 và Lambda.

![Tạo CodeDeploy Application](/images/5-Workshop/img_B/image29.png)
![Cấu hình Deployment Group](/images/5-Workshop/img_B/image30.png)

---

#### Bước 2: Thực thi Triển khai Tự động & Kiểm tra Lịch sử
1. Chạy GitHub Actions workflow để tự động deploy code mới.
2. Theo dõi tiến độ triển khai và xác nhận trạng thái thành công trong CodeDeploy Deployment History.

![Triển khai CodeDeploy thành công](/images/5-Workshop/img_B/image31.png)
