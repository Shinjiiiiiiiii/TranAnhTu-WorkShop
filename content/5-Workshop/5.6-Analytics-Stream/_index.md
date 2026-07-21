---
title: "Asynchronous Post-Match Processing with DynamoDB Streams"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

### Overview
In this module, you will enable **DynamoDB Streams** on the `ActiveMatches` table, create the **MatchAnalyticLambda** function, and capture post-match events asynchronously to log analytics without affecting matchmaking latency.

---

### Step-by-Step Implementation

#### Step 1: Enable DynamoDB Streams
1. Navigate to **DynamoDB** -> Select `ActiveMatches` table.
2. Under **Exports and streams**, enable **DynamoDB stream** (View type: `NEW_AND_OLD_IMAGES`).

![Enable DynamoDB Stream](/images/5-Workshop/img_B/image33.png)

---

#### Step 2: Create IAM Role for Analytics Lambda
1. Create IAM Role `MatchAnalyticRole`.
2. Attach policy granting read access to DynamoDB Streams (`dynamodb:GetRecords`, `dynamodb:GetShardIterator`, `dynamodb:DescribeStream`, `dynamodb:ListStreams`).

![Create MatchAnalytic Role](/images/5-Workshop/img_B/image36.png)
![Stream Reading Policy](/images/5-Workshop/img_B/image37.png)

---

#### Step 3: Create `MatchAnalyticLambda` Function
1. Navigate to **AWS Lambda** -> Click **Create function**.
2. Name: `MatchAnalyticLambda`.
3. Assign `MatchAnalyticRole`.

![Create MatchAnalytic Lambda](/images/5-Workshop/img_B/image39.png)

---

#### Step 4: Configure Event Source Mapping & Verify Analytics Output
1. Add DynamoDB Stream trigger to `MatchAnalyticLambda`.
2. Test match conclusion: when a match record transitions to finished state, `MatchAnalyticLambda` automatically processes player statistics and writes event logs to the analytics store.

![DynamoDB Stream Event Data](/images/5-Workshop/img_B/image40.png)
