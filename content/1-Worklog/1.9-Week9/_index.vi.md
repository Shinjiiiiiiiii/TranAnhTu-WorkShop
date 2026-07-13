---
title: "Worklog Tuần 9"
date: 2026-06-29
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---
### Mục tiêu tuần 9:
* Tìm hiểu công cụ giám sát và thu thập logs hệ thống bằng Amazon CloudWatch.
* Nghiên cứu cơ chế kiểm toán và ghi nhật ký hoạt động hệ thống qua AWS CloudTrail.
* Tìm hiểu giải pháp quản lý khóa mã hóa (KMS) và lưu trữ thông tin nhạy cảm bảo mật (Secrets Manager).
* Thiết lập các chỉ số giám sát (metrics), biểu đồ theo dõi (dashboards) và cấu hình cảnh báo CloudWatch Alarm.
* Thực hành bảo mật thông tin kết nối DB bằng cách tích hợp Secrets Manager.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------- |
| Hai | - Học lý thuyết về Amazon CloudWatch: Quản lý Logs Group, chỉ số Metrics, Event và Alarm | 29/06/2026 | 29/06/2026 | [Tài liệu giám sát CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) |
| Ba | - Tìm hiểu AWS CloudTrail: Cấu hình ghi log, tra cứu lịch sử thay đổi tài nguyên và API calls | 30/06/2026 | 30/06/2026 | [Kiểm toán hệ thống qua CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) |
| Tư | - Nghiên cứu dịch vụ AWS KMS (Key Management Service) và Secrets Manager quản lý thông tin bảo mật | 01/07/2026 | 01/07/2026 | [Tìm hiểu AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/Intro.html) |
| Năm | - **Thực hành:** Tạo CloudWatch Alarm cảnh báo khi CPU EC2 > 80% và xây dựng Dashboard trực quan | 02/07/2026 | 02/07/2026 | [Cấu hình CloudWatch Alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) |
| Sáu | - **Thực hành:** Lưu trữ mật khẩu cơ sở dữ liệu trên Secrets Manager và thực hành gọi lấy thông tin từ ứng dụng | 03/07/2026 | 03/07/2026 | [Truy xuất dữ liệu Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html) |

### Kết quả đạt được tuần 9:
* Nắm vững các mô hình bảo mật, kiểm toán và giám sát tài nguyên của AWS.
* Thiết lập thành công CloudWatch Dashboard theo dõi hiệu năng hệ thống theo thời gian thực.
* Tạo thành công CloudWatch Alarm kích hoạt gửi email cảnh báo thông qua SNS khi máy chủ EC2 bị quá tải CPU (> 80%).
* Sử dụng CloudTrail để kiểm tra và theo dõi dấu vết các hành động quản trị, truy vết ai đã gọi API thao tác tài nguyên.
* Triển khai lưu trữ thành công thông tin đăng nhập database lên AWS Secrets Manager, loại bỏ hoàn toàn việc lưu hardcode mật khẩu trong source code.
