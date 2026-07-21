---
title: "Cấu hình GitHub OIDC Provider & IAM Roles"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.5.1. </b> "
---

### Các bước thực hiện

#### Bước 1: Cấu hình GitHub OIDC Provider trong AWS IAM
1. Vào **IAM** -> **Identity providers** -> Thêm **GitHub OIDC Provider**.
2. Tạo IAM Role dành cho GitHub Actions với Trust Policy giới hạn quyền cho repository `Shinjiiiiiiiii/TranAnhTu-WorkShop`.

![Thêm GitHub OIDC Provider](/images/5-Workshop/img_B/image12.png)
![Cấu hình Trust Policy](/images/5-Workshop/img_B/image14.png)
