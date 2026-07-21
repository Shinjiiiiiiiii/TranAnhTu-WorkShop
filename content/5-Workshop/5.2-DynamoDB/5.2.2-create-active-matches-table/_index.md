---
title: "Create ActiveMatches Table & Verify"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.2.2. </b> "
---

### Step-by-Step Implementation

#### Step 1: Create Table `ActiveMatches`
1. Click **Create table**.
2. Enter Table Details:
   - **Table name**: `ActiveMatches`
   - **Partition key**: `playerId` (String)
   - **Sort key**: Leave blank
   - **Table settings**: Default settings
3. Click **Create table**.

![Create ActiveMatches Table](/images/5-Workshop/img_A/image28.png)

---

#### Step 2: Verify Tables Status
1. Check the table list to ensure both `MatchmakingQueue` and `ActiveMatches` have reached `Active` status.

![Active DynamoDB Tables](/images/5-Workshop/img_A/image29.png)
