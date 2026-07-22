---
title: "Clean Up Cognito & DynamoDB"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.7.1. </b> "
---

### Step-by-Step Implementation

#### Step 1: Delete Cognito User Pool
1. Go to the **Amazon Cognito** console -> **User pools**.
2. Select the User pool you created and click **Delete**.
3. Confirm deletion by typing the pool name.

![Delete Cognito User Pool](/images/5-Workshop/img_C/image1.png)
![Confirm Delete User Pool](/images/5-Workshop/img_C/image2.png)

---

#### Step 2: Delete Cognito Identity Pool
1. Select **Identity pools** from the Cognito dashboard.
2. Select the Identity pool you created and click **Delete**.
3. Confirm the deletion.

![Delete Cognito Identity Pool](/images/5-Workshop/img_C/image3.png)
![Confirm Delete Identity Pool](/images/5-Workshop/img_C/image4.png)

---

#### Step 3: Delete DynamoDB Tables
1. Go to the **Amazon DynamoDB** console -> **Tables**.
2. Select all the tables you created (`MatchmakingQueue`, `ActiveMatches`).
3. Click **Delete** and confirm.

![Delete DynamoDB Tables](/images/5-Workshop/img_C/image5.png)
![Confirm Delete Tables](/images/5-Workshop/img_C/image6.png)
