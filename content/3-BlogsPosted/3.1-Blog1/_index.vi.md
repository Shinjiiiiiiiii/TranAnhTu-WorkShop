---
title: "Blog 1"
date: 2026-07-13
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---
# CÁCH LITHOLENS CỦA ALS GEOANALYTICS CÁCH MẠNG HÓA QUÁ TRÌNH GHI LOG MẪU LÕI BẰNG MÁY HỌC VỚI AMAZON EKS

ALS Geoanalytics đã phát triển **LithoLens**, một nền tảng cloud-native sử dụng thị giác máy tính và học máy (ML) để tự động hóa và tối ưu hóa quy trình ghi nhận nhật ký mẫu lõi địa chất (core logging). Hệ thống tự động thu thập dữ liệu đầu vào, phân loại và phân tích hình ảnh mẫu lõi khoan, giúp đẩy nhanh đáng kể tốc độ đánh giá địa chất phục vụ khai thác mỏ và thăm dò tài nguyên.

### Các thành phần kiến trúc chính:

* **Truy cập phía Client & Lớp API:**
  Các ứng dụng phía Client kết nối bảo mật qua **Amazon API Gateway** và **AWS Lambda** (API Layer), với việc xác thực người dùng được quản lý tập trung thông qua **Amazon Cognito**.
* **Lớp Tính toán & Xử lý (Compute & Processing):**
  **Amazon EKS (Elastic Kubernetes Service)** điều phối các tác vụ suy luận (inference) học máy đã được đóng gói container. Chạy mô hình trên EKS cho phép ALS tự động điều chỉnh quy mô tài nguyên (auto-scaling) linh hoạt dựa trên lượng ảnh lõi khoan cần xử lý.
* **Lớp Lưu trữ & Cơ sở dữ liệu:**
  * **Amazon S3** được dùng để lưu trữ dữ liệu ảnh lõi khoan độ phân giải cao với khối lượng cực lớn.
  * **Amazon RDS** quản lý các dữ liệu có cấu trúc (metadata), thông tin tài khoản và dữ liệu ghi nhận địa chất.
  * **Amazon CloudWatch** giám sát hiệu năng hoạt động của hệ thống và ghi nhận nhật ký vận hành (logs).

### Lợi ích của kiến trúc:
* **Khả năng mở rộng vượt trội:** Các cụm Kubernetes trong EKS tự động co giãn giúp đáp ứng tốt các tác vụ học máy tải cao.
* **Tối ưu chi phí:** Kết hợp dịch vụ serverless (API Gateway & Lambda) và container tự co giãn giúp ALS chỉ phải trả phí cho lượng tài nguyên thực tế sử dụng.
* **Hiệu năng xử lý:** Việc sử dụng các máy ảo tối ưu hóa GPU trong cụm EKS giúp tăng tốc độ suy luận deep learning cho hình ảnh lõi khoan.

---

### Sơ đồ kiến trúc (Architecture Diagram):
![Kiến trúc LithoLens](/images/3-BlogsPosted/blog1.png)

---

### Liên kết bài viết & tài liệu tham khảo:
* **Link bài viết (Facebook):** [AWS Study Group Facebook Post](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2199204024177891/)
* **Link tham khảo (AWS Blog):** [How ALS Geoanalytics’ LithoLens revolutionizes core logging through machine learning with Amazon EKS](https://aws.amazon.com/vi/blogs/architecture/how-als-geoanalytics-litholens-revolutionizes-core-logging-through-machine-learning-with-amazon-eks/)