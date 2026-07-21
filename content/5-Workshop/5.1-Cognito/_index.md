---
title: "User Authentication with Amazon Cognito"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

### Overview
In this module, you will configure **Amazon Cognito User Pools** and **Cognito Identity Pools** to handle user sign-up, sign-in, and temporary IAM credential generation for downloading game assets.

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

---

#### Step 3: Configure App Client
1. Navigate to **Applications** -> **App clients**.
2. Select `FightingGame` app client.
3. Under **Authentication flows**, enable `ALLOW_USER_PASSWORD_AUTH`.
4. Save changes.
   - **App Client ID**: `73ipqvvo7h3u0j3elfqlj23jo3`

![App Client Settings](/images/5-Workshop/img_A/image12.png)
![Authentication Flow](/images/5-Workshop/img_A/image14.png)

---

#### Step 4: Create Cognito Identity Pool
1. Return to the Cognito dashboard and select **Identity pools**.
2. Click **Create identity pool**.
3. Select **Authenticated access** -> **Amazon Cognito user pool**.

![Create Identity Pool](/images/5-Workshop/img_A/image17.png)
![Identity Provider Settings](/images/5-Workshop/img_A/image19.png)

4. Under **Configure permissions**:
   - Create a new IAM Role named `FightingGameAuthenticatedRole`.
5. Under **Connect identity providers**:
   - Enter your User Pool ID (`ap-southeast-1_phYoaMUPC`) and App Client ID (`73ipqvvo7h3u0j3elfqlj23jo3`).
6. Name the pool: `FightingGameIdentityPool`.
7. Click **Create identity pool**.
   - **Identity Pool ID**: `ap-southeast-1:a5d743b9-e4a4-45d2-9cb1-9d214cee574c`

![Identity Pool Created](/images/5-Workshop/img_A/image23.png)

---

#### Step 5: Verify User Registration UI
1. Open the game client frontend.
2. Test user registration and authentication flow.

![User Registration UI](/images/5-Workshop/img_A/image99.png)
