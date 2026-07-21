---
title: "Cài đặt CodeDeploy Agent trên Ubuntu 24.04"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.5.2. </b> "
---

### Các bước thực hiện

#### Bước 1: Cài đặt & Patch CodeDeploy Agent trên Ubuntu 24.04 LTS
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
