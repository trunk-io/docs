---
description: Use webhooks to automate custom flaky test workflows
---

# Webhooks

Trunk provides webhooks for you to build custom integrations to automate workflows, like notifying your team when a test becomes flaky or automatically creating tickets to investigate flaky tests. Trunk already provides a Jira integration, and more are planned. Webhooks lets you build custom integrations for use cases that are not supported out of the box.

[Svix](https://docs.svix.com/) powers webhooks for Trunk. You'll be using Svix to configure webhooks and you should familiarize yourself with the [Svix App Portal docs](https://docs.svix.com/app-portal) to learn more.

### Supported Events

Trunk lets you create custom workflows with **event-triggered webhooks**. Flaky Test events are named with a `test_case` prefix. You can find all the events that Trunk supports in the event catalog:

{% embed url="https://www.svix.com/event-types/us/org_2eQPL41Ew5XSHxiXZIamIUIXg8H/#test_case.status_changed" %}

You can also find guides for specific examples here:

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Send a Slack Message</td><td></td><td></td><td></td><td><a href="slack-integration.md">slack-integration.md</a></td></tr><tr><td>Create a GitHub Issue</td><td></td><td></td><td></td><td><a href="github-issues-integration.md">github-issues-integration.md</a></td></tr><tr><td>Send a Microsoft Teams Message</td><td></td><td></td><td></td><td><a href="microsoft-teams-integration.md">microsoft-teams-integration.md</a></td></tr><tr><td>Create a Linear Issue</td><td></td><td></td><td></td><td><a href="linear-integration.md">linear-integration.md</a></td></tr></tbody></table>
