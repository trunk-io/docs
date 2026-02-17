---
description: Public Trunk Merge Queue API. All requests should be authenticated.
---

# API reference

The Trunk Merge Queue API provides programmatic access to manage your merge queues and the pull requests within them. Use these endpoints to submit and cancel PRs, configure queue settings, and build custom automation on top of Trunk Merge Queue.

The API is an HTTP REST API. All endpoints accept and return JSON, use standard HTTP response codes, and are hosted at `https://api.trunk.io/v1`.

All requests must be [authenticated](../../setup-and-administration/apis/#authentication) by providing the `x-api-token` header.

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

***

## Pull request endpoints

Use these endpoints to submit PRs to the queue, cancel them, check their status, restart tests, and provide impacted target information for parallel mode.

{% openapi-operation spec="trunk-api" path="/submitPullRequest" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/cancelPullRequest" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/getSubmittedPullRequest" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/restartTestsOnPullRequest" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/setImpactedTargets" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

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
    "targetBranch": "main",
    "prNumber": 1234
  }'
```

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
    "targetBranch": "main",
    "prNumber": 1234
  }'
```

</details>

***

## Queue management endpoints

Use these endpoints to create, configure, inspect, and delete merge queues programmatically. This is useful for automating queue management across multiple repositories, scripting queue configuration as part of infrastructure-as-code workflows, or building custom tooling on top of Trunk Merge Queue.

{% hint style="info" %}
Queue management endpoints perform the same operations available in the Trunk web app under **Settings > Repositories > Merge Queue**. See [Settings and configurations](../administration/advanced-settings.md) for details on each setting.
{% endhint %}

{% openapi-operation spec="trunk-api" path="/createQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/getQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/updateQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

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

{% hint style="warning" %}
The queue must be empty before it can be deleted. Any queued merge requests will not be merged and all data will be lost.
{% endhint %}

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
