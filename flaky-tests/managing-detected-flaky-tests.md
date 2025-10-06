---
description: >-
  A step-by-step guide for building an automated process to manage detected
  flaky tests.
---

# Managing Detected Flaky Tests

It is important to have a follow-up process in place to manage detected flaky tests. A good process ensures that flaky tests do not slow down CI for your development team and prevents flakes from accumulating over time.&#x20;

This guide walks through Trunk's recommended best practices for building a process around detected flaky tests in your organization.

{% hint style="info" %}
Flaky tests will be [automatically detected](detection.md) by Trunk after you:

* [Set up your test framework](get-started/frameworks/) to produce test reports
* [Integrated with your CI provider](get-started/ci-providers/) to upload those reports on CI runs.

Go through these guides first to start detecting flaky tests.
{% endhint %}

### Step 1: Create tickets for Flaky Tests

Creating Linear or Jira tickets for detected flaky tests helps to integrate flaky test fixes into your existing workflows.

* Start by [connecting to Linear or Jira](ticketing-integrations/). You can also set default labels or teams for flaky test tickets.
* Once connected, you can click **Create Ticket** on a test detail page in Trunk. Trunk will create the ticket with context, including the test ID, flake rate, and the last failure stack trace and reason.
* The ticket status and assignee will be visible on the test details page in Trunk, and these details will stay in sync with changes to the ticket.

### Step 2: Broadcast Flakes

It is important to keep the team informed on all status changes for flaky tests . This allows for fast follow-up when a test is marked as flaky.

* Use the [built-in Slack or Microsoft Teams webhook integrations](webhooks/) to transform webhook payloads into messages.
* Trunk's built-in templates help you get started and test the connection.
* You can then customize the transformation to update the message format and content, including @-mentioning test owners so they can follow up right away.

### Step 3: Start Quarantining Manually

Flaky tests slow down CI and have a high negative impact on merge queue throughput. You can minimize or eliminate this CI slowdown by [quarantining](quarantining.md) flaky tests at runtime.

* Enable quarantining for your repo at **Settings > your repo > Enable Test Quarantining**.
* Manually quarantine flaky tests by going to the test details page, clicking **Quarantine**, and setting the status to **Always**. Leave a comment detailing why you are quarantining this test to keep your team informed. The comment and quarantine status change will appear in the timeline on the test details page.

After quarantining a test, Trunk will ignore the test result (pass/fail) on CI runs, preventing this flaky test from failing CI.

### Step 4: Automation

Trunk has [webhooks](webhooks/) and [Flaky Tests APIs](webhooks/flaky-tests.md) that can be used to build custom workflows around ticket creation, linking existing tickets to Trunk, sending notifications, and dealing with quarantined tests.

There is also built-in automation support that handles tasks such as assigning flaky test ownership, ticket creation, and quarantining (so that unblocking CI is not a manual process).&#x20;

* [`CODEOWNERS` files](dashboard.md#code-owners) can automatically assign ownership of test flakes.
* Tickets can be [auto-created using webhooks](webhooks/) as triggers, similar to Slack or MS Teams notifications.
* Automatically quarantine flaky tests by enabling **Settings > your repo > Auto-Quarantine Flaky Tests**.

You can customize how flaky and quarantined tests are handled to suit your team and organization best.

### Step 5: Review Existing Flakes

It is important to track and triage existing flaky tests over time. Trunk collects historical failure logs and stack traces for flaky tests, providing developers as much information as possible for debugging high-impact flaky tests.

* Review all new flaky tests to determine their impact and the urgency of a fix.
* Review existing quarantined tests regularly to decide which tests should be fixed and which tests should be deleted from your test suite.
* Trunk can send weekly email reports with information such as your total number of flaky tests and the number of PRs blocked, and how those numbers have changed week over week. Frequently failing tests will also be highlighted in the report. Reach out on [Slack](https://slack.trunk.io/) to ask about enabling weekly reports for your organization.

## In Summary: Build a Process Around Managing Flaky Tests

Building processes for dealing with flaky tests helps decrease or eliminate their impact on CI and reduce the amount of developer time lost to debugging flakes and CI reruns.

Trunk allows you to customize this process to fit into your existing tooling and workflows, and automates manual tasks such as notifications and ticket creation.

Reach out to us on our [community Slack](https://slack.trunk.io/) to chat about how to structure a process for managing flaky tests across your team or organization.
