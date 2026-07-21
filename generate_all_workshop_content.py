import os, shutil

base_dir = r"c:\Study\TranAnhTu-workshop-main"
workshop_dir = os.path.join(base_dir, "content", "5-Workshop")

# Remove old subfolders if they exist
old_folders = [
    "5.1-Workshop-overview",
    "5.2-Prerequiste",
    "5.3-S3-vpc",
    "5.4-S3-onprem",
    "5.5-Policy",
    "5.6-Cleanup"
]
for f in old_folders:
    path = os.path.join(workshop_dir, f)
    if os.path.exists(path):
        shutil.rmtree(path)

# New 6 chapters
chapters = [
    "5.1-Cognito",
    "5.2-DynamoDB",
    "5.3-Lambda-API",
    "5.4-EC2-ASG",
    "5.5-GitOps-CodeDeploy",
    "5.6-Analytics-Stream"
]

for ch in chapters:
    os.makedirs(os.path.join(workshop_dir, ch), exist_ok=True)

# 1. Main Workshop _index.md (EN)
main_index_en = """---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Live-Service Game Backend Architecture on AWS
## Step-by-Step Hands-On Implementation Guide

### Overview
This workshop provides a complete, step-by-step hands-on implementation guide for building a serverless and Spot Instance backend architecture for live-service multiplayer games on AWS.

You will learn how to configure authentication with Amazon Cognito, build a serverless matchmaking queue with DynamoDB and AWS Lambda, expose REST APIs using Amazon API Gateway, manage an EC2 Spot fleet for live game servers, automate deployments with GitHub Actions and AWS CodeDeploy, and process post-match analytics asynchronously with DynamoDB Streams.

### Table of Contents

1. [User Authentication with Amazon Cognito](5.1-Cognito/)
2. [Database Setup: DynamoDB Matchmaking Queue & Active Matches](5.2-DynamoDB/)
3. [Matchmaker Lambda & API Gateway REST API](5.3-Lambda-API/)
4. [EC2 Game Server & Auto Scaling Group Warm Pool](5.4-EC2-ASG/)
5. [GitOps CI/CD Pipeline & AWS CodeDeploy](5.5-GitOps-CodeDeploy/)
6. [Asynchronous Post-Match Processing with DynamoDB Streams](5.6-Analytics-Stream/)
"""

# Main Workshop _index.vi.md (VI)
main_index_vi = """---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Xây dựng Kiến trúc Backend Game Live-Service trên AWS
## Hướng dẫn Triển khai Chi tiết từng bước (Hands-On Lab)

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
"""

with open(os.path.join(workshop_dir, "_index.md"), "w", encoding="utf-8") as f:
    f.write(main_index_en)

with open(os.path.join(workshop_dir, "_index.vi.md"), "w", encoding="utf-8") as f:
    f.write(main_index_vi)

print("Main Workshop index generated!")
