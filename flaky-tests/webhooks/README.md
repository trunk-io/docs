---
description: Use webhooks to automate custom flaky test workflows
---

# Webhooks

Trunk provides webhooks for you to build custom integrations to automate workflows, like notifying your team when a test becomes flaky or automatically creating tickets to investigate flaky tests. Trunk provides built-in connectors for [Linear](linear-integration.md) and [Jira](jira-integration.md) to automate ticket creation, and webhooks lets you build custom integrations for use cases that are not supported out of the box.

[Svix](https://docs.svix.com/) powers webhooks for Trunk. You'll be using Svix to configure webhooks and you should familiarize yourself with the [Svix App Portal docs](https://docs.svix.com/app-portal) to learn more.

### Supported Events

Trunk lets you create custom workflows with **event-triggered webhooks**. Flaky Tests events are named with a `test_case` prefix. You can find all the events that Trunk supports in the event catalog:

{% embed url="https://www.svix.com/event-types/us/org_2eQPL41Ew5XSHxiXZIamIUIXg8H/#test_case.status_changed" %}

#### test\_case.status\_changed

Fired when a test case transitions between statuses (e.g., from healthy to flaky). This is the primary event for routing new flaky test notifications to your team.

#### test\_case.investigation\_completed

Fired when Trunk's AI finishes investigating a flaky test. The payload includes a markdown summary, an overall confidence score, and a list of facts that explain why the test is failing.

**Payload schema:**

```json
{
  "type": "test_case.investigation_completed",
  "investigation_id": "<uuid>",
  "confidence": 0.87,
  "created_at": "2026-04-06T12:00:00.000Z",
  "markdown_summary": "## Summary\nThe test fails intermittently due to a race condition in ...",
  "failure_message": "AssertionError: expected 200 but got 503",
  "repository": {
    "id": "<repo-id>",
    "name": "my-repo",
    "url": "https://github.com/my-org/my-repo"
  },
  "test_case": {
    "id": "<test-case-id>",
    "name": "should handle concurrent requests",
    "class_name": "ConcurrencyTest",
    "parent": "ConcurrencyTestSuite",
    "url": "https://app.trunk.io/my-org/my-repo/flaky-tests/<test-case-id>",
    "codeowners": ["@my-org/backend"]
  },
  "facts": [
    {
      "fact_type": "CI_LOGS",
      "content": "The error appears in CI logs when two requests arrive within 10ms of each other. [Log link](https://...)",
      "confidence": 0.92
    }
  ]
}
```

| Field | Type | Description |
| --- | --- | --- |
| `investigation_id` | string | Unique ID for this investigation run |
| `confidence` | number | Overall confidence score (0–1) that the root cause was identified |
| `markdown_summary` | string | Human-readable summary with citations rendered as markdown links |
| `failure_message` | string | The raw failure message from the most recent flaky run |
| `repository` | object | Repository where the flaky test lives |
| `test_case` | object | Test case that was investigated |
| `facts` | array | List of evidence items supporting the root cause |
| `facts[].fact_type` | string | Category of evidence (e.g., `CI_LOGS`, `CODE_HISTORY`) |
| `facts[].content` | string | Markdown-formatted explanation with linked citations |
| `facts[].confidence` | number | Confidence score for this individual fact (0–1) |

{% hint style="info" %}
The `test_case.investigation_completed` event is emitted only for organizations with AI investigation enabled. Contact your account team to enable this feature.
{% endhint %}

You can also find guides for specific examples here:

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Send a Slack Message</td><td></td><td></td><td></td><td><a href="slack-integration.md">slack-integration.md</a></td></tr><tr><td>Create a GitHub Issue</td><td></td><td></td><td></td><td><a href="github-issues-integration.md">github-issues-integration.md</a></td></tr><tr><td>Send a Microsoft Teams Message</td><td></td><td></td><td></td><td><a href="microsoft-teams-integration.md">microsoft-teams-integration.md</a></td></tr><tr><td>Create a Linear Issue</td><td></td><td></td><td></td><td><a href="linear-integration.md">linear-integration.md</a></td></tr><tr><td>Create a Jira Issue</td><td></td><td></td><td></td><td><a href="jira-integration.md">jira-integration.md</a></td></tr></tbody></table>
