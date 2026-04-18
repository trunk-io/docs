---
description: Receive AI investigation results via webhook when Trunk completes a flaky test analysis
---

# AI Investigation Completed Event

When Trunk's AI finishes investigating a flaky test, it fires a `test_case.investigation_completed` webhook event. Your endpoint receives the investigation findings, a confidence score, and a rendered markdown summary you can post to Slack, create tickets from, or feed into your own tooling.

## Event type

`test_case.investigation_completed`

## Payload

```json
{
  "type": "test_case.investigation_completed",
  "investigation_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "confidence": 0.87,
  "created_at": "2026-04-17T23:26:45.000Z",
  "failure_message": "TypeError: Cannot read properties of undefined (reading 'map')",
  "markdown_summary": "The test fails because `userData` is `undefined` when the API returns a 401. See [CI run #4821](https://ci.example.com/runs/4821) and [commit abc1234](https://github.com/your-org/your-repo/commit/abc1234def5678) for context.",
  "repository": {
    "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "html_url": "https://github.com/your-org/your-repo"
  },
  "test_case": {
    "id": "c9d0e1f2-a3b4-5678-cdef-012345678901",
    "name": "should handle authenticated users",
    "classname": "UserService",
    "codeowners": ["@your-org/backend"],
    "file_path": "src/services/user.test.ts",
    "html_url": "https://app.trunk.io/your-org/flaky-tests/test/c9d0e1f2-a3b4-5678-cdef-012345678901",
    "parent": "UserServiceTests",
    "quarantined": false,
    "variant": ""
  },
  "facts": [
    {
      "fact_type": "CI_LOGS",
      "content": "The test failed in [CI run #4821](https://ci.example.com/runs/4821) with a TypeError at line 42.",
      "confidence": 0.91,
      "impact": 0.85
    }
  ]
}
```

## Fields

### Top-level

| Field | Type | Description |
|---|---|---|
| `type` | string | Always `test_case.investigation_completed`. |
| `investigation_id` | string (UUID) | Unique identifier for this investigation. |
| `confidence` | number | Overall confidence score from 0 to 1. Higher values indicate stronger evidence for the findings. |
| `created_at` | string | ISO 8601 timestamp when the investigation completed. |
| `failure_message` | string | The original failure message or error that triggered the investigation. |
| `markdown_summary` | string | Markdown-formatted summary of findings with rendered citation links. See [Markdown summary](#markdown-summary) below. |
| `repository` | object | The repository the test belongs to. |
| `test_case` | object | The flaky test that was investigated. |
| `facts` | array | Individual findings discovered during the investigation. |

### `repository`

| Field | Type | Description |
|---|---|---|
| `id` | string (UUID) | Unique identifier for the repository in Trunk. |
| `html_url` | string | URL of the repository on GitHub. |

### `test_case`

| Field | Type | Description |
|---|---|---|
| `id` | string (UUID) | Stable unique identifier for the test case. |
| `name` | string | Name of the test. |
| `classname` | string | Classname of the test. |
| `codeowners` | string[] | GitHub CODEOWNERS entries associated with the test file. |
| `file_path` | string | Path to the test file in the repository. |
| `html_url` | string | URL to the test detail page in the Trunk app. |
| `parent` | string | Parent test suite or file. |
| `quarantined` | boolean | Whether the test is currently quarantined. |
| `variant` | string | Test variant name, or empty string if none. |

### `facts[]`

| Field | Type | Description |
|---|---|---|
| `fact_type` | string | Category of evidence (e.g., `CI_LOGS`, `COMMIT`, `TEST_RUN`). |
| `content` | string | Markdown content for this finding with rendered citation links. |
| `confidence` | number | Confidence score (0-1) that this fact is correct. |
| `impact` | number | Impact score (0-1) indicating how relevant this fact is to the failure. |

## Markdown summary

The `markdown_summary` field contains a human-readable summary of the investigation findings. Citation references in the summary are resolved to real URLs before delivery, so links to CI runs, commits, and test history pages are ready to use directly.

For example, a citation to a CI run becomes a standard Markdown link:

```
[CI run #4821](https://ci.example.com/runs/4821)
```

Individual `facts[].content` fields follow the same pattern.

## Example: post findings to Slack

```javascript
app.post('/webhook', async (req, res) => {
  const { type, confidence, markdown_summary, test_case } = req.body;
  if (type !== 'test_case.investigation_completed') return res.sendStatus(200);

  await slack.chat.postMessage({
    channel: '#flaky-tests',
    text: `*AI investigation complete* for \`${test_case.name}\` (confidence: ${Math.round(confidence * 100)}%)\n\n${markdown_summary}`,
  });

  res.sendStatus(200);
});
```

## Enabling the webhook

Configure AI Investigation webhooks in the [Trunk app](https://app.trunk.io) under **Settings > Webhooks**. Select `test_case.investigation_completed` from the event catalog.

For general webhook setup, see [Webhooks](README.md).

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
