---
title: "Blog 2"
date: 2026-07-13
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---
# KHỞI TẠO TÀI NGUYÊN ORACLE DATABASE@AWS BẰNG TERRAFORM

Bài viết này tìm hiểu về giải pháp **Oracle Database@AWS**, một dịch vụ co-location đặc biệt giúp đưa các dịch vụ cơ sở dữ liệu của Oracle Cloud Infrastructure (OCI) chạy trực tiếp bên trong trung tâm dữ liệu của AWS. Giải pháp này cho phép doanh nghiệp vận hành cơ sở dữ liệu Oracle Exadata hiệu năng cao trên phần cứng OCI chuyên dụng với độ trễ kết nối cực thấp (dưới 1 mili-giây) tới các dịch vụ AWS như Amazon EC2.

### Các thành phần kiến trúc chính:

* **Customer VPC & Lớp ứng dụng:**
  Các ứng dụng chạy trên các máy chủ ảo **Amazon EC2** đặt trong mạng Customer VPC của AWS.
* **Mạng cơ sở dữ liệu Oracle (ODB Network):**
  Một phân vùng VPC ODB Network được thiết lập trong AWS Region, chứa các subnet kết nối (client subnet) và sao lưu (backup subnet). Phân vùng này kết nối trực tiếp với Customer VPC thông qua liên kết **ODB Peering**.
* **OCI Child Site (Đặt tại trung tâm dữ liệu AWS):**
  Phân vùng phần cứng OCI được co-locate trong AWS Datacenter, chứa hạ tầng vật lý **Exadata Infrastructure** chạy trên OCI Virtual Cloud Network (VCN) có các subnet kết nối tương thích với AWS.
* **Control Plane & Tự động hóa:**
  Quy trình khởi tạo và quản lý vòng đời tài nguyên được điều khiển tự động bởi **OCI Automation** liên kết trực tiếp với **OCI Control Plane** ở OCI Parent Region.

### Quản lý hạ tầng bằng Terraform (IaC):
Sử dụng đồng thời AWS Provider và OCI Provider trong **Terraform** giúp kỹ sư tự động hóa hoàn toàn quy trình khởi tạo tài nguyên đa đám mây (multi-cloud):
1. Khởi tạo VPC, Subnet, Route Table và máy chủ EC2 phía AWS.
2. Cấu hình OCI provider để tạo Exadata Infrastructure.
3. Thiết lập kết nối mạng riêng tư và định tuyến bảo mật giữa AWS VPC và OCI VCN tự động.

---

### Sơ đồ kiến trúc (Architecture Diagram):
![Kiến trúc Oracle Database@AWS](/images/3-BlogsPosted/blog2.png)

---

### Liên kết bài viết & tài liệu tham khảo:
* **Link bài viết (Facebook):** [AWS Study Group Facebook Post](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2198792150885745/)
* **Link tham khảo (AWS Blog):** [Provision Oracle Database and AWS resources using Terraform](https://aws.amazon.com/vi/blogs/database/provision-oracle-databaseaws-resources-using-terraform/)