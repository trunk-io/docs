---
description: Trunk APIs for integrating with Trunk products
---

# API Reference

## REST API Overview

Trunk provides HTTP REST APIs for several of our products. The APIs use status codes to indicate the success or failure of requests, returns JSON from all requests, and uses standard HTTP response codes. All API requests must be authenticated.

## Available APIs

* Flaky Tests: for accessing information like quarantined tests in your repo.
* [Merge API](merge.md) : for controlling the Trunk Merge Queue
* [CI Analytics API](../ci-analytics/setup/api.md): for submitting events to be tracked by the CI Analytics engine.

## Authentication

Authenticate to the API with an API key using the header `x-api-token`.

### Finding your API token

You can find your API token in the [Trunk App](https://app.trunk.io).

{% @supademo/embed demoId="BILCaBxa05Hkol0Ck4Z-y" url="https://app.supademo.com/demo/BILCaBxa05Hkol0Ck4Z-y" %}

### Example

To submit an empty list of events to be tracked, do the following from the command line.

```sh
curl \
    -i \
    -X POST https://api.trunk.io/v1/metrics/trackEvents \
    -H "Content-Type: application/json" \
    -H "x-source: curl-sample" \
    -H "x-api-token: {REDACTED}" \
    -d '{
	"repo": {
		"host": "github.com",
		"owner": "trunk-io",
		"name": "jenkins-plugin"
	},
	"events":[]
	}'
```
