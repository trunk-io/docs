# Flaky Tests

The Trunk Flaky Tests API provides access to check the status of Trunk services and fetch [quarantined](../../flaky-tests/quarantining.md) tests in your project. The API is an HTTP REST API, returns JSON from all requests, and uses standard HTTP response codes.

All requests must be [authenticated](./#authentication) by providing the `x-api-token` header.

{% openapi-operation spec="trunk-api" path="/flaky-tests/list-quarantined-tests" method="post" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

