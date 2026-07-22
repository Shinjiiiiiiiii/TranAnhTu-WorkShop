---
title: "Asynchronous Post-Match Processing with DynamoDB Streams"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

### Overview
In this chapter, you will enable **DynamoDB Streams** on the `ActiveMatches` table, create the **MatchAnalyticLambda** function, and capture post-match events asynchronously to log analytics without affecting matchmaking latency.

---

### Sub-modules
- [5.6.1 Enable DynamoDB Streams & IAM Roles](5.6.1-enable-dynamodb-streams/)
- [5.6.2 Create MatchAnalytic Lambda & Verify Logs](5.6.2-create-analytics-lambda/)
