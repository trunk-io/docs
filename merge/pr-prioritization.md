---
description: Control the order PRs are tested and merged in the Merge Queue
---

# PR Prioritization

When a high-priority change must be merged quickly but still validated by the Merge queue, you can use **PR Prioritization** to create a PR that goes through the queue faster than others.

## Setting Priorities

When submitting a PR to Merge you can set the priority to one of the text labels below or a number between 0 - 255. &#x20;

|        |     |                                                                                           |
| ------ | --- | ----------------------------------------------------------------------------------------- |
| urgent | 0   | highest priority. Urgent items will interrupt running jobs and begin testing immediately. |
| high   | 10  |                                                                                           |
| medium | 100 | default priority                                                                          |
| low    | 200 |                                                                                           |

The priority is set when the PR is submitted to Merge:

{% tabs %}
{% tab title="GitHub comment" %}
Specify the priority in a GitHub comment using the `--priority` or `-p` options with either labels or numbers

```
/trunk merge --priority=high
```

or

```
/trunk merge -p 10
```
{% endtab %}

{% tab title="Command Line" %}
Specify the priority on the command line using the `--priority` or `-p` options with either labels or numbers.

```
trunk merge <pr-number> --priority=high
```

or

```
trunk merge <pr-number> -p 10
```
{% endtab %}

{% tab title="Web UI" %}
The priority can also be specified from the [Merge Web UI](using-the-webapp.md).
{% endtab %}
{% endtabs %}

## How Priority Affects PR Order

PRs with a higher priority will always begin testing before any other PR that isn't currently being tested, ensuring that prioritized PRs move into the queue as soon as they can. A PR without a priority will use the default `medium` (100) priority. If there is already a PR in the queue with the exact same priority then the new one will be behind it.&#x20;

When prioritizing a PR, Merge will explicitly **not interrupt** any currently testing PR, as it is usually costly to restart testing on PRs even if you want another PR to be sooner. Because of this, if a PR is submitted with a priority and there is still room in the queue to begin testing PRs, it will being testing as normal without interrupting other PRs.

**There is one exception to this rule.** Sometimes, when there is a PR urgent enough to get in that it is worth the cost of restarting a currently testing PR, you can move the new PR to the front using the `"urgent"` priority. This is the only time Merge will reschedule a PR that is already in testing.

#### Example:

Say you have a queue that is configured to test two PRs at once. The queue currently looks like this:

**main <- A (testing) <- B(testing) <- C (pending)**

If you submit a PR D with a `"high"` priority it will be put in front of C (since it is a higher priority than C and C is not testing). D will begin as soon either A or B finishes, like this:

**main <- A (testing) <- B(testing) <- D (pending) <- C (pending)**

If instead you submit PR D with an "urgent" priority, then D would be tested immediately,  A would be restarted, and B would be bumped back to pending, like this:

**main <- D (testing) <- A (restarting) <- B(pending) <- C (pending)**
