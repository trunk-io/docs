# Flaky Tests

The Trunk Flaky Tests API provides access to check the status of Trunk services and fetch [unhealthy](../../flaky-tests/detection.md) or [quarantined](../../flaky-tests/quarantining.md) tests in your project. The API is an HTTP REST API, returns JSON from all requests, and uses standard HTTP response codes.

All requests must be [authenticated](./#authentication) by providing the `x-api-token` header.

{% openapi-operation spec="trunk-api" path="/flaky-tests/list-unhealthy-tests" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/flaky-tests/list-quarantined-tests" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}

{% openapi-operation spec="trunk-api" path="/flaky-tests/link-ticket-to-test-case" method="post" %}
[OpenAPI trunk-api](https://static.trunk.io/docs/openapi.json)
{% endopenapi-operation %}
