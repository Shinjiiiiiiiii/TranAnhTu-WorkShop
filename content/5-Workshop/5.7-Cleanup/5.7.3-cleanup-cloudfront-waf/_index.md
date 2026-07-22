---
title: "Clean Up CloudFront & WAF"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.7.3. </b> "
---

### Step-by-Step Implementation

#### Step 1: Disable and Delete CloudFront Distribution
1. Go to the **Amazon CloudFront** console -> **Distributions**.
2. Select the Distribution you created -> Click **Disable**.
3. Confirm and wait 5-10 minutes for status transition to completed.
4. Select it again and click **Delete**.

![Disable CloudFront Distribution](/images/5-Workshop/img_C/image11.png)
![Confirm Disable Distribution](/images/5-Workshop/img_C/image12.png)
![Delete CloudFront Distribution](/images/5-Workshop/img_C/image13.png)

---

#### Step 2: Disassociate and Delete WAF Web ACL
1. Go to the **AWS WAF & Shield** console -> **Web ACLs**.
2. Select your ACL (e.g. `CreatedByCloudFront-56a8180e`).
3. Go to **Associated AWS resources** and disassociate the CloudFront distribution.
4. Go back to Web ACLs list -> click **Delete**.

![Manage Associated WAF Resources](/images/5-Workshop/img_C/image14.png)
![Disassociate and Delete WAF ACL](/images/5-Workshop/img_C/image15.png)
