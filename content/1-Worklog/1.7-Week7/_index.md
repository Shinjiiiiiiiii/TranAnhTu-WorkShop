---
title: "Week 7 Worklog"
date: 2026-06-15
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---
### Week 7 Objectives:
* Learn about Infrastructure as Code (IaC) benefits and tools.
* Understand HashiCorp Terraform syntax, State management, Providers, Resources, Variables, and Modules.
* Study AWS CloudFormation as a native IaC alternative.
* Practice writing Terraform configuration files to automate the creation of network (VPC), compute (EC2), and storage (S3) resources.
* Learn how to manage infrastructure lifecycle using IaC.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | ------------------------------------------------------------------------------------------------------- |
| Mon | - Learn IaC benefits and Terraform syntax (HCL - HashiCorp Configuration Language) | 06/15/2026 | 06/15/2026 | [Terraform Introduction](https://developer.hashicorp.com/terraform/intro) |
| Tue | - Study Terraform workflow: `init`, `plan`, `apply`, and `destroy` commands; learn State file significance | 06/16/2026 | 06/16/2026 | [Terraform CLI Commands](https://developer.hashicorp.com/terraform/cli/commands) |
| Wed | - Study AWS CloudFormation: templates, JSON/YAML structure, Stacks, and nested templates | 06/17/2026 | 06/17/2026 | [AWS CloudFormation Overview](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) |
| Thu | - **Practice:** Write Terraform code to deploy a custom VPC with public subnets and an Internet Gateway | 06/18/2026 | 06/18/2026 | [AWS Provider for Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) |
| Fri | - **Practice:** Extend Terraform files to provision an EC2 instance and an S3 bucket; deploy and verify resources | 06/19/2026 | 06/19/2026 | [Terraform AWS Tutorials](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) |

### Week 7 Achievements:
* Gained a solid grasp of Declarative Infrastructure management vs imperative scripting.
* Installed Terraform CLI on local workstation and configured the AWS provider credentials.
* Mastered writing declarative `.tf` configuration files including variables, outputs, and local state handling.
* Successfully initialized, planned, and applied a configuration to provision a VPC, Route Tables, an EC2 Web Server, and an S3 bucket in one click.
* Learned how to update and clean up cloud resources dynamically using `terraform apply` and `terraform destroy`.
