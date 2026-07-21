---
title: "Create Cognito User Pool"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.1.1. </b> "
---

### Step-by-Step Implementation

#### Step 1: Select AWS Region
1. Switch your AWS Management Console region to **Singapore (ap-southeast-1)**.

![Select Region Singapore](/images/5-Workshop/img_A/image1.png)

---

#### Step 2: Create Cognito User Pool
1. Search for **Cognito** in the AWS Console search bar.
2. Click **Get started for free**.
3. Select **Single-page application (SPA)** and enter the Application name: `FightingGame`.

![Cognito Console](/images/5-Workshop/img_A/image4.png)
![SPA Configuration](/images/5-Workshop/img_A/image6.png)

4. Under **Configure options**:
   - Check **Username** self-registration.
   - Select **Required attributes**: Select `email` for password recovery.

![Configure Options](/images/5-Workshop/img_A/image7.png)

5. Click **Create user directory**.
   - **User Pool ID**: `ap-southeast-1_phYoaMUPC`
