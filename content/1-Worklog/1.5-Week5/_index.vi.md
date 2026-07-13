---
title: "Worklog Tuần 5"
date: 2026-06-01
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---
### Mục tiêu tuần 5:
* Tìm hiểu các dịch vụ cơ sở dữ liệu trên AWS bao gồm: Amazon RDS (Relational) và Amazon DynamoDB (NoSQL).
* Phân biệt kiến trúc cơ bản của cơ sở dữ liệu SQL (Quan hệ) và NoSQL (Phi quan hệ).
* Thực hành khởi tạo một cơ sở dữ liệu MySQL chạy trên Amazon RDS.
* Cấu hình kết nối an toàn từ máy chủ ảo EC2 tới cơ sở dữ liệu RDS.
* Thực hành quy trình sao lưu (snapshots) và khôi phục dữ liệu trên RDS.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------- |
| Hai | - Học lý thuyết về cơ sở dữ liệu quan hệ Amazon RDS: Các dòng DB Engine, tính năng Multi-AZ và Read Replicas | 01/06/2026 | 01/06/2026 | [Giới thiệu về Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) |
| Ba | - Tìm hiểu cơ sở dữ liệu NoSQL Amazon DynamoDB: Key-value, Table, Primary Key và cơ chế co giãn | 02/06/2026 | 02/06/2026 | [Tài liệu AWS DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) |
| Tư | - **Thực hành:** Khởi tạo một cơ sở dữ liệu MySQL trên RDS nằm trong phân vùng Private Subnet | 03/06/2026 | 03/06/2026 | [Khởi tạo DB MySQL trên RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingDeveloping.html) |
| Năm | - **Thực hành:** Cấu hình Security Group, mở quyền kết nối và dùng MySQL client từ EC2 kết nối tới RDS | 04/06/2026 | 04/06/2026 | [Kết nối EC2 với RDS MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.html) |
| Sáu | - **Thực hành:** Tạo bản sao lưu thủ công (Manual Snapshot), thiết lập backup tự động và khôi phục DB từ snapshot | 05/06/2026 | 05/06/2026 | [Sao lưu và phục hồi RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html) |

### Kết quả đạt được tuần 5:
* Phân biệt rõ ưu nhược điểm của cơ sở dữ liệu SQL và NoSQL để lựa chọn giải pháp lưu trữ dữ liệu phù hợp.
* Khởi tạo thành công cơ sở dữ liệu MySQL trên RDS trong phân vùng mạng riêng tư (Private Subnet).
* Phân quyền bảo mật tối đa bằng cách cấu hình Security Group của RDS chỉ cho phép kết nối đến từ Security Group của EC2 Instance.
* Kết nối thành công từ EC2 tới RDS, thực hiện các truy vấn SQL tạo bảng và ghi nhận dữ liệu thực tế.
* Nắm vững quy trình tạo Snapshot thủ công, lập lịch sao lưu tự động và khôi phục nhanh chóng khi có sự cố dữ liệu.
