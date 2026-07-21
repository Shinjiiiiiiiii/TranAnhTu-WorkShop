---
title: "Matchmaker Lambda & API Gateway REST API"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

### Tổng quan
Trong chương này, bạn sẽ triển khai hàm AWS Lambda **FightingGameMatchmaker** để xử lý yêu cầu tham gia hàng chờ (`POST /join`) và kiểm tra trạng thái trận đấu (`GET /check`), sau đó công khai dịch vụ qua **Amazon API Gateway** tích hợp bảo mật Cognito Authorizer.

---

### Các bài học nhỏ
- [5.3.1 Xây dựng Matchmaker Lambda Function](5.3.1-create-matchmaker-lambda/)
- [5.3.2 Triển khai REST API & Cognito Authorizer](5.3.2-create-api-gateway/)
