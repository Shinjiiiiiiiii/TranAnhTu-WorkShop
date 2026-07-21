---
title: "Launch EC2 Base & Setup Node.js Server"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.4.1. </b> "
---

### Step-by-Step Implementation

#### Step 1: Launch Base EC2 Instance
1. Navigate to **Amazon EC2** -> Click **Launch Instance**.
2. Name: `FightingGameServer`.
3. AMI: **Ubuntu Server 24.04 LTS**.
4. Instance Type: `t3.medium` (Graviton/x86 compatible).
5. Storage: 8 GB gp3.

![Launch EC2 Instance](/images/5-Workshop/img_A/image86.png)

---

#### Step 2: Set Up Node.js Game Server Environment
1. SSH into the EC2 instance.
2. Install Node.js runtime and dependencies.
3. Start the game server application and verify local port binding.

![Configure Node.js Game Server](/images/5-Workshop/img_A/image91.png)
![Test Game Server Connection](/images/5-Workshop/img_A/image97.png)
