---
title: "Matchmaker Lambda & API Gateway REST API"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

### Overview
In this chapter, you will build the **FightingGameMatchmaker** AWS Lambda function to process player queueing (`POST /join`) and match checks (`GET /check`), and expose these endpoints via **Amazon API Gateway** secured by Cognito Authorizer.

---

### Sub-modules
- [5.3.1 Build Matchmaker Lambda Function](5.3.1-create-matchmaker-lambda/)
- [5.3.2 Deploy REST API & Cognito Authorizer](5.3.2-create-api-gateway/)
