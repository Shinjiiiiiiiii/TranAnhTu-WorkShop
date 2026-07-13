---
title: "Week 4 Worklog"
date: 2026-05-25
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---
### Week 4 Objectives:
* Learn about Amazon Virtual Private Cloud (VPC) and AWS networking.
* Understand networking components: Subnets, Route Tables, Internet Gateways (IGW), and NAT Gateways.
* Compare Security Groups (Stateful) vs Network Access Control Lists (NACL - Stateless) security layers.
* Design a hybrid network architecture featuring both Public and Private subnets.
* Practice building a complete VPC environment from scratch.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | ------------------------------------------------------------------------------------------------------- |
| Mon | - Study VPC core concepts: CIDR block allocation, IP range design, and Subnetting | 05/25/2026 | 05/25/2026 | [Amazon VPC Core Concepts](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| Tue | - Learn about Route Tables, Internet Gateways (IGW), and how traffic flows from public resources | 05/26/2026 | 05/26/2026 | [VPC Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) |
| Wed | - Study NAT Gateways and how private subnets connect securely to the Internet | 05/27/2026 | 05/27/2026 | [Amazon VPC NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) |
| Thu | - Compare and configure Security Groups vs Network ACLs (NACL) security rules | 05/28/2026 | 05/28/2026 | [VPC Security Layer Comparison](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html) |
| Fri | - **Practice:** Construct a custom VPC with Public Subnets, Private Subnets, IGW, Route Tables, and launch EC2s inside | 05/29/2026 | 05/29/2026 | [Build a Custom VPC Guide](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html) |

### Week 4 Achievements:
* Gained a solid foundation in cloud networking, CIDR design, and subnet planning.
* Designed and built a custom VPC with isolated public (web) and private (database) zones.
* Configured Internet Gateways and Route Tables to enable external connectivity for public servers.
* Deployed a NAT Gateway in the public subnet to allow servers in private subnets to download system updates securely without internet exposure.
* Implemented double-layered security combining Security Groups (instance-level) and NACLs (subnet-level).
