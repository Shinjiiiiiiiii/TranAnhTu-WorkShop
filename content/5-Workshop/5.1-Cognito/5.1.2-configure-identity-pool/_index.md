---
title: "Configure App Client & Identity Pool"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.1.2. </b> "
---

### Step-by-Step Implementation

#### Step 1: Configure App Client
1. Navigate to **Applications** -> **App clients**.
2. Select `FightingGame` app client.
3. Under **Authentication flows**, enable `ALLOW_USER_PASSWORD_AUTH`.
4. Save changes.
   - **App Client ID**: `73ipqvvo7h3u0j3elfqlj23jo3`

![App Client Settings](/images/5-Workshop/img_A/image12.png)
![Authentication Flow](/images/5-Workshop/img_A/image14.png)

---

#### Step 2: Create Cognito Identity Pool
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
