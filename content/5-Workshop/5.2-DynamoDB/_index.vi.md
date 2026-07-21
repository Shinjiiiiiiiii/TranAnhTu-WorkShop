---
title: "Cơ sở dữ liệu DynamoDB: MatchmakingQueue & ActiveMatches"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

### Tổng quan
Trong phần này, bạn sẽ tiến hành khởi tạo hai bảng **Amazon DynamoDB** cốt lõi: `MatchmakingQueue` (hàng chờ người chơi) và `ActiveMatches` (lưu phiên trận đấu đang diễn ra).

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

---

#### Bước 3: Tạo Bảng `ActiveMatches`
1. Chọn **Create table**.
2. Điền thông tin bảng:
   - **Table name**: `ActiveMatches`
   - **Partition key**: `playerId` (Kiểu dữ liệu: String)
   - **Sort key**: Để trống
   - **Table settings**: Giữ Default settings
3. Kéo xuống cuối trang và bấm **Create table**.

![Tạo bảng ActiveMatches](/images/5-Workshop/img_A/image28.png)

---

#### Bước 4: Kiểm tra trạng thái Bảng
1. Kiểm tra danh sách bảng đảm bảo cả `MatchmakingQueue` và `ActiveMatches` đều ở trạng thái `Active`.

![Bảng DynamoDB ở trạng thái Active](/images/5-Workshop/img_A/image29.png)
