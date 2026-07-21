---
title: "Database Setup: DynamoDB Matchmaking Queue & Active Matches"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

### Overview
In this module, you will create two core **Amazon DynamoDB** tables: `MatchmakingQueue` (for pending players) and `ActiveMatches` (for active match sessions).

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

---

#### Step 3: Create Table `ActiveMatches`
1. Click **Create table**.
2. Enter Table Details:
   - **Table name**: `ActiveMatches`
   - **Partition key**: `playerId` (String)
   - **Sort key**: Leave blank
   - **Table settings**: Default settings
3. Click **Create table**.

![Create ActiveMatches Table](/images/5-Workshop/img_A/image28.png)

---

#### Step 4: Verify Tables Status
1. Check the table list to ensure both `MatchmakingQueue` and `ActiveMatches` have reached `Active` status.

![Active DynamoDB Tables](/images/5-Workshop/img_A/image29.png)
