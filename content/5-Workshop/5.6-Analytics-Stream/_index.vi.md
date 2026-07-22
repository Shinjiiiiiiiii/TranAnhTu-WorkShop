---
title: "Xử lý dữ liệu bất đồng bộ sau trận đấu với DynamoDB Streams"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

### Tổng quan
Trong chương này, bạn sẽ bật **DynamoDB Streams** trên bảng `ActiveMatches`, khởi tạo hàm **MatchAnalyticLambda** và thu thập sự kiện kết thúc trận đấu bất đồng bộ để ghi log phân tích mà không gây ảnh hưởng tới độ trễ của hệ thống matchmaking.

---

### Các bài học nhỏ
- [5.6.1 Kích hoạt DynamoDB Streams & IAM Roles](5.6.1-enable-dynamodb-streams/)
- [5.6.2 Khởi tạo MatchAnalytic Lambda & Kiểm thử Log](5.6.2-create-analytics-lambda/)
