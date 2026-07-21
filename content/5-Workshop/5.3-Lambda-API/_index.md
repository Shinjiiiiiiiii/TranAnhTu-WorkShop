---
title: "Matchmaker Lambda & API Gateway REST API"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# Matchmaker Lambda & API Gateway REST API

### Overview
In this module, you will build the **FightingGameMatchmaker** AWS Lambda function to process player queueing (`POST /join`) and match checks (`GET /check`), and expose these endpoints via **Amazon API Gateway** secured by Cognito Authorizer.

---

### Step-by-Step Implementation

#### Step 1: Create AWS Lambda Function
1. Navigate to **AWS Lambda** console -> Click **Create function**.
2. Function name: `FightingGameMatchmaker`.
3. Runtime: **Node.js 20.x**.

![Create Lambda Function](/images/5-Workshop/img_A/image31.png)

---

#### Step 2: Configure Lambda IAM Permissions & Environment Variables
1. Under **Configuration** -> **Permissions**, click the Execution Role link.
2. Add an inline policy granting `dynamodb:PutItem`, `dynamodb:GetItem`, `dynamodb:DeleteItem`, and `ec2:DescribeInstances` access.

![Lambda Permissions](/images/5-Workshop/img_A/image35.png)

3. Under **Environment variables**, click **Edit** and set:
   - `MATCHMAKING_QUEUE_TABLE`: `MatchmakingQueue`
   - `ACTIVE_MATCHES_TABLE`: `ActiveMatches`

![Environment Variables](/images/5-Workshop/img_A/image42.png)

---

#### Step 3: Deploy & Test Lambda Function
1. Paste the Matchmaker Node.js source code into the editor and click **Deploy**.
2. Test payload execution for `Player1` and `Player2`.
3. Verify that players are successfully inserted into `MatchmakingQueue`.

![Lambda Code Editor](/images/5-Workshop/img_A/image44.png)
![Lambda Test Result](/images/5-Workshop/img_A/image47.png)

---

#### Step 4: Create Amazon API Gateway REST API
1. Navigate to **API Gateway** console -> Click **Create API**.
2. Select **REST API** -> Build.
3. API Name: `FightingGameAPI`.

![API Gateway Console](/images/5-Workshop/img_A/image56.png)

---

#### Step 5: Create Resources `/join` & `/check`
1. Click **Create resource**:
   - Resource Name: `join` -> Create method `POST` -> Link to `FightingGameMatchmaker` Lambda.
2. Click **Create resource**:
   - Resource Name: `check` -> Create method `GET` -> Link to `FightingGameMatchmaker` Lambda.

![Create Resource Join](/images/5-Workshop/img_A/image61.png)
![Create Resource Check](/images/5-Workshop/img_A/image68.png)

---

#### Step 6: Configure Cognito Authorizer & CORS
1. Under **Authorizers**, click **Create authorizer**:
   - Name: `FightinggameCognitoAuthorizer`
   - Type: **Cognito**
   - User Pool: `ap-southeast-1_phYoaMUPC`
2. Attach `FightinggameCognitoAuthorizer` to `/join` (POST) and `/check` (GET) method request settings.
3. Enable **CORS** for both `/join` and `/check` endpoints.

![Create Cognito Authorizer](/images/5-Workshop/img_A/image72.png)
![Enable CORS](/images/5-Workshop/img_A/image78.png)

---

#### Step 7: Deploy API Gateway
1. Select `/` root resource -> Click **Deploy API**.
2. Deployment stage: `prod`.
   - **Invoke URL**: `https://6whg1d5qca.execute-api.ap-southeast-1.amazonaws.com/prod`

![Deploy API](/images/5-Workshop/img_A/image84.png)
