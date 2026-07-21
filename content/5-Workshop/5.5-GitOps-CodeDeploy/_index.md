---
title: "GitOps CI/CD Pipeline & AWS CodeDeploy"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# GitOps CI/CD Pipeline & AWS CodeDeploy

### Overview
In this module, you will integrate **GitHub Actions OIDC** for passwordless authentication, install and patch the **AWS CodeDeploy Agent** on Ubuntu 24.04 LTS, configure CodeDeploy applications, and execute automated zero-downtime deployments.

---

### Step-by-Step Implementation

#### Step 1: Configure GitHub OIDC Provider in AWS IAM
1. Navigate to **IAM** -> **Identity providers** -> Add **GitHub OIDC Provider**.
2. Create an IAM Role for GitHub Actions with trust policy restricted to `Shinjiiiiiiiii/TranAnhTu-WorkShop`.

![Add GitHub OIDC Provider](/images/5-Workshop/img_B/image12.png)
![GitHub Role Trust Policy](/images/5-Workshop/img_B/image14.png)

---

#### Step 2: Install & Patch AWS CodeDeploy Agent on Ubuntu 24.04 LTS
Execute the following commands on the EC2 instance to patch the Ruby 3.3 dependency compatibility issue:

```bash
# 1. Install prerequisites
sudo apt-get update && sudo apt-get install -y ruby-full ruby-webrick wget gdebi-core

# 2. Download CodeDeploy deb package
cd /tmp
wget https://aws-codedeploy-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/releases/codedeploy-agent_1.8.1-26_all.deb

# 3. Unpack and fix Ruby dependency
dpkg-deb -R codedeploy-agent_1.8.1-26_all.deb /tmp/codedeploy-extracted
sed -i "s/ruby3.2/ruby3.3/g" /tmp/codedeploy-extracted/DEBIAN/control
dpkg-deb -b /tmp/codedeploy-extracted /tmp/codedeploy-agent_fixed.deb

# 4. Install patched package and start service
sudo dpkg -i /tmp/codedeploy-agent_fixed.deb
sudo systemctl enable codedeploy-agent
sudo systemctl start codedeploy-agent
```

![CodeDeploy Installation Script](/images/5-Workshop/img_B/image27.png)

---

#### Step 3: Create AWS CodeDeploy Application & Deployment Group
1. Create CodeDeploy Role for EC2 and Lambda deployments.
2. Create CodeDeploy Application: `FightingGameCodeDeployApp`.
3. Create Deployment Group targeting EC2 Spot instances and Lambda alias traffic shifting.

![CodeDeploy Application](/images/5-Workshop/img_B/image29.png)
![Deployment Group Config](/images/5-Workshop/img_B/image30.png)

---

#### Step 4: Execute Automated Deployment & Verify Logs
1. Trigger GitHub Actions workflow execution.
2. Monitor CodeDeploy job execution progress and verify deployment history.

![Successful CodeDeploy Job](/images/5-Workshop/img_B/image31.png)
