---
title: "Deploy REST API & Cognito Authorizer"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.3.2. </b> "
---

### Step-by-Step Implementation

#### Step 1: Create Amazon API Gateway REST API
1. Navigate to **API Gateway** console -> Click **Create API**.
2. Select **REST API** -> Build.
3. API Name: `FightingGameAPI`.

![API Gateway Console](/images/5-Workshop/img_A/image56.png)

---

#### Step 2: Create Resources `/join` & `/check`
1. Click **Create resource**:
   - Resource Name: `join` -> Create method `POST` -> Link to `FightingGameMatchmaker` Lambda.
2. Click **Create resource**:
   - Resource Name: `check` -> Create method `GET` -> Link to `FightingGameMatchmaker` Lambda.

![Create Resource Join](/images/5-Workshop/img_A/image61.png)
![Create Resource Check](/images/5-Workshop/img_A/image68.png)

---

#### Step 3: Configure Cognito Authorizer & CORS
1. Under **Authorizers**, click **Create authorizer**:
   - Name: `FightinggameCognitoAuthorizer`
   - Type: **Cognito**
   - User Pool: `ap-southeast-1_phYoaMUPC`
2. Attach `FightinggameCognitoAuthorizer` to `/join` (POST) and `/check` (GET) method request settings.
3. Enable **CORS** for both `/join` and `/check` endpoints.

![Create Cognito Authorizer](/images/5-Workshop/img_A/image72.png)
![Enable CORS](/images/5-Workshop/img_A/image78.png)

---

#### Step 4: Deploy API Gateway
1. Select `/` root resource -> Click **Deploy API**.
2. Deployment stage: `prod`.
   - **Invoke URL**: `https://6whg1d5qca.execute-api.ap-southeast-1.amazonaws.com/prod`

![Deploy API](/images/5-Workshop/img_A/image84.png)
