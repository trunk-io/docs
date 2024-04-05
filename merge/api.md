---
title: null
language_tabs:
  - http: HTTP
  - javascript: JavaScript
  - python: Python
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="">undefined vv1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Base URLs:

* <a href="https://api.trunk.io:433/v1">https://api.trunk.io:433/v1</a>

<h1 id="-impacted-targets">Impacted Targets</h1>

## Set impacted targets

> Code samples

```http
POST https://api.trunk.io:433/v1/setImpactedTargets HTTP/1.1
Host: api.trunk.io:433
Content-Type: application/json

```

```javascript
const inputBody = '{
  "repo": {
    "host": "github.com",
    "owner": "trunk-io",
    "name": "trunk"
  },
  "pr": {
    "number": 1,
    "sha": "1234567890abcdef"
  },
  "targetBranch": "main",
  "impactedTargets": [
    "services_backend"
  ]
}';
const headers = {
  'Content-Type':'application/json'
};

fetch('https://api.trunk.io:433/v1/setImpactedTargets',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Content-Type': 'application/json'
}

r = requests.post('https://api.trunk.io:433/v1/setImpactedTargets', headers = headers)

print(r.json())

```

`POST /setImpactedTargets`

Upload impacted targets for the PR and its current SHA. Used specifically when running the queue in Parallel mode

> Body parameter

```json
{
  "repo": {
    "host": "github.com",
    "owner": "trunk-io",
    "name": "trunk"
  },
  "pr": {
    "number": 1,
    "sha": "1234567890abcdef"
  },
  "targetBranch": "main",
  "impactedTargets": [
    "services_backend"
  ]
}
```

