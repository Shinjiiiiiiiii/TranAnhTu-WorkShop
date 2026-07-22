---
title: "Dọn dẹp CloudFront & WAF"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.7.3. </b> "
---

### Các bước thực hiện

#### Bước 1: Vô hiệu hóa và Xóa CloudFront Distribution
1. Truy cập **Amazon CloudFront** console -> **Distributions**.
2. Chọn Distribution đã khởi tạo -> Click **Disable**.
3. Xác nhận và đợi 5-10 phút để quá trình vô hiệu hóa hoàn tất.
4. Chọn lại Distribution đó và bấm **Delete** để xóa hẳn.

![Vô hiệu hóa CloudFront Distribution](/images/5-Workshop/img_C/image11.png)
![Xác nhận vô hiệu hóa](/images/5-Workshop/img_C/image12.png)
![Xóa CloudFront Distribution](/images/5-Workshop/img_C/image13.png)

---

#### Bước 2: Gỡ liên kết và Xóa WAF Web ACL
1. Truy cập **AWS WAF & Shield** console -> **Web ACLs**.
2. Chọn Web ACL của bạn (ví dụ: `CreatedByCloudFront-56a8180e`).
3. Chọn tab **Associated AWS resources** và gỡ liên kết (Disassociate) với CloudFront distribution.
4. Quay lại danh sách Web ACLs -> Chọn ACL và bấm **Delete**.

![Quản lý tài nguyên liên kết WAF](/images/5-Workshop/img_C/image14.png)
![Gỡ liên kết và Xóa WAF ACL](/images/5-Workshop/img_C/image15.png)
