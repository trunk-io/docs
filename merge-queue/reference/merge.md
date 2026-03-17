---
description: Public Trunk Merge Queue API. All requests should be authenticated.
---

# API reference

The Trunk Merge Queue API lets you manage pull requests, configure queues, and monitor queue health programmatically. Use it to integrate merge queue operations into your CI/CD pipelines, build custom dashboards, or automate queue management across repositories.

The API is an HTTP REST API hosted at `https://api.trunk.io/v1`. It returns JSON from all requests and uses standard HTTP response codes.

All requests must be [authenticated](../../setup-and-administration/apis/#authentication) by providing the `x-api-token` header.

## Endpoint summary

| Endpoint | Method | Description |
| --- | --- | --- |
| [`/submitPullRequest`](#pull-request-endpoints) | POST | Submit a PR to the merge queue for testing and merging |
| [`/cancelPullRequest`](#pull-request-endpoints) | POST | Remove a PR from the merge queue |
| [`/restartTestsOnPullRequest`](#pull-request-endpoints) | POST | Re-run tests on a PR currently in the queue |
| [`/getSubmittedPullRequest`](#pull-request-endpoints) | POST | Check the status of a submitted PR |
| [`/setImpactedTargets`](#pull-request-endpoints) | POST | Set impacted targets for a PR (used with [parallel queues](../optimizations/parallel-queues/)) |
| [`/getMergeQueueTestingDetails`](#pull-request-endpoints) | POST | Get details about in-progress merge queue testing |
| [`/createQueue`](#queue-endpoints) | POST | Create a new merge queue for a branch |
| [`/deleteQueue`](#queue-endpoints) | POST | Delete an empty merge queue |
| [`/getQueue`](#queue-endpoints) | POST | Get queue state, configuration, and enqueued PRs |
| [`/updateQueue`](#queue-endpoints) | POST | Update queue configuration (mode, concurrency, batching, etc.) |
| [`/getMergeQueueMetrics`](#metrics-endpoints) | GET | Get Prometheus-format metrics for monitoring |

## Common use cases

**CI/CD automation** — Submit PRs to the queue, check their status, and restart tests automatically from your CI pipelines.

**Queue management** — Create and configure queues for different branches, adjust concurrency and batching settings, or pause and drain queues during maintenance windows.

**Monitoring dashboards** — Use the Prometheus metrics endpoint to build custom Grafana dashboards or feed queue health data into your existing observability stack.

**PR status checks** — Query the status of submitted PRs to build custom notifications or gate downstream workflows.

## Request format

Most endpoints accept a JSON request body with these common fields:

```json
{
  "repo": {
    "host": "github.com",
    "owner": "my-org",
    "name": "my-repo"
  },
  "targetBranch": "main",
  "pr": {
    "number": 123
  }
}
```

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `repo.host` | string | Yes | Repository host (e.g., `github.com`) |
| `repo.owner` | string | Yes | Repository owner or organization |
| `repo.name` | string | Yes | Repository name |
| `targetBranch` | string | Yes | The branch the merge queue targets |
| `pr.number` | integer | Varies | The pull request number (required for PR endpoints) |

## Examples

### Submit a PR to the queue

```bash
curl -X POST https://api.trunk.io/v1/submitPullRequest \
  -H "Content-Type: application/json" \
  -H "x-api-token: $TRUNK_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "my-org",
      "name": "my-repo"
    },
    "targetBranch": "main",
    "pr": {
      "number": 123
    }
  }'
```

### Check PR status

```bash
curl -X POST https://api.trunk.io/v1/getSubmittedPullRequest \
  -H "Content-Type: application/json" \
  -H "x-api-token: $TRUNK_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "my-org",
      "name": "my-repo"
    },
    "targetBranch": "main",
    "pr": {
      "number": 123
    }
  }'
```

The response includes the PR state (`NOT_READY`, `PENDING`, `TESTING`, `TESTS_PASSED`, `MERGED`, `FAILED`, `CANCELLED`, or `PENDING_FAILURE`), priority information, and whether the PR is currently submitted to the queue.

### Get queue state

```bash
curl -X POST https://api.trunk.io/v1/getQueue \
  -H "Content-Type: application/json" \
  -H "x-api-token: $TRUNK_API_TOKEN" \
  -d '{
    "repo": {
      "host": "github.com",
      "owner": "my-org",
      "name": "my-repo"
    },
    "targetBranch": "main"
  }'
```

The response includes the queue state (`RUNNING`, `PAUSED`, `DRAINING`, or `SWITCHING_MODES`), configuration settings, and a list of all enqueued pull requests with their current states.

---

## Pull request endpoints

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

{% openapi-operation spec="trunk-api" path="/submitPullRequest" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/getMergeQueueTestingDetails" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

## Metrics endpoints

### Prometheus metrics

`GET /v1/getMergeQueueMetrics`

Returns merge queue metrics in Prometheus text exposition format. Authenticate with the `x-api-token` header.

| Parameter | Required | Description |
| --- | --- | --- |
| `repo` | No | Repository in `owner/name` format. If omitted, returns metrics for all repositories in the organization. Must be provided together with `repoHost`. |
| `repoHost` | Conditional | Repository host (e.g., `github.com`). Required if `repo` is specified. |

Response content type: `text/plain; version=0.0.4; charset=utf-8`

See [Prometheus metrics endpoint](../administration/metrics.md#prometheus-metrics-endpoint) for the full list of available metrics, scrape configuration, and example queries.

## Queue endpoints

Use these endpoints to create, configure, and manage merge queues. Each queue targets a specific branch in your repository. For more on running multiple queues, see [parallel queues](../optimizations/parallel-queues/).

{% openapi-operation spec="trunk-api" path="/createQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/deleteQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% hint style="warning" %}
The queue must be empty before it can be deleted. Cancel all enqueued PRs or wait for them to be merged first.
{% endhint %}

{% openapi-operation spec="trunk-api" path="/getQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/updateQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

## Related resources

* [CLI reference](merge-queue-cli-reference.md) — Command-line interface for merge queue operations
* [Metrics and monitoring](../administration/metrics.md) — Dashboard analytics and Prometheus endpoint details
* [Webhooks](../webhooks.md) — Event-driven notifications for queue activity
* [Settings and configurations](../administration/advanced-settings.md) — Queue settings available in the Trunk web app
* [Authentication](../../setup-and-administration/apis/#authentication) — API token setup and management
