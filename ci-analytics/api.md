---
description: Integrate with Trunk CI Analytics using the API
---

# API Reference

## REST API Overview

The Trunk CI Analytics API aims to give you access to instrument any CI or build system. The API is an HTTP REST API. The API uses status codes to indicate the success or failure of requests, returns JSON from all requests, and uses standard HTTP response codes. Use the Trunk CI Analytics API to access Trunk CI Analytics programmatically.\
\
The current version of the Trunk CI Analytics API is v1.

## Getting Started

Authenticate to the API with an API key using the header `x-api-token`.

### Finding your API token

You can find your API token in the [Trunk App](https://app.trunk.io).

{% @supademo/embed demoId="BILCaBxa05Hkol0Ck4Z-y" url="https://app.supademo.com/demo/BILCaBxa05Hkol0Ck4Z-y" %}

## Endpoints

{% swagger path="/trackEvent" summary="Track Events" method="post" baseUrl="https://api.trunk.io/v1/metrics" fullWidth="true" %}
{% swagger-description %}
The track events endpoint uploads event data about a CI run. Each event contains a start and end timestamp, metrics, tags, and an optional parent association ID.
{% endswagger-description %}

{% swagger-parameter in="header" name="Content-Type" required="true" type="String" %}
application/json
{% endswagger-parameter %}

{% swagger-parameter in="header" name="x-api-token" type="String" required="true" %}
Trunk API Token
{% endswagger-parameter %}

{% swagger-parameter in="body" name="repo" type="Object" required="true" %}
The repository in which the CI Event ran. See [repo](api.md#repo) schema.
{% endswagger-parameter %}

{% swagger-parameter in="body" name="events" type="Array" required="true" %}
An array of event objects. See [event](api.md#event) schema.
{% endswagger-parameter %}

{% swagger-parameter in="header" name="x-source" type="String" required="false" %}
Name of the uploading client
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Events were created successfully" %}

{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="Request body is not formed correctly" %}

{% endswagger-response %}

{% swagger-response status="401: Unauthorized" description="Request is not authorized" %}

{% endswagger-response %}
{% endswagger %}

#### Repo

Repo object properties:

<table data-full-width="true"><thead><tr><th>Property</th><th width="721.3333333333333">Description</th><th data-type="select">Required</th></tr></thead><tbody><tr><td><code>host</code></td><td>The name of the code host for this repository. Currently only <code>github.com</code> is supported.</td><td></td></tr><tr><td><code>owner</code></td><td>The owner of this repository</td><td></td></tr><tr><td><code>name</code></td><td>The name of this repository</td><td></td></tr></tbody></table>

For example, the repository `https://github.com/trunk-io/jenkins-plugin` would be&#x20;

```json
{
  "host": "github.com",
  "owner": "trunk-io",
  "name": "jenkins-plugin"
}
```

#### Event

Event object properties

<table data-full-width="true"><thead><tr><th width="153">Property</th><th width="601.3333333333333">Description</th><th data-type="select">Required</th><th data-type="select">Type</th></tr></thead><tbody><tr><td><code>id</code></td><td>A unique identifier for this event</td><td></td><td></td></tr><tr><td><code>chainId</code></td><td>The root event id. <code>chainId</code> is used to group all events that were part of the same run.</td><td></td><td></td></tr><tr><td><code>parent</code></td><td>The parent event. Not required if this event has no parent.</td><td></td><td></td></tr><tr><td><code>createdAt</code></td><td>The millisecond epoch marking the start of this event</td><td></td><td></td></tr><tr><td><code>finishedAt</code></td><td>The millisecond epoch marking the end of this event</td><td></td><td></td></tr><tr><td><code>conclusion</code></td><td><code>"SUCCESS" | "FAILURE" | "CANCELLED" | "TIMED_OUT" | "SKIPPED"</code></td><td></td><td></td></tr><tr><td><code>payload</code></td><td>An object containing metrics and tags. See <a href="api.md#payload">payload</a> schema.</td><td></td><td></td></tr><tr><td><code>sequence</code></td><td>Describes the workflow, pipeline, or job, etc. that this event is from. See <a href="api.md#sequence">sequence</a> schema.</td><td></td><td></td></tr></tbody></table>

#### Parent

Parent object properties:

<table data-full-width="true"><thead><tr><th width="165">Property</th><th width="588.5">Description</th><th width="102" data-type="select">Required</th><th data-type="select">Type</th></tr></thead><tbody><tr><td><code>eventId</code></td><td>The parent event's unique identifier</td><td></td><td></td></tr><tr><td><code>sequenceKey</code></td><td>The key to the parent event's sequence</td><td></td><td></td></tr></tbody></table>

#### Payload

Payload object properties:

<table data-full-width="true"><thead><tr><th width="127.49999999999997">Property</th><th width="644">Description</th><th data-type="select">Required</th><th data-type="select">Type</th></tr></thead><tbody><tr><td><code>metrics</code></td><td>Each metric is an object containing the metric key and value (where value is a number). For example: <code>{"k": "duration_ms", "v": 101920}</code></td><td></td><td></td></tr><tr><td><code>tags</code></td><td>Each metric is an object containing the tag key and value (where value can be a number or a string). For example: <code>{"k": "runner", "v": "self-hosted"}</code></td><td></td><td></td></tr></tbody></table>

#### Sequence

A sequence describes the CI pipeline, job, workflow, etc. Events are grouped under sequences using the `sequenceKey`.

Sequence object properties:

<table data-full-width="true"><thead><tr><th width="134.49999999999997">Property</th><th width="619">Description</th><th width="111" data-type="select">Required</th><th data-type="select">Type</th></tr></thead><tbody><tr><td><code>platform</code></td><td>The string name of the CI platform.</td><td></td><td></td></tr><tr><td><code>kind</code></td><td>The type of the sequence (i.e., <code>job</code>, <code>workflow</code>, <code>pipeline</code>).</td><td></td><td></td></tr><tr><td><code>key</code></td><td>An identifier for this <code>sequence</code>.</td><td></td><td></td></tr><tr><td><code>name</code></td><td>The name of this <code>sequence</code></td><td></td><td></td></tr><tr><td><code>payload</code></td><td>The tags for this sequence. See <a href="api.md#payload">payload</a> schema. (note: metrics are not supported for a <code>sequence</code>)</td><td></td><td></td></tr></tbody></table>

#### Example Request

{% code fullWidth="true" %}
```bash
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
	"events": [{
			"id": "fba555ee-90ce-42ca-a60c-38d200e9290e",
			"chainId": "b0ea8b0d-6574-4421-a63b-56f04eab9738",
			"createdAt": 1694616487000,
			"finishedAt": 1694615487000,
			"conclusion": "SUCCESS",
			"sequence": {
				"platform": "Jenkins",
				"kind": "pipeline",
				"key": "test-pipeline",
				"name": "Trying out a test pipeline",
				"payload": {
					"tags": [{
						"k": "label",
						"v": "self-hosted"
					}]
				}
			},
			"payload": {
				"metrics": [{
						"k": "duration_ms",
						"v": 1000
					},
					{
						"k": "api_latency",
						"v": 500
					}
				],
				"tags": [{
						"k": "branch",
						"v": "merge-PR-1"
					},
					{
						"k": "sha",
						"v": "88962a71bcfa92e5950670fc7e3f2b9f8d993b87"
					}
				]
			}
		},
		{
			"id": "test-workflow-a-1",
			"chainId": "test-workflow-a-1",
			"createdAt": 1694616487000,
			"finishedAt": 1694615487000,
			"conclusion": "SUCCESS",
			"parent": {
				"eventId": "fba555ee-90ce-42ca-a60c-38d200e9290e",
				"chainId": "b0ea8b0d-6574-4421-a63b-56f04eab9738"
			},
			"sequence": {
				"platform": "Jenkins",
				"kind": "nested-pipeline",
				"key": "test-pipeline/nested-pipeline",
				"name": "Trying out a test nested pipeline",
				"payload": {
					"tags": [{
						"k": "label",
						"v": "self-hosted"
					}]
				}
			},
			"payload": {
				"metrics": [{
						"k": "duration_ms",
						"v": 1000
					},
					{
						"k": "api_latency",
						"v": 500
					}
				],
				"tags": [{
						"k": "branch",
						"v": "merge-PR-1"
					},
					{
						"k": "sha",
						"v": "88962a71bcfa92e5950670fc7e3f2b9f8d993b87"
					}
				]
			}
		}
	]
}'
```
{% endcode %}
