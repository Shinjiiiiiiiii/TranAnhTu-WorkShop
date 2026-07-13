---
title: "Worklog Tuần 6"
date: 2026-06-08
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---
### Mục tiêu tuần 6:
* Tìm hiểu về kiến trúc không máy chủ (Serverless) thông qua dịch vụ tính toán AWS Lambda.
* Nghiên cứu định tuyến API bằng dịch vụ Amazon API Gateway.
* Tìm hiểu các dịch vụ truyền tin nhắn và sự kiện: Amazon SNS, Amazon SQS và Amazon EventBridge.
* Thực hành xây dựng một REST API hoàn chỉnh không dùng máy chủ bằng Lambda.
* Tích hợp API Gateway với Lambda, tiến hành kiểm thử và theo dõi hoạt động hệ thống.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------- |
| Hai | - Học lý thuyết cơ bản về AWS Lambda: Cơ chế hoạt động (trực quan hóa kiến trúc Serverless), môi trường chạy và tối ưu hóa Cold Start | 08/06/2026 | 08/06/2026 | [Tài liệu hướng dẫn AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) |
| Ba | - Tìm hiểu dịch vụ Amazon API Gateway: Phương thức kết nối REST API, HTTP API và phân quyền CORS | 09/06/2026 | 09/06/2026 | [Tìm hiểu API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) |
| Tư | - Nghiên cứu hệ thống Event-driven: Amazon SNS (thông báo), Amazon SQS (hàng đợi tin nhắn) và EventBridge (quản lý sự kiện) | 10/06/2026 | 10/06/2026 | [Ứng dụng Serverless trên AWS](https://aws.amazon.com/serverless/) |
| Năm | - **Thực hành:** Viết mã nguồn Python/NodeJS trên Lambda, cấu hình trigger gọi hàm từ API Gateway | 11/06/2026 | 11/06/2026 | [Tích hợp API Gateway với Lambda](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html) |
| Sáu | - **Thực hành:** Deploy REST API endpoint (GET/POST), gửi dữ liệu test payload và debug logs trong CloudWatch Logs | 12/06/2026 | 12/06/2026 | [Giám sát Lambda bằng CloudWatch](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html) |

### Kết quả đạt được tuần 6:
* Nắm vững kiến trúc lập trình Serverless và mô hình thiết kế hệ thống dựa trên sự kiện (Event-driven Architecture).
* Viết và triển khai thành công mã nguồn Python/NodeJS chạy trực tiếp trên môi trường Serverless của AWS Lambda.
* Thiết lập thành công REST API bằng Amazon API Gateway.
* Tích hợp thành công API Gateway làm cổng kết nối chuyển tiếp dữ liệu đến hàm xử lý AWS Lambda (Lambda Proxy Integration).
* Sử dụng thành thạo các công cụ cURL/Postman để gọi thử nghiệm API và phân tích logs xử lý lỗi thông qua Amazon CloudWatch Logs.
* Hiểu cách liên kết và đồng bộ hóa các dịch vụ thông qua SQS và SNS.
