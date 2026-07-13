---
title: "Week 9 Worklog"
date: 2026-06-29
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---
### Week 9 Objectives:
* Learn about systems monitoring and logging using Amazon CloudWatch.
* Understand audit trails and governance tracking via AWS CloudTrail.
* Study encryption and credential management tools: AWS Key Management Service (KMS) and AWS Secrets Manager.
* Set up metrics, dashboards, and CloudWatch Alarms.
* Secure applications by storing database passwords inside Secrets Manager.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | ------------------------------------------------------------------------------------------------------- |
| Mon | - Study Amazon CloudWatch architecture (metrics, logs, alarms, dashboards) | 06/29/2026 | 06/29/2026 | [Amazon CloudWatch Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) |
| Tue | - Study AWS CloudTrail: configuring trails, checking activity logs, and tracking API calls | 06/30/2026 | 06/30/2026 | [AWS CloudTrail Overview](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) |
| Wed | - Study AWS Key Management Service (KMS) and AWS Secrets Manager for security governance | 07/01/2026 | 07/01/2026 | [AWS Secrets Manager Introduction](https://docs.aws.amazon.com/secretsmanager/latest/userguide/Intro.html) |
| Thu | - **Practice:** Configure CloudWatch Alarms to monitor EC2 CPU usage (alert if > 80%) and create a simple monitoring dashboard | 07/02/2026 | 07/02/2026 | [Create CloudWatch Alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) |
| Fri | - **Practice:** Store database secrets in AWS Secrets Manager and retrieve them programmatically | 07/03/2026 | 07/03/2026 | [Retrieve Secret via Code](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html) |

### Week 9 Achievements:
* Gained comprehensive knowledge of AWS auditing, monitoring, and compliance structures.
* Configured custom CloudWatch Dashboards visualizing CPU utilization and network activity.
* Successfully set up an active CloudWatch Alarm with email notification (via SNS) when EC2 CPU exceeds 80%.
* Monitored management and data events using CloudTrail to audit administrative actions.
* Eliminated hardcoded passwords by migrating database credentials to AWS Secrets Manager, accessing them securely via IAM permissions.
