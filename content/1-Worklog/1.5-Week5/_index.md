---
title: "Week 5 Worklog"
date: 2026-06-01
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---
### Week 5 Objectives:
* Learn about database services on AWS: Relational (Amazon RDS) and Non-Relational (Amazon DynamoDB).
* Understand the core architectural differences between SQL (Relational) and NoSQL (Document/Key-Value) databases.
* Practice provisioning an Amazon RDS MySQL instance.
* Connect an application hosted on an EC2 instance securely to the RDS database.
* Configure backup and restore procedures on RDS.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | ------------------------------------------------------------------------------------------------------- |
| Mon | - Study relational database architecture on AWS: Amazon RDS features, Multi-AZ, and Read Replicas | 06/01/2026 | 06/01/2026 | [Amazon RDS Overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) |
| Tue | - Study NoSQL databases: Amazon DynamoDB concepts, primary keys, indexes, and write capacity units | 06/02/2026 | 06/02/2026 | [Amazon DynamoDB Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) |
| Wed | - **Practice:** Provision a MySQL database instance in Amazon RDS inside the private subnet | 06/03/2026 | 06/03/2026 | [Create an RDS MySQL DB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingDeveloping.html) |
| Thu | - **Practice:** Configure security groups and connect an EC2 instance to the RDS instance via MySQL client | 06/04/2026 | 06/04/2026 | [Connect EC2 to RDS MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.html) |
| Fri | - **Practice:** Perform manual snapshots, set up automated backups, and practice database recovery | 06/05/2026 | 06/05/2026 | [RDS Backups and Restores](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html) |

### Week 5 Achievements:
* Mastered SQL vs NoSQL differences and learned when to use RDS vs DynamoDB.
* Created a private database subnet group and successfully deployed an RDS MySQL instance inside a private subnet.
* Set up secure EC2-to-RDS communication by restricting RDS Security Group access rules exclusively to the EC2 security group.
* Populated tables, executed SQL queries from EC2, and verified data storage.
* Configured automated nightly backups and successfully restored database data from a manual backup snapshot.
