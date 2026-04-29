---
description: >-
  Browse, filter, and analyze your CI test upload history using charts and
  an interactive table.
---

# Uploads

The Uploads page gives you a historical view of every test run uploaded to Trunk Flaky Tests. It lets you quickly spot upload problems, filter down to specific branches or pull requests, and understand pass/fail trends over time.

## Overview

<figure><picture><source srcset="../.gitbook/assets/uploads-page-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/uploads-page-light.png" alt="Uploads page showing a stacked bar chart and filtered results table"></picture><figcaption><p>The Uploads page with chart, filter bar, and results table.</p></figcaption></figure>

The page has three main sections:

- **Stacked bar chart** — Shows Pass, Fail, and Other upload bins by day. Click a bar or drag across a range to filter the table to that date window.
- **Filter bar** — Narrow results by upload status, job conclusion, PR number, commit SHA, branch, or author. Multiple values can be entered for each filter.
- **Results table** — Paginated list of uploads with customizable columns. All filter, column, and chart range state is saved in the URL so you can share or bookmark a specific view.

## Filtering Uploads

The filter bar runs across the top of the results table. Each filter accepts multiple values.

| Filter | What it matches |
|---|---|
| **Status** | Upload processing status (e.g., Done, Processing, Failed) |
| **Conclusion** | Job-level conclusion from CI (e.g., success, failure, cancelled) |
| **PR number** | The pull request number associated with the upload |
| **SHA** | The commit SHA of the uploaded run |
| **Branch** | The branch name the upload was made from |
| **Author** | The committer who triggered the upload |

To apply filters, select a filter chip, type one or more values, and click **Apply**. To reset all active filters and any chart range selection, click **Clear all filters**.

### Filtering by date range

Click any bar in the chart to filter the table to that single day. Click and drag across multiple bars to select a date range. The table updates immediately to show only uploads that fall within that window. Click the chart again outside a selection to clear the range.

## Results Table

The table shows individual upload records. The visible columns can be customized using the column customizer (the gear icon at the top right of the table). Your column preferences are saved in the URL along with your other filter state.

A refresh button in the table header shows a badge count of new uploads that arrived since you last loaded the page. Click it to pull in the latest records without losing your current filter state.

## Reading Upload Statuses

| Status | Meaning |
|---|---|
| **Done** | Upload processed and test results are available |
| **Processing** | Upload is queued or actively being processed |
| **Done (empty)** | Upload completed but contained no test cases or test files |
| **Failed** | Upload could not be processed |

Uploads marked **Done (empty)** are stored as complete uploads with zero tests and zero files. They count toward upload history but do not contribute to flaky test detection.

## Next Steps

- [Trunk Analytics CLI](uploader.md) — Learn how to configure your CI jobs to send uploads.
- [Dashboard](dashboard.md) — View aggregate flaky test health for your repo.
- [Managing detected flaky tests](managing-detected-flaky-tests.md) — Act on tests flagged by Trunk.
