---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

## Xây dựng Kiến trúc Backend Game Live-Service trên AWS
### Hướng dẫn Triển khai Chi tiết từng bước (Hands-On Lab)

### Tổng quan
Bài lab thực hành (Workshop) này hướng dẫn chi tiết từng bước cách thiết lập và triển khai hệ thống Backend cho Game Live-Service trên đám mây AWS kết hợp kiến trúc Serverless và cụm máy chủ EC2 Spot Instance.

Bạn sẽ thực hành cấu hình xác thực người chơi với Amazon Cognito, xây dựng hàng đợi ghép trận với DynamoDB và AWS Lambda, công khai REST API qua Amazon API Gateway, quản lý cụm máy chủ EC2 Spot cho các phiên chơi game, tự động hóa quy trình CI/CD qua GitHub Actions & AWS CodeDeploy, và xử lý dữ liệu sau trận đấu bất đồng bộ với DynamoDB Streams.

### Nội dung bài Lab

1. [Xác thực người dùng với Amazon Cognito](5.1-Cognito/)
2. [Khởi tạo Cơ sở dữ liệu DynamoDB: MatchmakingQueue & ActiveMatches](5.2-DynamoDB/)
3. [Xây dựng Matchmaker Lambda & API Gateway REST API](5.3-Lambda-API/)
4. [Cấu hình EC2 Game Server & Auto Scaling Group Warm Pool](5.4-EC2-ASG/)
5. [Thiết lập Pipeline GitOps CI/CD & AWS CodeDeploy](5.5-GitOps-CodeDeploy/)
6. [Xử lý dữ liệu bất đồng bộ sau trận đấu với DynamoDB Streams](5.6-Analytics-Stream/)
