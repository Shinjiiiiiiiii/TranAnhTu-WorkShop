---
title: "Create CodeDeploy App & Execute Pipeline"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.5.3. </b> "
---

### Step-by-Step Implementation

#### Step 1: Create AWS CodeDeploy Application & Deployment Group
1. Create CodeDeploy Role for EC2 and Lambda deployments.
2. Create CodeDeploy Application: `FightingGameCodeDeployApp`.
3. Create Deployment Group targeting EC2 Spot instances and Lambda alias traffic shifting.

![CodeDeploy Application](/images/5-Workshop/img_B/image29.png)
![Deployment Group Config](/images/5-Workshop/img_B/image30.png)

---

#### Step 2: Execute Automated Deployment & Verify Logs
1. Trigger GitHub Actions workflow execution.
2. Monitor CodeDeploy job execution progress and verify deployment history.

![Successful CodeDeploy Job](/images/5-Workshop/img_B/image31.png)
