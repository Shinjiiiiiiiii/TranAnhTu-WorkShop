---
title: "Worklog Tuần 4"
date: 2026-05-25
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---
### Mục tiêu tuần 4:
* Tìm hiểu dịch vụ mạng riêng ảo Amazon VPC (Virtual Private Cloud).
* Hiểu rõ các thành phần cấu tạo mạng: Subnet, Route Table, Internet Gateway (IGW) và NAT Gateway.
* So sánh cơ chế hoạt động của tường lửa Security Group (Stateful) và Network ACL (Stateless).
* Thiết kế mô hình mạng kết hợp phân vùng Public Subnet (Công khai) và Private Subnet (Riêng tư).
* Thực hành tự tay xây dựng một hệ thống VPC hoàn chỉnh từ đầu.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------- |
| Hai | - Học lý thuyết cơ bản về VPC: Cách chia dải IP (CIDR block), quy hoạch IP cho các Subnet | 25/05/2026 | 25/05/2026 | [Kiến thức cơ bản về VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| Ba | - Tìm hiểu về Route Table, Internet Gateway (IGW) và cơ chế định tuyến dữ liệu ra Internet | 26/05/2026 | 26/05/2026 | [Định tuyến trong VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) |
| Tư | - Tìm hiểu cơ chế hoạt động và vai trò bảo mật của NAT Gateway đối với Private Subnet | 27/05/2026 | 27/05/2026 | [NAT Gateway trong AWS](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) |
| Năm | - So sánh sự khác nhau về cơ chế lọc traffic giữa Security Group và Network ACL (NACL) | 28/05/2026 | 28/05/2026 | [Bảo mật trong VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html) |
| Sáu | - **Thực hành:** Thiết lập VPC tùy biến chứa Public/Private Subnet, tạo Route Table, IGW, NAT Gateway và khởi tạo EC2 chạy kiểm tra kết nối | 29/05/2026 | 29/05/2026 | [Tự xây dựng VPC hoàn chỉnh](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html) |

### Kết quả đạt được tuần 4:
* Nắm vững các kiến thức cốt lõi về thiết kế mạng đám mây, chia subnet và định tuyến.
* Thiết lập thành công một VPC tùy chỉnh với cấu trúc Public Subnet (dành cho Web Server) và Private Subnet (dành cho Database).
* Định tuyến thành công lưu lượng từ Public Subnet ra ngoài Internet qua Internet Gateway.
* Cấu hình NAT Gateway chạy ổn định, cho phép các tài nguyên chạy trong Private Subnet có thể tải thư viện/updates mà không bị truy cập trực tiếp từ Internet.
* Áp dụng thành công chính sách bảo mật đa tầng kết hợp Security Group ở cấp độ máy chủ ảo và Network ACL ở cấp độ subnet.