<h3 id="set-impacted-targets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» repo|body|[repo](#schemarepo)|false|none|
|»» host|body|string|false|The host of the repository. Currently only supports 'github.com'|
|»» owner|body|string|false|The owner of the repository|
|»» name|body|string|false|The name of the repository|
|» pr|body|[prWithSha](#schemaprwithsha)|false|none|
|»» number|body|number|false|The PR number|
|»» sha|body|string|false|The SHA of the PR|
|» targetBranch|body|[targetBranch](#schematargetbranch)|false|The branch the merge queue will be merging PRs into|
|» impactedTargets|body|any|false|none|
|»» *anonymous*|body|[string]|false|none|
|»» *anonymous*|body|string|false|Special value to indicate that all targets are impacted by the changes in the pull request|

#### Enumerated Values

|Parameter|Value|
|---|---|
|»» host|github.com|
|»» *anonymous*|IMPACTS_ALL|

<h3 id="set-impacted-targets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="-merge-items">Merge Items</h1>

## Submits a Pull Request to the queue

{% tabs %}
{% tab title="http" %}
```http
POST https://api.trunk.io:433/v1/queuePullRequest HTTP/1.1
Host: api.trunk.io:433
Content-Type: application/json

```
{% endtab %}
{% tab title="javascript" %}
```javascript
const inputBody = '{
  "repo": {
    "host": "github.com",
    "owner": "trunk-io",
    "name": "trunk"
  },
  "pr": {
    "number": 1
  },
  "targetBranch": "main",
  "priority": "low"
}';
const headers = {
  'Content-Type':'application/json'
};

fetch('https://api.trunk.io:433/v1/queuePullRequest',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```
{% endtab %}

{% tab title="python" %}
```python
import requests
headers = {
  'Content-Type': 'application/json'
}

r = requests.post('https://api.trunk.io:433/v1/queuePullRequest', headers = headers)

print(r.json())

```
{% endtab %}
{% endtabs %}

`POST /queuePullRequest`

> Body parameter

```json
{
  "repo": {
    "host": "github.com",
    "owner": "trunk-io",
    "name": "trunk"
  },
  "pr": {
    "number": 1
  },
  "targetBranch": "main",
  "priority": "low"
}
```

<h3 id="submits-a-pull-request-to-the-queue-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» repo|body|[repo](#schemarepo)|false|none|
|»» host|body|string|false|The host of the repository. Currently only supports 'github.com'|
|»» owner|body|string|false|The owner of the repository|
|»» name|body|string|false|The name of the repository|
|» pr|body|[pr](#schemapr)|false|none|
|»» number|body|number|false|The PR number|
|» targetBranch|body|[targetBranch](#schematargetbranch)|false|The branch the merge queue will be merging PRs into|
|» priority|body|any|false|none|
|»» *anonymous*|body|string|false|The priority name to assign to the PR when it begins testing in the queue|
|»» *anonymous*|body|number|false|The priority number (0 - 255, 0 is the highest) to assign to the PR when it begins testing in the queue|

#### Enumerated Values

|Parameter|Value|
|---|---|
|»» host|github.com|
|»» *anonymous*|low|
|»» *anonymous*|medium|
|»» *anonymous*|high|
|»» *anonymous*|urgent|

<h3 id="submits-a-pull-request-to-the-queue-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|

<aside class="success">
This operation does not require authentication
</aside>

## Restarts tests on a PR in the queue without moving its position or causing other PRs to be retested

> Code samples

```http
POST https://api.trunk.io:433/v1/restartTestsOnPullRequest HTTP/1.1
Host: api.trunk.io:433
Content-Type: application/json

```

```javascript
const inputBody = '{
  "repo": {
    "host": "github.com",
    "owner": "trunk-io",
    "name": "trunk"
  },
  "pr": {
    "number": 1
  },
  "targetBranch": "main"
}';
const headers = {
  'Content-Type':'application/json'
};

fetch('https://api.trunk.io:433/v1/restartTestsOnPullRequest',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```python
import requests
headers = {
  'Content-Type': 'application/json'
}

r = requests.post('https://api.trunk.io:433/v1/restartTestsOnPullRequest', headers = headers)

print(r.json())

```

`POST /restartTestsOnPullRequest`

> Body parameter

```json
{
  "repo": {
    "host": "github.com",
    "owner": "trunk-io",
    "name": "trunk"
  },
  "pr": {
    "number": 1
  },
  "targetBranch": "main"
}
```

<h3 id="restarts-tests-on-a-pr-in-the-queue-without-moving-its-position-or-causing-other-prs-to-be-retested-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» repo|body|[repo](#schemarepo)|false|none|
|»» host|body|string|false|The host of the repository. Currently only supports 'github.com'|
|»» owner|body|string|false|The owner of the repository|
|»» name|body|string|false|The name of the repository|
|» pr|body|[pr](#schemapr)|false|none|
|»» number|body|number|false|The PR number|
|» targetBranch|body|[targetBranch](#schematargetbranch)|false|The branch the merge queue will be merging PRs into|

#### Enumerated Values

|Parameter|Value|
|---|---|
|»» host|github.com|

<h3 id="restarts-tests-on-a-pr-in-the-queue-without-moving-its-position-or-causing-other-prs-to-be-retested-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_repo">repo</h2>
<!-- backwards compatibility -->
<a id="schemarepo"></a>
<a id="schema_repo"></a>
<a id="tocSrepo"></a>
<a id="tocsrepo"></a>

```json
{
  "host": "github.com",
  "owner": "trunk-io",
  "name": "trunk"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|host|string|false|none|The host of the repository. Currently only supports 'github.com'|
|owner|string|false|none|The owner of the repository|
|name|string|false|none|The name of the repository|

#### Enumerated Values

|Property|Value|
|---|---|
|host|github.com|

<h2 id="tocS_pr">pr</h2>
<!-- backwards compatibility -->
<a id="schemapr"></a>
<a id="schema_pr"></a>
<a id="tocSpr"></a>
<a id="tocspr"></a>

```json
{
  "number": 1
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number|number|false|none|The PR number|

<h2 id="tocS_prWithSha">prWithSha</h2>
<!-- backwards compatibility -->
<a id="schemaprwithsha"></a>
<a id="schema_prWithSha"></a>
<a id="tocSprwithsha"></a>
<a id="tocsprwithsha"></a>

```json
{
  "number": 1,
  "sha": "1234567890abcdef"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number|number|false|none|The PR number|
|sha|string|false|none|The SHA of the PR|

<h2 id="tocS_targetBranch">targetBranch</h2>
<!-- backwards compatibility -->
<a id="schematargetbranch"></a>
<a id="schema_targetBranch"></a>
<a id="tocStargetbranch"></a>
<a id="tocstargetbranch"></a>

```json
"main"

```

The branch the merge queue will be merging PRs into

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The branch the merge queue will be merging PRs into|

