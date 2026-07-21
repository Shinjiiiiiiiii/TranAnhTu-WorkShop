---
title: "Configure ASG Warm Pool & S3 Bucket"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.4.3. </b> "
---

### Step-by-Step Implementation

#### Step 1: Configure Auto Scaling Group (ASG) Warm Pool
1. Create Auto Scaling Group: `FightingGameServerASG`.
2. Attach Launch Template.
3. Configure **Warm Pool** settings to maintain pre-initialized warm instances ready for instant match assignment.

![Configure ASG Warm Pool](/images/5-Workshop/img_B/image7.png)

---

#### Step 2: Create Amazon S3 Asset Bucket & Policy
1. Create S3 Bucket for client builds, patches, and game server bundles.
2. Configure **Public Read Bucket Policy** and **CORS** rules.

![S3 Bucket Policy](/images/5-Workshop/img_B/image10.png)

---

#### Step 3: Assign IAM Instance Profile
1. Create `FightingGameServerInstanceRole` with S3 read permissions.
2. Attach IAM Instance Profile to EC2 Launch Template.

![Attach Instance Role](/images/5-Workshop/img_B/image18.png)
