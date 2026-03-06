---
description: Public Trunk Merge Queue API. All requests should be authenticated.
---

# API reference

The Trunk Merge Queue API provides programmatic access to manage your merge queues and the pull requests within them. Use these endpoints to submit and cancel PRs, configure queue settings, and build custom automation on top of Trunk Merge Queue.

The API is an HTTP REST API. All endpoints accept and return JSON, use standard HTTP response codes, and are hosted at `https://api.trunk.io/v1`.

All requests must be [authenticated](../../setup-and-administration/apis/#authentication) by providing the `x-api-token` header. You can also manage your queue using the [CLI](merge-queue-cli-reference.md) or the [Trunk App](https://app.trunk.io).

## Common request fields

Most endpoints require a `repo` object and a `targetBranch` to identify which merge queue to operate on:

```json
{
  "repo": {
    "host": "github.com",
    "owner": "your-org",
    "name": "your-repo"
  },
  "targetBranch": "main"
}
```

## Endpoint summary

### Pull request endpoints

| Endpoint | Description |
| --- | --- |
| [POST /submitPullRequest](#submit-a-pull-request) | Submit a PR to the merge queue |
| [POST /cancelPullRequest](#cancel-a-pull-request) | Cancel a PR in the merge queue |
| [POST /getSubmittedPullRequest](#get-a-submitted-pull-request) | Get the status of a submitted PR |
| [POST /restartTestsOnPullRequest](#restart-tests-on-a-pull-request) | Restart tests on a PR in the queue |
| [POST /setImpactedTargets](#set-impacted-targets) | Set impacted targets for parallel queues |
| [POST /getMergeQueueTestingDetails](#get-merge-queue-testing-details) | Get testing run details and check statuses |

### Queue management endpoints

| Endpoint | Description |
| --- | --- |
| [POST /getQueue](#get-the-queue) | Get queue configuration and enqueued PRs |
| [POST /createQueue](#create-a-queue) | Create a new merge queue |
| [POST /updateQueue](#update-the-queue) | Update queue settings (pause, resume, configure) |
| [POST /deleteQueue](#delete-a-queue) | Delete an empty merge queue |

## Common use cases

**CI/CD automation** — Use `/submitPullRequest` and `/cancelPullRequest` to integrate merge queue operations into your CI pipelines or custom merge bots.

**Monitoring dashboards** — Use `/getQueue` and `/getSubmittedPullRequest` to build real-time visibility into queue health and individual PR status.

**Queue state management** — Use `/updateQueue` with the `state` field to pause, resume, or drain your queue during incidents, deployments, or maintenance windows. Supported states: `RUNNING`, `PAUSED`, `DRAINING`. See [queue states](../administration/advanced-settings.md) for details.

**Parallel queue configuration** — Use `/setImpactedTargets` to define which targets a PR affects so the queue can test non-overlapping changes simultaneously. See [parallel queues](../optimizations/parallel-queues/) for setup details.

**Test monitoring** — Use `/getMergeQueueTestingDetails` to inspect which checks are running, their current status, and which PRs are being tested together in a batch.

## Authentication

All requests require an API token passed in the `x-api-token` header. Find your token in the [Trunk App](https://app.trunk.io). See the [authentication guide](../../setup-and-administration/apis/#authentication) for full details.

{% hint style="info" %}
**Forked pull requests:** Workflows from forked PRs may not have access to your organization's API token. In this case, pass the GitHub Actions run ID as the `x-forked-workflow-run-id` header instead of `x-api-token`. Trunk verifies the run ID belongs to a currently running workflow from a forked PR. See the [parallel queues API guide](../optimizations/parallel-queues/api.md) for details.
{% endhint %}

***

## Pull request endpoints

Use these endpoints to submit PRs to the queue, cancel them, check their status, restart tests, and provide impacted target information for parallel mode.

### Submit a pull request

{% openapi-operation spec="trunk-api" path="/submitPullRequest" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

### Cancel a pull request

{% openapi-operation spec="trunk-api" path="/cancelPullRequest" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

### Get a submitted pull request

Use this endpoint to check whether a PR is currently in the queue, its testing state, readiness status, and priority.

{% openapi-operation spec="trunk-api" path="/getSubmittedPullRequest" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

### Restart tests on a pull request

{% openapi-operation spec="trunk-api" path="/restartTestsOnPullRequest" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

### Set impacted targets

Used with [parallel queues](../optimizations/parallel-queues/) to specify which targets a PR impacts, enabling non-overlapping PRs to be tested simultaneously. See the [custom build systems guide](../optimizations/parallel-queues/api.md) for implementation details.

{% openapi-operation spec="trunk-api" path="/setImpactedTargets" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

### Get merge queue testing details

Returns detailed information about a specific test run, including required status checks, the test branch, check suite results, and which PRs are being tested together.

{% openapi-operation spec="trunk-api" path="/getMergeQueueTestingDetails" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

<details>

<summary>Example: Submit a PR to the queue</summary>

```bash
curl -X POST https://api.trunk.io/v1/submitPullRequest \
  -H "Content-Type: application/json" \
  -H "x-api-token: YOUR_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "your-org",
      "name": "your-repo"
    },
    "pr": {
      "number": 1234
    },
    "targetBranch": "main"
  }'
```

</details>

<details>

<summary>Example: Check PR status in the queue</summary>

```bash
curl -X POST https://api.trunk.io/v1/getSubmittedPullRequest \
  -H "Content-Type: application/json" \
  -H "x-api-token: YOUR_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "your-org",
      "name": "your-repo"
    },
    "pr": {
      "number": 1234
    },
    "targetBranch": "main"
  }'
```

The response includes the PR state (`NOT_READY`, `PENDING`, `TESTING`, `TESTS_PASSED`, `MERGED`, `FAILED`, `CANCELLED`, `PENDING_FAILURE`), readiness information, and priority details.

</details>

<details>

<summary>Example: Cancel a PR in the queue</summary>

```bash
curl -X POST https://api.trunk.io/v1/cancelPullRequest \
  -H "Content-Type: application/json" \
  -H "x-api-token: YOUR_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "your-org",
      "name": "your-repo"
    },
    "pr": {
      "number": 1234
    },
    "targetBranch": "main"
  }'
```

</details>

***

## Queue management endpoints

Use these endpoints to create, configure, inspect, and delete merge queues programmatically. This is useful for automating queue management across multiple repositories, scripting queue configuration as part of infrastructure-as-code workflows, or building custom tooling on top of Trunk Merge Queue.

{% hint style="info" %}
Queue management endpoints perform the same operations available in the Trunk web app under **Settings > Repositories > Merge Queue**. See [Settings and configurations](../administration/advanced-settings.md) for details on each setting.
{% endhint %}

### Get the queue

Returns the queue configuration and all currently enqueued pull requests with their states.

{% openapi-operation spec="trunk-api" path="/getQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

### Create a queue

{% openapi-operation spec="trunk-api" path="/createQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

### Update the queue

Use this endpoint to change queue configuration or manage queue state. To pause the queue, set `state` to `PAUSED`. To resume, set it to `RUNNING`. To drain (finish current PRs but accept no new ones), set it to `DRAINING`.

{% openapi-operation spec="trunk-api" path="/updateQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

### Delete a queue

{% hint style="warning" %}
The queue must be empty before it can be deleted. Any queued merge requests will not be merged and all data will be lost.
{% endhint %}

{% openapi-operation spec="trunk-api" path="/deleteQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

<details>

<summary>Example: Create a new queue</summary>

```bash
curl -X POST https://api.trunk.io/v1/createQueue \
  -H "Content-Type: application/json" \
  -H "x-api-token: YOUR_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "your-org",
      "name": "your-repo"
    },
    "targetBranch": "main",
    "mode": "single",
    "concurrency": 5
  }'
```

</details>

<details>

<summary>Example: Get current queue status and enqueued PRs</summary>

```bash
curl -X POST https://api.trunk.io/v1/getQueue \
  -H "Content-Type: application/json" \
  -H "x-api-token: YOUR_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "your-org",
      "name": "your-repo"
    },
    "targetBranch": "main"
  }'
```

The response includes the queue configuration and a list of all enqueued PRs with their current state:

```json
{
  "state": "RUNNING",
  "branch": "main",
  "concurrency": 5,
  "testingTimeoutMins": 300,
  "mode": "SINGLE",
  "canOptimisticallyMerge": false,
  "pendingFailureDepth": 0,
  "isBatching": false,
  "batchingMaxWaitTimeMins": 0,
  "batchingMinSize": 0,
  "createPrsForTestingBranches": true,
  "enqueuedPullRequests": [
    {
      "state": "TESTING",
      "stateChangedAt": "2025-01-15T10:30:00Z",
      "priorityValue": 100,
      "priorityName": "default",
      "skipTheLine": false,
      "prNumber": 1234,
      "prTitle": "Add user authentication",
      "prSha": "abc123",
      "prBaseBranch": "main",
      "prAuthor": "octocat"
    }
  ]
}
```

</details>

<details>

<summary>Example: Pause the queue (e.g., during a CI outage)</summary>

```bash
curl -X POST https://api.trunk.io/v1/updateQueue \
  -H "Content-Type: application/json" \
  -H "x-api-token: YOUR_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "your-org",
      "name": "your-repo"
    },
    "targetBranch": "main",
    "state": "PAUSED"
  }'
```

</details>

<details>

<summary>Example: Update queue settings (concurrency, batching, timeouts)</summary>

```bash
curl -X POST https://api.trunk.io/v1/updateQueue \
  -H "Content-Type: application/json" \
  -H "x-api-token: YOUR_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "your-org",
      "name": "your-repo"
    },
    "targetBranch": "main",
    "concurrency": 10,
    "testingTimeoutMinutes": 120,
    "pendingFailureDepth": 2,
    "canOptimisticallyMerge": true,
    "batch": true,
    "batchingMinSize": 3,
    "batchingMaxWaitTimeMinutes": 15
  }'
```

</details>

<details>

<summary>Example: Delete a queue</summary>

```bash
curl -X POST https://api.trunk.io/v1/deleteQueue \
  -H "Content-Type: application/json" \
  -H "x-api-token: YOUR_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "your-org",
      "name": "your-repo"
    },
    "targetBranch": "main"
  }'
```

</details>

***

## Related resources

- [CLI reference](merge-queue-cli-reference.md) — Manage the queue from the command line
- [Parallel queues API](../optimizations/parallel-queues/api.md) — Impacted targets setup for custom build systems
- [Webhooks](../webhooks.md) — Subscribe to merge queue events
- [Queue settings](../administration/advanced-settings.md) — Configure queue behavior in the Trunk App
- [Authentication](../../setup-and-administration/apis/) — API token setup and management
