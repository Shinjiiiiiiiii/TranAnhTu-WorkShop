---
title: "Tạo Bảng MatchmakingQueue"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.2.1. </b> "
---

### Các bước thực hiện

#### Bước 1: Truy cập Amazon DynamoDB Console
1. Tìm kiếm **DynamoDB** trên thanh tìm kiếm AWS.
2. Chọn **Get started**.

![DynamoDB Console](/images/5-Workshop/img_A/image25.png)

---

#### Bước 2: Tạo Bảng `MatchmakingQueue`
1. Chọn **Create table**.
2. Điền thông tin bảng:
   - **Table name**: `MatchmakingQueue`
   - **Partition key**: `playerId` (Kiểu dữ liệu: String)
   - **Sort key**: Để trống
   - **Table settings**: Giữ Default settings
3. Kéo xuống cuối trang và bấm **Create table**.

![Tạo bảng MatchmakingQueue](/images/5-Workshop/img_A/image27.png)
