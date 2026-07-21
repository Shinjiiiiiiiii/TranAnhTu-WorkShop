---
title: "EC2 Game Server & Auto Scaling Group Warm Pool"
date: 2026-07-21
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

### Overview
In this module, you will launch the baseline **EC2 Game Server**, bake a customized **AMI**, create a **Launch Template**, configure an **Auto Scaling Group (ASG) Warm Pool**, and set up the **Amazon S3 Asset Bucket**.

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

---

#### Step 3: Bake Custom AMI & Create Launch Template
1. Tag the running server instance.
2. Actions -> Image and templates -> **Create image** (`FightingGameServer-AMI`).

![Create AMI](/images/5-Workshop/img_B/image5.png)

3. Navigate to **Launch Templates** -> Click **Create launch template**:
   - Select `FightingGameServer-AMI`.
   - Set Purchasing Option: **Spot Instances**.

![Create Launch Template](/images/5-Workshop/img_B/image6.png)

---

#### Step 4: Configure Auto Scaling Group (ASG) Warm Pool
1. Create Auto Scaling Group: `FightingGameServerASG`.
2. Attach Launch Template.
3. Configure **Warm Pool** settings to maintain pre-initialized warm instances ready for instant match assignment.

![Configure ASG Warm Pool](/images/5-Workshop/img_B/image7.png)

---

#### Step 5: Create Amazon S3 Asset Bucket
1. Create S3 Bucket for client builds, patches, and game server bundles.
2. Configure **Public Read Bucket Policy** and **CORS** rules.

![S3 Bucket Policy](/images/5-Workshop/img_B/image10.png)

---

#### Step 6: Assign IAM Instance Profile
1. Create `FightingGameServerInstanceRole` with S3 read permissions.
2. Attach IAM Instance Profile to EC2 Launch Template.

![Attach Instance Role](/images/5-Workshop/img_B/image18.png)
