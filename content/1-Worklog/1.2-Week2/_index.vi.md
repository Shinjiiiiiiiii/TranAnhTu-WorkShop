---
title: "Worklog Tuần 2"
date: 2026-05-11
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---
### Mục tiêu tuần 2:
* Tìm hiểu dịch vụ máy chủ ảo Amazon EC2 (Elastic Compute Cloud).
* Hiểu rõ các khái niệm: Instance Types, AMI (Amazon Machine Image), Key Pair và Elastic IP.
* Học cách cấu hình Security Group làm tường lửa phân quyền truy cập.
* Thực hành khởi chạy và quản lý EC2 instance, triển khai một website đơn giản.
* Làm quen với khái niệm cân bằng tải Elastic Load Balancer (ELB) và tự động co giãn Auto Scaling.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------- |
| Hai | - Học lý thuyết về Amazon EC2 và phân loại các nhóm Instance Types (T, M, C, R, etc.) | 11/05/2026 | 11/05/2026 | [Các dòng Instance EC2](https://aws.amazon.com/ec2/instance-types/) |
| Ba | - Tìm hiểu cơ chế hoạt động của AMI, Key Pair và cách liên kết địa chỉ tĩnh Elastic IP | 12/05/2026 | 12/05/2026 | [Tìm hiểu về AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) |
| Tư | - Cấu hình Security Group mở các cổng kết nối cần thiết <br> - **Thực hành:** Khởi tạo EC2 và dùng SSH/PuTTY kết nối vào hệ thống | 13/05/2026 | 13/05/2026 | [Hướng dẫn kết nối EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) |
| Năm | - **Thực hành:** Cài đặt Nginx/Apache Web Server trên EC2 để host trang web HTML đơn giản | 14/05/2026 | 14/05/2026 | [Triển khai Web Server](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2023.html) |
| Sáu | - Tìm hiểu lý thuyết về Elastic Load Balancer (ALB, NLB) và nhóm tự động co giãn Auto Scaling Group (ASG) | 15/05/2026 | 15/05/2026 | [Tự động co giãn ASG](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) |

### Kết quả đạt được tuần 2:
* Hiểu rõ cơ chế hoạt động của máy chủ ảo EC2 trên AWS.
* Tạo và khởi chạy thành công một EC2 Instance chạy hệ điều hành Amazon Linux.
* Cấu hình Security Group bảo mật, cho phép truy cập SSH (cổng 22) và HTTP (cổng 80) từ bên ngoài.
* Triển khai thành công dịch vụ Nginx trên EC2 để chạy một trang web tĩnh cơ bản.
* Hiểu cách áp dụng Load Balancer và Auto Scaling để xây dựng ứng dụng có tính sẵn sàng cao (High Availability).
