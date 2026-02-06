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
