---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

## Live-Service Game Backend Architecture on AWS

### Overview
This workshop provides a complete, step-by-step hands-on implementation guide for building a serverless and Spot Instance backend architecture for live-service multiplayer games on AWS.

* **Demo Web Link:** [http://fighting-game-assets-508768431157.s3-website-ap-southeast-1.amazonaws.com/](http://fighting-game-assets-508768431157.s3-website-ap-southeast-1.amazonaws.com/)
* **Source Code Link:** [https://github.com/Nothingtoread/fighting-game/tree/main](https://github.com/Nothingtoread/fighting-game/tree/main)

---

### Table of Contents

1. [5.1 User Authentication with Amazon Cognito](5.1-cognito/)
   - 5.1.1 Create Cognito User Pool
   - 5.1.2 Configure App Client & Identity Pool
   - 5.1.3 Verify User Registration UI
2. [5.2 Database Setup: DynamoDB](5.2-dynamodb/)
   - 5.2.1 Create MatchmakingQueue Table
   - 5.2.2 Create ActiveMatches Table
3. [5.3 Matchmaker Lambda & API Gateway REST API](5.3-lambda-api/)
   - 5.3.1 Build Matchmaker Lambda Function
   - 5.3.2 Deploy REST API & Cognito Authorizer
4. [5.4 EC2 Game Server & Auto Scaling Group Warm Pool](5.4-ec2-asg/)
   - 5.4.1 Launch EC2 Base & Setup Node.js Server
   - 5.4.2 Bake AMI & Create Launch Template
   - 5.4.3 Configure ASG Warm Pool & S3 Bucket
5. [5.5 GitOps CI/CD Pipeline & AWS CodeDeploy](5.5-gitops-codedeploy/)
   - 5.5.1 Setup GitHub OIDC Provider & IAM Roles
   - 5.5.2 Install CodeDeploy Agent on Ubuntu 24.04
   - 5.5.3 Create CodeDeploy App & Execute Pipeline
6. [5.6 Asynchronous Post-Match Processing](5.6-analytics-stream/)
   - 5.6.1 Enable DynamoDB Streams & IAM Roles
   - 5.6.2 Create MatchAnalytic Lambda & Verify Logs
7. [5.7 Resource Cleanup](5.7-cleanup/)
   - 5.7.1 Clean Up Cognito & DynamoDB
   - 5.7.2 Clean Up Lambda & API Gateway
   - 5.7.3 Clean Up CloudFront & WAF
