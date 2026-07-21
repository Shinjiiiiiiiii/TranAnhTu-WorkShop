---
title: "Thiết lập Pipeline GitOps CI/CD & AWS CodeDeploy"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

### Tổng quan
Trong chương này, bạn sẽ cấu hình **GitHub Actions OIDC** để xác thực không dùng access key tĩnh, cài đặt và patch **AWS CodeDeploy Agent** trên Ubuntu 24.04 LTS, cấu hình CodeDeploy Application và thực thi quy trình triển khai tự động không gây gián đoạn.

---

### Các bài học nhỏ
- [5.5.1 Cấu hình GitHub OIDC Provider & IAM Roles](5.5.1-setup-github-oidc/)
- [5.5.2 Cài đặt CodeDeploy Agent trên Ubuntu 24.04](5.5.2-install-codedeploy-agent/)
- [5.5.3 Tạo CodeDeploy App & Triển khai Pipeline](5.5.3-execute-gitops-pipeline/)
