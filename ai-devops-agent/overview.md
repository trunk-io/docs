---
description: Schedule and automates repetitive, asynchronous DevOps tasks
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: false
---

# Overview

### Your AI DevOps Agent

Trunk's AI DevOps Agent connects to your codebase, CI provider, and existing tools like Slack and Linear to schedule and automate repetitive DevOps tasks.

It can answer questions about your CI pipeline and tests, send notifications on a schedule or when a webhook is fired, and help you take action on CI failures by providing detailed root cause analysis in your PRs.

{% hint style="success" %}
## The AI DevOps Agent is currently in beta

Sign up for the [waitlist](https://trunk.io/agent), and we'll reach out when we're ready to onboard you.
{% endhint %}

{% code title="How the agent works" %}
```
                                           ╔═ trunk ═══════════════════════════════════╗ 
╔════════════╗      ╔═══════════╗          ║                         ┏━━━━━━━━━━━━━━┓  ║░
║            ║░     ║           ║░         ║  ┏━━━━━━━━━━━━━━━━┓     ┃   GitHub     ┃  ║░
║   CI Jobs  ║░────▶║   Tests   ║░───API──▶║  ┃  AI Root Cause ┃────▶┃   Slack      ┃  ║░
║            ║░     ║           ║░         ║  ┃    Analysis    ┃     ┃   Linear     ┃  ║░
╚════════════╝░     ╚═══════════╝░         ║  ┗━━━━━━━━━━━━━━━━┛     ┃   MCP        ┃  ║░
 ░░░░░░░░░░░░░░      ░░░░░░░░░░░░░         ║                         ┃   Webhooks   ┃  ║░
      │                                    ║                         ┃   Dashboard  ┃  ║░
      └─────────────── API ───────────────▶║                         ┗━━━━━━━━━━━━━━┛  ║░
                                           ╚═══════════════════════════════════════════╝░
                                            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```
{% endcode %}

### Features

The AI DevOps Agent connects your codebase, CI data, and existing chat and ticketing tools to answer questions and automate tasks. Some sample use cases include:

#### Schedule async tasks

The agent can run repetitive async tasks using cron jobs and webhooks as triggers. Some examples of tasks you can schedule include:

* Create weekly reports and send them to the product team.
* Run daily checks and send a notification to developers if any issues are found.
* Review pull requests to ensure they follow specific contribution guidelines.

#### Debug CI failures and slowdowns

Instead of manually digging through CI logs and stack trace info, the agent can root cause CI and test failures and tell you exactly what is wrong and how to fix it.

#### Ask questions about your pipelines

Dig into CI trends and analytics without hunting through dashboards. Find out what CI job is slowing down the pipeline over the past two weeks, or how the current CI process could be parallelized to improve time to merge.

{% embed url="https://play.vidyard.com/tkbBdXyHJR98Ek9ZWg3aef.jpg" %}
Some of the capabilities of the AI DevOps Agent
{% endembed %}

{% hint style="success" %}
## The AI DevOps Agent is currently in beta

Sign up for the [waitlist](https://trunk.io/agent), and we'll reach out when we're ready to onboard you.
{% endhint %}
