---
title: "Thiết lập Pipeline GitOps CI/CD & AWS CodeDeploy"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

### Tổng quan
Trong phần này, bạn sẽ cấu hình **GitHub Actions OIDC** để xác thực không dùng access key tĩnh, cài đặt và patch **AWS CodeDeploy Agent** trên Ubuntu 24.04 LTS, cấu hình CodeDeploy Application và thực thi quy trình triển khai tự động không gây gián đoạn.

---

### Các bước thực hiện

#### Bước 1: Cấu hình GitHub OIDC Provider trong AWS IAM
1. Vào **IAM** -> **Identity providers** -> Thêm **GitHub OIDC Provider**.
2. Tạo IAM Role dành cho GitHub Actions với Trust Policy giới hạn quyền cho repository `Shinjiiiiiiiii/TranAnhTu-WorkShop`.

![Thêm GitHub OIDC Provider](/images/5-Workshop/img_B/image12.png)
![Cấu hình Trust Policy](/images/5-Workshop/img_B/image14.png)

---

#### Bước 2: Cài đặt & Patch CodeDeploy Agent trên Ubuntu 24.04 LTS
Chạy các lệnh sau trên EC2 instance để sửa lỗi tương thích phiên bản Ruby 3.3 trên Ubuntu 24.04:

```bash
# 1. Cài đặt các thư viện tiền đề
sudo apt-get update && sudo apt-get install -y ruby-full ruby-webrick wget gdebi-core

# 2. Tải gói cài đặt CodeDeploy
cd /tmp
wget https://aws-codedeploy-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/releases/codedeploy-agent_1.8.1-26_all.deb

# 3. Giải nén và sửa phụ thuộc Ruby trong file control
dpkg-deb -R codedeploy-agent_1.8.1-26_all.deb /tmp/codedeploy-extracted
sed -i "s/ruby3.2/ruby3.3/g" /tmp/codedeploy-extracted/DEBIAN/control
dpkg-deb -b /tmp/codedeploy-extracted /tmp/codedeploy-agent_fixed.deb

# 4. Cài đặt gói đã sửa và khởi chạy dịch vụ
sudo dpkg -i /tmp/codedeploy-agent_fixed.deb
sudo systemctl enable codedeploy-agent
sudo systemctl start codedeploy-agent
```

![Lệnh cài đặt CodeDeploy Agent](/images/5-Workshop/img_B/image27.png)

---

#### Bước 3: Tạo AWS CodeDeploy Application & Deployment Group
1. Tạo IAM Role cho CodeDeploy.
2. Tạo CodeDeploy Application: `FightingGameCodeDeployApp`.
3. Tạo Deployment Group cho cụm EC2 và Lambda.

![Tạo CodeDeploy Application](/images/5-Workshop/img_B/image29.png)
![Cấu hình Deployment Group](/images/5-Workshop/img_B/image30.png)

---

#### Bước 4: Thực thi Triển khai Tự động & Kiểm tra Lịch sử
1. Chạy GitHub Actions workflow để tự động deploy code mới.
2. Theo dõi tiến độ triển khai và xác nhận trạng thái thành công trong CodeDeploy Deployment History.

![Triển khai CodeDeploy thành công](/images/5-Workshop/img_B/image31.png)
