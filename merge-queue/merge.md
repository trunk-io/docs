---
description: Public Trunk Merge Queue API. All requests should be authenticated.
---

# Merge Queue API

The Trunk Merge Queue API provides access to submit PRs for testing and merging, canceling PRs, and providing extra information to optimize the queue. The API is an HTTP REST API, returns JSON from all requests, and uses standard HTTP response codes.

All requests must be [authenticated](../references/apis/#authentication) by providing the `x-api-token` header.



{% openapi src="../.gitbook/assets/mergeapi.json" path="/submitPullRequest" method="post" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endopenapi %}

{% openapi src="../.gitbook/assets/mergeapi.json" path="/getSubmittedPullRequest" method="post" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endopenapi %}

{% openapi src="../.gitbook/assets/mergeapi.json" path="/restartTestsOnPullRequest" method="post" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endopenapi %}

{% openapi src="../.gitbook/assets/mergeapi.json" path="/cancelPullRequest" method="post" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endopenapi %}

{% openapi src="../.gitbook/assets/mergeapi.json" path="/getQueue" method="post" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endopenapi %}

{% openapi src="../.gitbook/assets/mergeapi.json" path="/setImpactedTargets" method="post" %}
[mergeapi.json](../.gitbook/assets/mergeapi.json)
{% endopenapi %}

{% openapi-operation spec="manual-merge-api" path="/updateQueue" method="post" %}
[OpenAPI manual-merge-api](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/ef0b6658a709da6917f20852e67f77196a18741e382b998dd5258c6f4c1fc126.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20251006%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20251006T204330Z&X-Amz-Expires=172800&X-Amz-Signature=70c102ca3da4ad8d08927221d4987fc177998deca5acf5be1dd172564f34f4b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}

