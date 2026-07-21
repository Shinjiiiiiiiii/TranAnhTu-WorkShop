---
title: "Install CodeDeploy Agent on Ubuntu 24.04"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.5.2. </b> "
---

### Step-by-Step Implementation

#### Step 1: Install & Patch AWS CodeDeploy Agent on Ubuntu 24.04 LTS
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
