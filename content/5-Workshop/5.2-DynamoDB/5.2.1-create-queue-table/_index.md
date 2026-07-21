---
title: "Create MatchmakingQueue Table"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.2.1. </b> "
---

### Step-by-Step Implementation

#### Step 1: Open Amazon DynamoDB Console
1. Search for **DynamoDB** in the AWS search bar.
2. Click **Get started**.

![DynamoDB Console](/images/5-Workshop/img_A/image25.png)

---

#### Step 2: Create Table `MatchmakingQueue`
1. Click **Create table**.
2. Enter Table Details:
   - **Table name**: `MatchmakingQueue`
   - **Partition key**: `playerId` (String)
   - **Sort key**: Leave blank
   - **Table settings**: Default settings
3. Click **Create table**.

![Create MatchmakingQueue Table](/images/5-Workshop/img_A/image27.png)
