---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

## Live-Service Game Backend Architecture on AWS
### Step-by-Step Hands-On Implementation Guide

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
