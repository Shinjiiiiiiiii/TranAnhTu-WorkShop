---
title: "Worklog Tuần 7"
date: 2026-06-15
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---
### Mục tiêu tuần 7:
* Tìm hiểu khái niệm và lợi ích của Cơ sở hạ tầng dưới dạng mã (Infrastructure as Code - IaC).
* Học cú pháp công cụ HashiCorp Terraform: Cấu trúc quản lý State, Provider, Resource, Variable và Module.
* Tìm hiểu AWS CloudFormation dưới dạng dịch vụ IaC tích hợp sẵn của AWS.
* Thực hành viết mã nguồn Terraform để tự động hóa việc khởi tạo VPC, EC2 và S3 trên AWS.
* Quản lý vòng đời hệ thống tài nguyên thông qua mã nguồn.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------- |
| Hai | - Học lý thuyết về IaC và cú pháp ngôn ngữ HCL (HashiCorp Configuration Language) của Terraform | 15/06/2026 | 15/06/2026 | [Giới thiệu Terraform](https://developer.hashicorp.com/terraform/intro) |
| Ba | - Tìm hiểu quy trình làm việc chuẩn của Terraform qua các lệnh: `init`, `plan`, `apply`, `destroy` và tầm quan trọng của file State | 16/06/2026 | 16/06/2026 | [Các câu lệnh Terraform](https://developer.hashicorp.com/terraform/cli/commands) |
| Tư | - Tìm hiểu AWS CloudFormation: Cấu trúc file JSON/YAML, Stack, Nested Stack và cơ chế quản lý | 17/06/2026 | 17/06/2026 | [Giới thiệu AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) |
| Năm | - **Thực hành:** Viết mã nguồn Terraform tạo VPC, Public Subnet, Route Table và Internet Gateway | 18/06/2026 | 18/06/2026 | [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) |
| Sáu | - **Thực hành:** Mở rộng code Terraform để tạo thêm EC2 Instance và S3 Bucket; chạy triển khai kiểm thử hệ thống | 19/06/2026 | 19/06/2026 | [Thực hành Terraform trên AWS](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) |

### Kết quả đạt được tuần 7:
* Nắm vững triết lý quản lý hạ tầng theo kiểu Declarative (khai báo trạng thái mong muốn).
* Cài đặt thành công Terraform CLI trên máy tính cá nhân và cấu hình quyền truy cập AWS Provider.
* Viết thành thạo các file cấu hình `.tf` sử dụng biến (variables), đầu ra (outputs) và hiểu rõ nguyên lý lưu trữ của file `terraform.tfstate`.
* Triển khai tự động thành công toàn bộ hạ tầng gồm mạng VPC, máy chủ EC2 và bộ lưu trữ S3 chỉ với một câu lệnh `terraform apply`.
* Thành thạo kỹ năng dọn dẹp và xóa bỏ tài nguyên thử nghiệm một cách tự động bằng lệnh `terraform destroy`.
