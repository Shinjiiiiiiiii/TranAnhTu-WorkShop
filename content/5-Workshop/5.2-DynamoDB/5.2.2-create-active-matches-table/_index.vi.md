---
title: "Tạo Bảng ActiveMatches & Kiểm tra"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.2.2. </b> "
---

### Các bước thực hiện

#### Bước 1: Tạo Bảng `ActiveMatches`
1. Chọn **Create table**.
2. Điền thông tin bảng:
   - **Table name**: `ActiveMatches`
   - **Partition key**: `playerId` (Kiểu dữ liệu: String)
   - **Sort key**: Để trống
   - **Table settings**: Giữ Default settings
3. Kéo xuống cuối trang và bấm **Create table**.

![Tạo bảng ActiveMatches](/images/5-Workshop/img_A/image28.png)

---

#### Bước 2: Kiểm tra trạng thái Bảng
1. Kiểm tra danh sách bảng đảm bảo cả `MatchmakingQueue` và `ActiveMatches` đều ở trạng thái `Active`.

![Bảng DynamoDB ở trạng thái Active](/images/5-Workshop/img_A/image29.png)
