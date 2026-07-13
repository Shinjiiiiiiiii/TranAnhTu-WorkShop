---
title: "Worklog Tuần 8"
date: 2026-06-22
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---
### Mục tiêu tuần 8:
* Học kiến thức cơ bản về đóng gói ứng dụng bằng Docker (Containerization).
* Thực hành viết Dockerfile, build Docker Image và chạy thử nghiệm Docker Container trên máy cục bộ.
* Tìm hiểu dịch vụ lưu trữ Docker image của AWS - Amazon ECR (Elastic Container Registry).
* Nghiên cứu dịch vụ quản lý Container - Amazon ECS (Elastic Container Service) và cơ chế Serverless AWS Fargate.
* Thực hành triển khai một ứng dụng web dạng container lên ECS sử dụng Fargate.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------- |
| Hai | - Học lý thuyết về Containerization vs Virtualization; cài đặt và cấu hình Docker Desktop | 22/06/2026 | 22/06/2026 | [Docker Get Started](https://docs.docker.com/get-started/) |
| Ba | - Tìm hiểu cú pháp viết Dockerfile (FROM, RUN, COPY, EXPOSE, CMD) <br> - **Thực hành:** Build Docker Image của một web app đơn giản | 23/06/2026 | 23/06/2026 | [Cú pháp viết Dockerfile](https://docs.docker.com/engine/reference/builder/) |
| Tư | - Tìm hiểu dịch vụ Amazon ECR (Private Repository) <br> - **Thực hành:** Cấu hình AWS CLI login vào ECR, tag và push Docker image lên ECR | 24/06/2026 | 24/06/2026 | [Amazon ECR là gì](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) |
| Năm | - Tìm hiểu cấu trúc Amazon ECS: Cluster, Task Definition, Service, Task và so sánh EC2 vs Fargate Launch Type | 25/06/2026 | 25/06/2026 | [Kiến trúc Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) |
| Sáu | - **Thực hành:** Tạo ECS Cluster, viết Task Definition lấy image từ ECR và chạy một Service bằng AWS Fargate | 26/06/2026 | 26/06/2026 | [Triển khai Container lên ECS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html) |

### Kết quả đạt được tuần 8:
* Hiểu rõ cơ chế đóng gói ứng dụng dạng Container bằng Docker so với máy ảo truyền thống.
* Đóng gói thành công ứng dụng Web (Node.js/Python) bằng cách xây dựng file cấu hình Dockerfile tối ưu.
* Tạo kho lưu trữ ECR private trên AWS và đẩy thành công Docker Image lên hệ thống thông qua AWS CLI.
* Thành thạo các thiết lập trên ECS bao gồm định nghĩa Task (Task Definition) với các giới hạn về RAM/CPU cụ thể.
* Khởi chạy thành công ứng dụng web không dùng máy chủ vật lý qua AWS Fargate và kiểm tra truy cập thông qua địa chỉ IP công khai.
