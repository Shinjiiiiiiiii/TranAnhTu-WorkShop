---
title: "Worklog Tuần 3"
date: 2026-05-18
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---
### Mục tiêu tuần 3:
* Tìm hiểu các loại dịch vụ lưu trữ dữ liệu của AWS bao gồm: EBS, EFS, S3 và Glacier.
* Học cách quản lý Bucket và Object trên Amazon S3.
* Thực hành cấu hình Static Website Hosting trên S3 để chạy một trang web tĩnh không dùng máy chủ.
* Cấu hình các tính năng nâng cao: Versioning (Quản lý phiên bản) và Lifecycle Policy (Quy trình vòng đời dữ liệu).
* Tìm hiểu cơ chế Backup (Sao lưu) và Restore (Phục hồi) dữ liệu hệ thống.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------- |
| Hai | - Tìm hiểu sự khác nhau và kịch bản sử dụng giữa EBS (Block Storage), EFS (File Storage) và S3 (Object Storage) | 18/05/2026 | 18/05/2026 | [So sánh các dịch vụ lưu trữ AWS](https://aws.amazon.com/products/storage/) |
| Ba | - Tìm hiểu nguyên lý hoạt động của Amazon S3 (Bucket, Object, Metadata, Namespace toàn cầu) | 19/05/2026 | 19/05/2026 | [Tài liệu cơ bản về Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |
| Tư | - **Thực hành:** Tạo S3 Bucket, upload tệp tin, cấu hình phân quyền truy cập Bucket Policy và Access Control List (ACL) | 20/05/2026 | 20/05/2026 | [Phân quyền trên Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) |
| Năm | - **Thực hành:** Triển khai một Website tĩnh trên Amazon S3 và kiểm tra truy cập từ Internet | 21/05/2026 | 21/05/2026 | [Lưu trữ Website tĩnh trên S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html) |
| Sáu | - **Thực hành:** Kích hoạt S3 Versioning, thiết lập Lifecycle Policy để chuyển dữ liệu cũ sang Amazon S3 Glacier lưu trữ giá rẻ | 22/05/2026 | 22/05/2026 | [Thiết lập Lifecycle Policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) |

### Kết quả đạt được tuần 3:
* Phân biệt rõ các giải pháp lưu trữ của AWS (EBS, EFS, S3) để áp dụng vào các dự án cụ thể.
* Thành thạo các thao tác tạo Bucket, tải lên tệp tin và thiết lập bảo mật/phân quyền truy cập trên S3.
* Triển khai thành công Website tĩnh chạy trực tiếp trên S3 với chi phí cực kỳ tối ưu.
* Thiết lập tính năng Versioning để theo dõi lịch sử chỉnh sửa file và bảo vệ dữ liệu chống xóa nhầm.
* Xây dựng thành công chính sách vòng đời (Lifecycle rules) tự động lưu trữ hoặc xóa dữ liệu hết hạn giúp tiết kiệm dung lượng lưu trữ.
