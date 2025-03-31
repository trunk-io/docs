---
description: Control the order pull requests are tested and merged in the Merge Queue
---

# Priority

When a high-priority change must be merged quickly but still validated by the Merge queue, you can use **PR Prioritization** to create a PR that goes through the queue faster than others.

## Setting Priorities

You specify a custom priority for a pull request at the time of insertion into the queue:

{% tabs %}
{% tab title="GitHub comment" %}
```
/trunk merge --priority=<level>
```

or

```
/trunk merge -p <level>
```
{% endtab %}

{% tab title="Command Line" %}
```shell
trunk merge <pr-number> --priority=<level>
```

or

```
trunk merge <pr-number> -p <level>
```
{% endtab %}

{% tab title="Web UI" %}
The priority can also be specified from the [Merge Web UI](managing-merge-queue/using-the-webapp.md).
{% endtab %}
{% endtabs %}

valid values for the priority level:

<table><thead><tr><th width="151">label</th><th width="109">number</th><th>note</th></tr></thead><tbody><tr><td>urgent</td><td>0</td><td>urgent items will interrupt running jobs and begin testing immediately</td></tr><tr><td>high</td><td>10</td><td></td></tr><tr><td>medium</td><td>100</td><td>default priority</td></tr><tr><td>low</td><td>200</td><td></td></tr><tr><td></td><td>255</td><td>lowest possible priority</td></tr></tbody></table>

## How Priority Affects PR Order

PRs with a higher priority will always begin testing before any other PR that isn't currently being tested, ensuring that prioritized PRs move into the queue as soon as they can. A PR without a priority will use the default `medium` (100) priority. If there is already a PR in the queue with the same priority then the new one will be behind it.&#x20;

When prioritizing a PR, Merge will explicitly **not interrupt** any currently testing PR, as it is usually costly to restart testing on PRs even if you want another PR to be sooner. Because of this, if a PR is submitted with a priority and there is still room in the queue to begin testing PRs, it will begin testing as normal without interrupting other PRs.

**There is one exception to this rule.** Sometimes, when there is a PR urgent enough to get in that it is worth the cost of restarting a currently testing PR, you can move the new PR to the front using the `"urgent"` priority. This is the only time Merge will reschedule a PR that is already in testing.

#### Example:

Say you have a queue that is configured to test two PRs at once. The queue currently looks like this:

<img src="../.gitbook/assets/file.excalidraw (1).svg" alt="queue with two testing PRs and one pending" class="gitbook-drawing">

If you submit a PR D with a `"high"` priority it will be put in front of C (since it is a higher priority than C and C is not testing). D will begin as soon as either A or B finishes, like this:

<img src="../.gitbook/assets/file.excalidraw (1) (1).svg" alt="queue with two testing PRs and a new higher priority pending PR" class="gitbook-drawing">

If instead, you submit PR D with an `"urgent"` priority, then D would be tested immediately,  A would be restarted, and B would be bumped back to pending, like this:

<img src="../.gitbook/assets/file.excalidraw (2).svg" alt="queue with an urgent PR moved to the front and a normal PR restarting" class="gitbook-drawing">
