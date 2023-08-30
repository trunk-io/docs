---
description: CI Analytics provides metrics about the CI pipelines running on Pull Requests
---

# Pull Request Metrics

## Overview

Trunk CI Analytics collects CI metrics about all CI pipelines that run on pull requests. This allows you to see how much CI time is spent on each pull request, which pull requests are improving or degrading CI performance, and how often pull requests are rerunning CI pipelines.

## Pull Request Comments

CI Analytics can post comments on pull requests to highlight interesting insights about how your CI system is performing, and how that pull request impacts your CI performance and reliability.

<figure><img src="../.gitbook/assets/Screenshot 2023-08-29 at 11.54.07 PM.png" alt=""><figcaption></figcaption></figure>

### Total CI Time

Total CI time shows the aggregate CI time for this pull request, across all updates of the pull request and retries of CI pipelines. The expandable table includes a breakdown of the total CI time and reliability per pipeline.

### Anomalous Pipelines

Pipelines that run significantly faster or slower than their baseline will be highlighted here. This highlights potential regressions caused by the pull request and also celebrates efforts that improve CI performance.

### Getting Started

{% @supademo/embed demoId="HBFQ1vFqJhg529jjWK1Ep" url="https://app.supademo.com/demo/HBFQ1vFqJhg529jjWK1Ep" %}
