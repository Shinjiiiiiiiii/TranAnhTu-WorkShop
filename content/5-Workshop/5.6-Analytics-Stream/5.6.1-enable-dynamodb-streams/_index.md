---
title: "Enable DynamoDB Streams & IAM Roles"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.6.1. </b> "
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
