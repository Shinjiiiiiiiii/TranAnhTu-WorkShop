---
title: "Kích hoạt DynamoDB Streams & IAM Roles"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.6.1. </b> "
---

### Các bước thực hiện

#### Bước 1: Bật DynamoDB Streams
1. Vào **DynamoDB** console -> Chọn bảng `ActiveMatches`.
2. Tại mục **Exports and streams**, bật **DynamoDB stream** (View type: `NEW_AND_OLD_IMAGES`).

![Bật DynamoDB Stream](/images/5-Workshop/img_B/image33.png)

---

#### Bước 2: Tạo IAM Role cho Analytics Lambda
1. Tạo IAM Role `MatchAnalyticRole`.
2. Gắn Policy cho phép đọc dữ liệu từ DynamoDB Streams (`dynamodb:GetRecords`, `dynamodb:GetShardIterator`, `dynamodb:DescribeStream`, `dynamodb:ListStreams`).

![Tạo Role MatchAnalytic](/images/5-Workshop/img_B/image36.png)
![Policy đọc Stream](/images/5-Workshop/img_B/image37.png)
