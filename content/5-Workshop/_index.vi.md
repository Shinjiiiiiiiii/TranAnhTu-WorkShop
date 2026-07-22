---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

## Xây dựng Kiến trúc Backend Game Live-Service trên AWS

### Tổng quan
Bài lab thực hành (Workshop) này hướng dẫn chi tiết từng bước cách thiết lập và triển khai hệ thống Backend cho Game Live-Service trên đám mây AWS kết hợp kiến trúc Serverless và cụm máy chủ EC2 Spot Instance.

* **Link web demo:** [http://fighting-game-assets-508768431157.s3-website-ap-southeast-1.amazonaws.com/](http://fighting-game-assets-508768431157.s3-website-ap-southeast-1.amazonaws.com/)
* **Link source code:** [https://github.com/Nothingtoread/fighting-game/tree/main](https://github.com/Nothingtoread/fighting-game/tree/main)

---

### Nội dung bài Lab

1. [5.1 Xác thực người dùng với Amazon Cognito](5.1-cognito/)
   - 5.1.1 Tạo Cognito User Pool
   - 5.1.2 Cấu hình App Client & Identity Pool
   - 5.1.3 Kiểm thử Giao diện Đăng ký Người dùng
2. [5.2 Khởi tạo Cơ sở dữ liệu DynamoDB](5.2-dynamodb/)
   - 5.2.1 Tạo Bảng MatchmakingQueue
   - 5.2.2 Tạo Bảng ActiveMatches
3. [5.3 Matchmaker Lambda & API Gateway REST API](5.3-lambda-api/)
   - 5.3.1 Xây dựng Matchmaker Lambda Function
   - 5.3.2 Triển khai REST API & Cognito Authorizer
4. [5.4 Cấu hình EC2 Game Server & ASG Warm Pool](5.4-ec2-asg/)
   - 5.4.1 Khởi tạo EC2 Game Server Node.js
   - 5.4.2 Đóng gói AMI & Tạo Launch Template
   - 5.4.3 Cấu hình ASG Warm Pool & S3 Bucket
5. [5.5 Thiết lập Pipeline GitOps CI/CD & AWS CodeDeploy](5.5-gitops-codedeploy/)
   - 5.5.1 Cấu hình GitHub OIDC Provider & IAM Roles
   - 5.5.2 Cài đặt CodeDeploy Agent trên Ubuntu 24.04
   - 5.5.3 Tạo CodeDeploy App & Triển khai Pipeline
6. [5.6 Xử lý dữ liệu bất đồng bộ sau trận đấu](5.6-analytics-stream/)
   - 5.6.1 Kích hoạt DynamoDB Streams & IAM Roles
   - 5.6.2 Khởi tạo MatchAnalytic Lambda & Kiểm thử Log
7. [5.7 Dọn dẹp tài nguyên](5.7-cleanup/)
   - 5.7.1 Dọn dẹp Cognito & DynamoDB
   - 5.7.2 Dọn dẹp Lambda & API Gateway
   - 5.7.3 Dọn dẹp CloudFront & WAF
