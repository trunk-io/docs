---
description: Use webhooks to automate custom flaky test workflows
---

# Webhooks

Trunk provides webhooks for you to build custom integrations to automate workflows, like notifying your team when a test becomes flaky or automatically creating tickets to investigate flaky tests. Trunk provides built-in connectors for [Linear](linear-integration.md) and [Jira](jira-integration.md) to automate ticket creation, and webhooks lets you build custom integrations for use cases that are not supported out of the box.

[Svix](https://docs.svix.com/) powers webhooks for Trunk. You'll be using Svix to configure webhooks and you should familiarize yourself with the [Svix App Portal docs](https://docs.svix.com/app-portal) to learn more.

### Supported Events

Trunk lets you create custom workflows with **event-triggered webhooks**. Flaky Tests events are named with a `test_case` prefix. You can find all the events that Trunk supports in the event catalog:

{% embed url="https://www.svix.com/event-types/us/org_2eQPL41Ew5XSHxiXZIamIUIXg8H/#test_case.status_changed" %}

Trunk publishes three Flaky Tests event types to Svix. Each event includes a full JSON schema with field descriptions visible in the Svix app portal.

#### `test_case.monitor_status_changed`

Emitted when a monitor activates or resolves for a test case.

| Field | Type | Description |
|---|---|---|
| `type` | string | Always `test_case.monitor_status_changed` |
| `timestamp` | string (ISO 8601) | When the event occurred |
| `monitor.id` | string (UUID) | Unique identifier for the monitor |
| `monitor.type` | string | The type of monitor (e.g. `pass_on_retry`) |
| `monitor.status` | string | Current monitor status (`active` or `resolved`) |
| `evidence` | object | Data supporting the status change; structure varies by monitor type |
| `repository.id` | string (UUID) | Unique identifier for the repository |
| `repository.html_url` | string | URL of the repository |
| `test_case.id` | string (UUID) | Stable unique identifier for the test |
| `test_case.name` | string | Name of the test |
| `test_case.classname` | string | Test classname |
| `test_case.file_path` | string | File path of the test |
| `test_case.html_url` | string | URL to the test detail page in Trunk |
| `test_case.codeowners` | string[] | Code owners associated with the test |
| `test_case.quarantined` | boolean | Whether the test is quarantined |
| `test_case.variant` | string | Test variant name |

#### `v2.test_case.status_changed`

Emitted when a test case changes status (e.g. becomes flaky or is resolved), triggered by a monitor.

| Field | Type | Description |
|---|---|---|
| `type` | string | Always `v2.test_case.status_changed` |
| `timestamp` | string (ISO 8601) | When the event occurred |
| `previous_status` | string | The prior status of the test case |
| `new_status` | string | The updated status of the test case |
| `triggered_by.monitor_id` | string | Unique identifier of the triggering monitor |
| `triggered_by.monitor_type` | string | Type of monitor that triggered the change |
| `triggered_by.monitor_status` | string | Status of the monitor at the time of the trigger |
| `repository` | object | See `repository` fields above |
| `test_case` | object | See `test_case` fields above |

#### `test_case.investigation_completed`

Emitted when an AI-powered flaky test analysis finishes for a test case.

| Field | Type | Description |
|---|---|---|
| `type` | string | Always `test_case.investigation_completed` |
| `investigation_id` | string (UUID) | Unique identifier for the investigation |
| `confidence` | number | Overall confidence score (0-1) for the findings |
| `created_at` | string (ISO 8601) | When the investigation completed |
| `markdown_summary` | string | Markdown-formatted summary of findings and recommendations |
| `failure_message` | string | The original failure message that triggered the investigation |
| `facts` | array | Facts discovered during the investigation |
| `facts[].fact_type` | string | Category of the fact (e.g. `GIT_BLAME`) |
| `facts[].content` | string | Detailed description with citations to supporting evidence |
| `facts[].confidence` | number | Confidence score (0-1) for this individual fact |
| `repository` | object | See `repository` fields above |
| `test_case` | object | See `test_case` fields above |

You can also find guides for specific examples here:

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Send a Slack Message</td><td></td><td></td><td></td><td><a href="slack-integration.md">slack-integration.md</a></td></tr><tr><td>Create a GitHub Issue</td><td></td><td></td><td></td><td><a href="github-issues-integration.md">github-issues-integration.md</a></td></tr><tr><td>Send a Microsoft Teams Message</td><td></td><td></td><td></td><td><a href="microsoft-teams-integration.md">microsoft-teams-integration.md</a></td></tr><tr><td>Create a Linear Issue</td><td></td><td></td><td></td><td><a href="linear-integration.md">linear-integration.md</a></td></tr><tr><td>Create a Jira Issue</td><td></td><td></td><td></td><td><a href="jira-integration.md">jira-integration.md</a></td></tr></tbody></table>
