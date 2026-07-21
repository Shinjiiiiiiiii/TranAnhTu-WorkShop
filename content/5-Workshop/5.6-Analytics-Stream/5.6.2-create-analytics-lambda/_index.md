---
title: "Create MatchAnalytic Lambda & Verify Logs"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.6.2. </b> "
---

### Step-by-Step Implementation

#### Step 1: Create `MatchAnalyticLambda` Function
1. Navigate to **AWS Lambda** -> Click **Create function**.
2. Name: `MatchAnalyticLambda`.
3. Assign `MatchAnalyticRole`.

![Create MatchAnalytic Lambda](/images/5-Workshop/img_B/image39.png)

---

#### Step 2: Configure Event Source Mapping & Verify Analytics Output
1. Add DynamoDB Stream trigger to `MatchAnalyticLambda`.
2. Test match conclusion: when a match record transitions to finished state, `MatchAnalyticLambda` automatically processes player statistics and writes event logs to the analytics store.

![DynamoDB Stream Event Data](/images/5-Workshop/img_B/image40.png)
