---
title: "Build Matchmaker Lambda Function"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.3.1. </b> "
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
