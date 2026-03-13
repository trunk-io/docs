---
description: Public Trunk Merge Queue API. All requests should be authenticated.
---

# API reference

The Trunk Merge Queue API provides access to submit PRs for testing and merging, canceling PRs, and providing extra information to optimize the queue. The API is an HTTP REST API, returns JSON from all requests, and uses standard HTTP response codes.

All requests must be [authenticated](../../setup-and-administration/apis/#authentication) by providing the `x-api-token` header.

## Pull Request Endpoints

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

## Metrics Endpoints

### Prometheus metrics

`GET /v1/getMergeQueueMetrics`

Returns merge queue metrics in Prometheus text exposition format. Authenticate with the `x-api-token` header.

| Parameter | Required | Description |
| --- | --- | --- |
| `repo` | No | Repository in `owner/name` format. If omitted, returns metrics for all repositories in the organization. |
| `repoHost` | No | Repository host. Defaults to `github.com`. |

Response content type: `text/plain; version=0.0.4; charset=utf-8`

See [Prometheus metrics endpoint](../administration/metrics.md#prometheus-metrics-endpoint) for the full list of available metrics, scrape configuration, and example queries.

## Queue Endpoints

{% openapi-operation spec="trunk-api" path="/createQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/deleteQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/getQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/updateQueue" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}
