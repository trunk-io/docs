---
description: Public Trunk Merge Queue API. All requests should be authenticated.
---

# Merge Queue

The Trunk Merge Queue API provides access to submit PRs for testing and merging, canceling PRs, and providing extra information to optimize the queue.  The API is an HTTP REST API, returns JSON from all requests, and uses standard HTTP response codes.&#x20;

All requests must be [authenticated](./#authentication) by providing the `x-api-token` header.

{% swagger src="../.gitbook/assets/mergeapi.json" path="/submitPullRequest" method="post" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endswagger %}

{% swagger src="../.gitbook/assets/mergeapi.json" path="/cancelPullRequest" method="post" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endswagger %}

{% swagger src="../.gitbook/assets/mergeapi.json" path="/host/github/owner/{owner}/name/{name}/branch/{targetBranch}/pr/{prNumber}" method="get" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endswagger %}

{% swagger src="../.gitbook/assets/mergeapi.json" path="/restartTestsOnPullRequest" method="post" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endswagger %}

{% swagger src="../.gitbook/assets/mergeapi.json" path="/setImpactedTargets" method="post" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endswagger %}

