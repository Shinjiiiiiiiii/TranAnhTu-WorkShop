---
title: "Bake AMI & Create Launch Template"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.4.2. </b> "
---

### Step-by-Step Implementation

#### Step 1: Bake Custom AMI
1. Tag the running server instance.
2. Actions -> Image and templates -> **Create image** (`FightingGameServer-AMI`).

![Create AMI](/images/5-Workshop/img_B/image5.png)

---

#### Step 2: Create Launch Template for Spot Fleet
1. Navigate to **Launch Templates** -> Click **Create launch template**:
   - Select `FightingGameServer-AMI`.
   - Set Purchasing Option: **Spot Instances**.

![Create Launch Template](/images/5-Workshop/img_B/image6.png)
