---
description: Trunk APIs for building custom integrations.
---

# API Reference

## REST API Overview

Trunk provides HTTP REST APIs for each of our features. The APIs use status codes to indicate the success or failure of requests, return JSON from all requests, and use standard HTTP response codes. All API requests must be authenticated.

## Available APIs

* [Flaky Tests](flaky-tests.md): for accessing information like quarantined tests in your repo.
* [Merge API](merge.md) : for controlling the Trunk Merge Queue
* [CI Analytics API](ci-analytics.md): for submitting events to be tracked by the CI Analytics engine.

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
