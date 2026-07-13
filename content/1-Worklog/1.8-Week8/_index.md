---
title: "Week 8 Worklog"
date: 2026-06-22
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---
### Week 8 Objectives:
* Learn Docker containerization concepts.
* Practice creating Dockerfiles, building Docker Images, and running Docker Containers locally.
* Understand Amazon Elastic Container Registry (ECR) for hosting private container images.
* Learn about Amazon Elastic Container Service (ECS) and serverless container hosting via AWS Fargate.
* Deploy a containerized web application on Amazon ECS using AWS Fargate.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | ------------------------------------------------------------------------------------------------------- |
| Mon | - Study Containerization theory vs Virtualization; install Docker Desktop | 06/22/2026 | 06/22/2026 | [Docker Get Started Guide](https://docs.docker.com/get-started/) |
| Tue | - Learn Dockerfile instructions (FROM, RUN, COPY, EXPOSE, CMD) <br> - **Practice:** Package a simple web application into a Docker Image | 06/23/2026 | 06/23/2026 | [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/) |
| Wed | - Study Amazon ECR (Elastic Container Registry) repositories <br> - **Practice:** Authenticate, tag, and push the local Docker image to ECR | 06/24/2026 | 06/24/2026 | [Amazon ECR Overview](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) |
| Thu | - Learn ECS (Elastic Container Service) core components: clusters, task definitions, services, and EC2 vs Fargate launch types | 06/25/2026 | 06/25/2026 | [Amazon ECS Architecture](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) |
| Fri | - **Practice:** Create an ECS cluster, write a Task Definition pointing to ECR image, and deploy a Service using AWS Fargate | 06/26/2026 | 06/26/2026 | [Deploy Container on ECS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html) |

### Week 8 Achievements:
* Acquired Docker development skills, including image layering, container caching, and port mapping.
* Containerized a Node.js/Python web application by writing a custom multi-stage Dockerfile.
* Created an Amazon ECR repository and successfully pushed container images using the AWS CLI.
* Mastered ECS cluster setup and configured ECS Task Definitions with specific CPU and Memory resource limits.
* Successfully launched a serverless containerized service via AWS Fargate and validated web application access through its public IP.
