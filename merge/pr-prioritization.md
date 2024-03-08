---
description: >-
  Optional PR priorities to control the order PRs are tested and merged in the
  Merge queue.
---

# PR Prioritization

Sometimes you have a high-priority change that must be merged quickly, but you still want to validate it in the merge queue. For these cases you can use **PR Prioritization** to create a PR that goes through the queue faster than others.

## Setting Priorities

When submitting a PR to Merge you can set the priority to one of the following strings: `"urgent"`, `"high"`, `"medium"`, or `"low"`. The default priority of a PR is `"medium"` if it is submitted without one.&#x20;

If you submit the PR with a GitHub comment you can specify the priority with the `--priority` or `-p` options like this:

```
/trunk merge --priority=high
```

or

```
/trunk merge -p urgent
```

If you submit the PR from the command line you can use the same options:

```
trunk merge <pr-number> --priority=high
```

The priority can also be specified from the [Merge Web UI](using-the-webapp.md).

## Numeric Priorities

You can also use a number from 0 to 255 as the priority in addition to the text labels. The labels are equivalent to the following numbers:

| label  | value |
| ------ | ----- |
| urgent | 0     |
| high   | 10    |
| medium | 100   |
| low    | 200   |

Numbers can be used the in the same way as the text labels. ex: `/trunk merge -p 0` to submit the PR to Trunk Merge with an `urgent` priority.

## How Priority Affects PR Order

PRs with a higher priority will always begin testing before any other PR that isn't currently being tested, ensuring that prioritized PRs move into the queue as soon as they can. A PR without a priority will use the default `medium` (100) priority. If there is already a PR in the queue with the exact same priority then the new one will be behind it.&#x20;

When prioritizing a PR, Merge will explictly **not interrupt** any currently tested PR, as it is usually not a good idea to restart PRs even if you want another PR to be sooner. Because of this, if a PR is submitted with a priority and there is still room in the queue to begin testing PRs, it will being testing as normal without interrupting other PRs.

**There is one exception to this rule.** Sometimes, when there is a PR urgent enough to get in that it is worth the cost of restarting a currently testing PR, you can move the new PR to the front using the `"urgent"` priority. This is the only time Merge will reschedule a PR that is already in testing.

#### Example:

Say you have a queue that is configured to test two PRs at once. The queue currently looks like

**main <- A (testing) <- B(testing) <- C (pending, waiting to test)**

If you submit a PR **D** with a `"high"` priority it will put in front of **C** (since it is a higher priority than C and C is not testing). **D** will begin as soon either **A** or **B** finishes.
