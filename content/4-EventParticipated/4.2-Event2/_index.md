---
title: "Event 2"
date: 2025-06-27
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---
# Summary Report: AWS SageMaker Deep Dive

### Event Information:
* **Event Name:** AWS SageMaker Deep Dive (Highlighting features from re:Invent 2024)
* **Date:** June 27, 2025
* **Location:** Hybrid (In-person & Virtual) at 26th Floor (and 36th Floor), Bitexco Financial Tower, 02 Hai Trieu Street, Ben Nghe Ward, District 1, Ho Chi Minh City
* **Organizer:** AWS (Amazon Web Services), broadcasted on AWS Study Group YouTube channel

---

### Event Objectives:
* **Deep Dive into AI/ML Development:** Explore the new SageMaker Unified Studio and the latest machine learning capabilities within the AWS ecosystem.
* **Unified Development Experience:** Showcase a single, integrated environment that unifies data processing, SQL analytics, ML model development, generative AI application building, and data governance.
* **Break Down Silos:** Enable Data Engineers, Data Scientists, and Data Analysts to collaborate in a single shared digital workspace.

---

### Speakers:
* **Anh Trung** – Speaker 1
* **Kirara Lador** – Speaker 2
* **Isaac** – Speaker 3

---

### Key Highlights:

#### 1. Overcoming Legacy Data Silos
* In the past, data processing tools (EMR, Glue, Athena) and ML model management tools were separated, causing constant switching overhead.
* Data sharing within organizations was bottlenecked by manual administrative approvals.
* Technical raw schemas made datasets incomprehensible to business users.

#### 2. The Solution: SageMaker Unified Studio
* **Unified Studio:** A single pane of glass offering full access to code repositories, compute configurations, open-source AI models, and shared data catalogs.

#### 3. Technology & Tooling Showcase
* **Jupyter Lab IDE:** Multi-language notebooks supporting Python, Scala, and SQL cells running seamlessly side-by-side. Includes Visual ETL capabilities for drag-and-drop pipelines.
* **Integrated Amazon Q:** Serves as a coding assistant inside the IDE to generate SQL queries from natural language, explain code blocks, debug errors, and refactor scripts.
* **AI/ML Foundation Models:** Integration with Amazon Bedrock, SageMaker Jumpstart, and advanced LLMs such as Amazon Nova and Claude 4. Introduces SageMaker HyperPod for distributed, large-scale training.
* **Data Governance:** Built-in Data Catalog, Data Lineage tracking, and packaging datasets as "Data Products."

#### 4. Live Demos & Case Studies
* **Three-Role Collaboration Demo:** Kiara demonstrated a workflow acting as a Data Engineer setting security rules, a Data Scientist requesting access to train a loan default prediction model, and a Data Analyst searching for Marketing data. The entire requesting and approval workflow was frictionless and automated.
* **AI Business Metadata Generation:** Using generative AI to automatically generate business descriptions for hundreds of technical table columns.
* **Data Products Concept:** Packaging related tables into one "Data Product" so users request access to one item rather than hundreds of tables separately.

---

### Key Takeaways:

#### 1. Design Mindset & Data Collaboration
* Shift from fragmented workflows to active data collaboration. Data governance is not about locking data away, but making it easily discoverable while preserving security boundaries.
* **Change Management:** Utilizing Data Lineage to identify downstream "Data consumers" before altering database columns to prevent breaking other departments' dashboards.

#### 2. Technical Learnings
* Understood Data Lineage tracking to trace data ancestry from raw ingestion to final tables.
* Explored running Apache Airflow workflows (MWAA) directly inside the Unified Studio interface.
* **Security & Best Practices:** Implementing Column-level security to mask PII (such as employer names in credit datasets) before provisioning access to Data Scientists.
* **Refactoring:** Leveraging Amazon Q to refactor notebook cells into structured, clean code.

---

### Applying to Work:
* **Self-Service Permissions:** Implement UI-based permission request flows instead of manual GRANT SQL queries to eliminate database administrator bottlenecks.
* **Dev Workflow Automation:** Experiment with Amazon Q to generate Visual ETL pipelines from prompts, and use SageMaker Jumpstart to deploy open-source models with minimal code.
* **Data Standardization:** Transition away from manual CSV file transfers in S3 between Data Engineers and Data Scientists; introduce a standardized Business Glossary.

---

### Event Experience:
* **Practical Value:** Highly valuable lecture flow detailing data processing, IDE tools, AI integration, and live demos by Kiara and Isaac.
* **Hands-on Workshop:** Attendees participated in workshop lab sessions to interact with datasets directly.
* **Networking & Mentorship:** Speakers were highly accessible to discuss advanced architectures like SageMaker HyperPod setup after sessions.
* **Memorable Highlight:** The integration of the Spark debugging UI directly into the IDE without needing complex networking setups.

---

### Key Lessons & Next Steps:
* **SageMaker Evolution:** Amazon SageMaker has evolved from a machine learning service into a complete Machine Learning and Analytics platform covering the full lifecycle from raw data ingestion to GenAI application deployment.
* **Next Steps:** Deep dive into Data Lakehouse concepts, experiment with fast/lightweight Amazon Nova models, and integrate MLflow to track and log model training runs.

---

### Event Photos:
![AWS SageMaker Deep Dive Intro Ho Chi Minh City](/images/4-EventParticipated/event2-1.png)

![AWS SageMaker Deep Dive Live Demo Lineage](/images/4-EventParticipated/event2-2.png)

![AWS SageMaker AI Notebook Development](/images/4-EventParticipated/event2-3.png)
