---
description: Integrate with Trunk CI Analytics using the API
---

# CI Analytics

The Trunk CI Analytics API provides access to instrument any CI or build system. The API is an HTTP REST API, returns JSON from all requests, and uses standard HTTP response codes.

All requests must be [authenticated](./#authentication) by providing the `x-api-token` header.

## Track Events

<mark style="color:green;">`POST`</mark> `https://api.trunk.io/v1/metrics/trackEvents`

## Track Events

<mark style="color:green;">`POST`</mark> `https://api.trunk.io/v1/metrics/trackEvents`

The track events endpoint uploads event data about a CI run. Each event contains a start and end timestamp, metrics, tags, and an optional parent association ID.

#### Headers

| Name                                           | Type   | Description                  |
| ---------------------------------------------- | ------ | ---------------------------- |
| Content-Type<mark style="color:red;">\*</mark> | String | application/json             |
| x-api-token<mark style="color:red;">\*</mark>  | String | Trunk API Token              |
| x-source                                       | String | Name of the uploading client |

#### Request Body

| Name                                     | Type   | Description                                                                        |
| ---------------------------------------- | ------ | ---------------------------------------------------------------------------------- |
| repo<mark style="color:red;">\*</mark>   | Object | The repository in which the CI Event ran. See [repo](ci-analytics.md#repo) schema. |
| events<mark style="color:red;">\*</mark> | Array  | An array of event objects. See [event](ci-analytics.md#event) schema.              |

{% tabs %}
{% tab title="200: OK Events were created successfully" %}

{% endtab %}

{% tab title="401: Unauthorized Request is not authorized" %}

{% endtab %}

{% tab title="400: Bad Request Request body is not formed correctly" %}

{% endtab %}
{% endtabs %}

#### Headers

| Name                                           | Type   | Description  |
| ---------------------------------------------- | ------ | ------------ |
| Content-Type<mark style="color:red;">\*</mark> | String | AO8NCa6G0paE |
| x-api-token<mark style="color:red;">\*</mark>  | String | 3HCw9xVi1CBh |
| x-source                                       | String | JBoUSZxipIYA |

#### Request Body

| Name                                     | Type   | Description  |
| ---------------------------------------- | ------ | ------------ |
| repo<mark style="color:red;">\*</mark>   | Object | eN1mmETFshzM |
| events<mark style="color:red;">\*</mark> | Array  | Mk0uImz3AIoq |

#### Repo

Repo object properties:

<table data-full-width="true"><thead><tr><th>Property</th><th width="721.3333333333333">Description</th><th>Required<select><option value="25a8e84e0dbf4d55accabd36d1c71f74" label="Required" color="blue"></option><option value="8c34c2d0f5f94594b255e4ae9d7b8b70" label="Optional" color="blue"></option></select></th></tr></thead><tbody><tr><td><code>host</code></td><td>The name of the code host for this repository. Currently only <code>github.com</code> is supported.</td><td><span data-option="25a8e84e0dbf4d55accabd36d1c71f74">Required</span></td></tr><tr><td><code>owner</code></td><td>The owner of this repository</td><td><span data-option="25a8e84e0dbf4d55accabd36d1c71f74">Required</span></td></tr><tr><td><code>name</code></td><td>The name of this repository</td><td><span data-option="25a8e84e0dbf4d55accabd36d1c71f74">Required</span></td></tr></tbody></table>

For example, the repository `https://github.com/trunk-io/jenkins-plugin` would be

```json
{
  "host": "github.com",
  "owner": "trunk-io",
  "name": "jenkins-plugin"
}
```

#### Event

Event object properties

<table data-full-width="true"><thead><tr><th width="153">Property</th><th width="601.3333333333333">Description</th><th>Required<select><option value="66d3b13cd60643799b2e1091ada92a07" label="Required" color="blue"></option><option value="6fb35305397e4449bd4c1fa0d371eff1" label="Optional" color="blue"></option></select></th><th>Type<select><option value="945bb79052184bbb97ae94bca5496c54" label="String" color="blue"></option><option value="909c4e76e0044f818d97daca0d29837c" label="Timestamp" color="blue"></option><option value="574a82c72c02434f9ad51c20afa9e58f" label="Object" color="blue"></option><option value="205a93b64af0478389941000f7689f89" label="Number" color="blue"></option></select></th></tr></thead><tbody><tr><td><code>id</code></td><td>A unique identifier for this event</td><td><span data-option="66d3b13cd60643799b2e1091ada92a07">Required</span></td><td><span data-option="945bb79052184bbb97ae94bca5496c54">String</span></td></tr><tr><td><code>chainId</code></td><td>The root event id. <code>chainId</code> is used to group all events that were part of the same run.</td><td><span data-option="66d3b13cd60643799b2e1091ada92a07">Required</span></td><td><span data-option="945bb79052184bbb97ae94bca5496c54">String</span></td></tr><tr><td><code>parent</code></td><td>The parent event. Not required if this event has no parent.</td><td><span data-option="6fb35305397e4449bd4c1fa0d371eff1">Optional</span></td><td><span data-option="574a82c72c02434f9ad51c20afa9e58f">Object</span></td></tr><tr><td><code>createdAt</code></td><td>The millisecond epoch marking the start of this event</td><td><span data-option="66d3b13cd60643799b2e1091ada92a07">Required</span></td><td><span data-option="205a93b64af0478389941000f7689f89">Number</span></td></tr><tr><td><code>finishedAt</code></td><td>The millisecond epoch marking the end of this event</td><td><span data-option="6fb35305397e4449bd4c1fa0d371eff1">Optional</span></td><td><span data-option="205a93b64af0478389941000f7689f89">Number</span></td></tr><tr><td><code>conclusion</code></td><td><code>"SUCCESS" | "FAILURE" | "CANCELLED" | "TIMED_OUT" | "SKIPPED"</code></td><td><span data-option="6fb35305397e4449bd4c1fa0d371eff1">Optional</span></td><td><span data-option="945bb79052184bbb97ae94bca5496c54">String</span></td></tr><tr><td><code>payload</code></td><td>An object containing metrics and tags. See <a href="ci-analytics.md#payload">payload</a> schema.</td><td><span data-option="6fb35305397e4449bd4c1fa0d371eff1">Optional</span></td><td><span data-option="574a82c72c02434f9ad51c20afa9e58f">Object</span></td></tr><tr><td><code>sequence</code></td><td>Describes the workflow, pipeline, or job, etc. that this event is from. See <a href="ci-analytics.md#sequence">sequence</a> schema.</td><td><span data-option="6fb35305397e4449bd4c1fa0d371eff1">Optional</span></td><td><span data-option="574a82c72c02434f9ad51c20afa9e58f">Object</span></td></tr></tbody></table>

#### Parent

Parent object properties:

<table data-full-width="true"><thead><tr><th width="165">Property</th><th width="588.5">Description</th><th width="102">Required<select><option value="e921922113714280a463790797af3b61" label="Required" color="blue"></option><option value="102076614aea441bac1f1222322804c8" label="Optional" color="blue"></option></select></th><th>Type<select><option value="c77b377b4b6d481e8517406f716b0277" label="String" color="blue"></option></select></th></tr></thead><tbody><tr><td><code>eventId</code></td><td>The parent event's unique identifier</td><td><span data-option="e921922113714280a463790797af3b61">Required</span></td><td><span data-option="c77b377b4b6d481e8517406f716b0277">String</span></td></tr><tr><td><code>sequenceKey</code></td><td>The key to the parent event's sequence</td><td><span data-option="e921922113714280a463790797af3b61">Required</span></td><td><span data-option="c77b377b4b6d481e8517406f716b0277">String</span></td></tr></tbody></table>

#### Payload

Payload object properties:

<table data-full-width="true"><thead><tr><th width="127.49999999999997">Property</th><th width="644">Description</th><th>Required<select><option value="929852d24bd54a93931e6e817adc5f1c" label="Required" color="blue"></option><option value="2ffe59d31f5141a09b4f9bb55880bf92" label="Optional" color="blue"></option></select></th><th>Type<select><option value="16dd80689dcc4959999cc99a54371ade" label="Object" color="blue"></option></select></th></tr></thead><tbody><tr><td><code>metrics</code></td><td>Each metric is an object containing the metric key and value (where value is a number). For example: <code>{"k": "duration_ms", "v": 101920}</code></td><td><span data-option="929852d24bd54a93931e6e817adc5f1c">Required</span></td><td><span data-option="16dd80689dcc4959999cc99a54371ade">Object</span></td></tr><tr><td><code>tags</code></td><td>Each metric is an object containing the tag key and value (where value can be a number or a string). For example: <code>{"k": "runner", "v": "self-hosted"}</code></td><td><span data-option="929852d24bd54a93931e6e817adc5f1c">Required</span></td><td><span data-option="16dd80689dcc4959999cc99a54371ade">Object</span></td></tr></tbody></table>

#### Sequence

A sequence describes the CI pipeline, job, workflow, etc. Events are grouped under sequences using the `sequenceKey`.

Sequence object properties:

<table data-full-width="true"><thead><tr><th width="135.49999999999997">Property</th><th width="201">Description</th><th width="111">Required<select><option value="eebbee918b604ece8ce2482a16759b69" label="Required" color="blue"></option><option value="3f4f7f26257b4582be4ff01fb7566a3a" label="Optional" color="blue"></option></select></th><th width="99">Type<select><option value="7acdd76faf8d4c749556056b1e90e615" label="String" color="blue"></option><option value="3e905fa3815f4842b7c49a95569b69c0" label="Object" color="blue"></option></select></th><th>Examples</th></tr></thead><tbody><tr><td><code>platform</code></td><td>The string name of the CI platform. Must be <code>snake_case</code>.</td><td><span data-option="eebbee918b604ece8ce2482a16759b69">Required</span></td><td><span data-option="7acdd76faf8d4c749556056b1e90e615">String</span></td><td><code>jenkins</code>, <code>trunk_merge</code>.</td></tr><tr><td><code>kind</code></td><td>The type of the sequence.</td><td><span data-option="eebbee918b604ece8ce2482a16759b69">Required</span></td><td><span data-option="7acdd76faf8d4c749556056b1e90e615">String</span></td><td><code>job</code>, <code>workflow</code></td></tr><tr><td><code>key</code></td><td>An identifier for this <code>sequence</code>. Must be unique within the <code>repo</code> and &#x3C; 128 characters.</td><td><span data-option="eebbee918b604ece8ce2482a16759b69">Required</span></td><td><span data-option="7acdd76faf8d4c749556056b1e90e615">String</span></td><td><code>my-global-uuid</code></td></tr><tr><td><code>name</code></td><td>The name of this <code>sequence</code>. These will appear as top-level entries in your CI Analytics dashboards.</td><td><span data-option="eebbee918b604ece8ce2482a16759b69">Required</span></td><td><span data-option="7acdd76faf8d4c749556056b1e90e615">String</span></td><td><code>Integration Tests [linux]</code>.</td></tr><tr><td><code>payload</code></td><td>The tags for this sequence. See <a href="ci-analytics.md#payload">payload</a> schema. (note: metrics are not supported for a <code>sequence</code>)</td><td><span data-option="eebbee918b604ece8ce2482a16759b69">Required</span></td><td><span data-option="3e905fa3815f4842b7c49a95569b69c0">Object</span></td><td><p><code>{</code></p><p><code>metrics: [],</code></p><p><code>tags: []</code></p><p><code>}</code></p></td></tr></tbody></table>

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
