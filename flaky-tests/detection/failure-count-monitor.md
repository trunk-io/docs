---
description: Detect flaky or broken tests as soon as they accumulate a configured number of failures
---

# Failure Count Monitor

The failure count monitor flags a test the moment it accumulates a configured number of failures on monitored branches within a rolling time window. Unlike the failure rate monitor, which requires a failure *rate* calculated over many runs, the failure count monitor reacts to individual failures without needing a minimum sample size or a percentage calculation.

This makes it well-suited for stable branches like `main` where any test failure is unexpected and worth investigating immediately.

## When to Use This Monitor

Use the failure count monitor when you want immediate visibility into test failures on branches that should be green. Common scenarios:

- **Stable branch alerting:** Flag any test that fails on `main`, even once. On a branch where all tests should pass, a single failure is a meaningful signal.
- **Post-merge regression detection:** Catch tests that start failing after a merge, before the failure rate accumulates enough data for a failure rate monitor to trigger.
- **High-confidence branches:** Monitor merge queue or release branches where failures are suspicious by definition.

If you need to detect patterns of intermittent failure over time (e.g., a test that fails 20% of the time), use a [failure rate monitor](failure-rate-monitor.md) instead. If you want to catch tests that fail and then pass on retry within a single commit, [pass-on-retry](pass-on-retry-monitor.md) handles that automatically.

## Detection Type

Each failure count monitor has a **detection type** -- either **flaky** or **broken** -- which controls what status a test receives when the monitor flags it:

- **Flaky monitors** are appropriate when failures on the monitored branch are likely non-deterministic. A test that fails once on `main` but passes on retry is probably flaky.
- **Broken monitors** are appropriate when failures indicate a real regression. If a test fails on `main` and you expect it to keep failing until someone fixes it, broken is the right classification.

The detection type is set at creation and cannot be changed afterward. If you need to switch a monitor's type, create a new monitor with the desired type and disable the old one.

## How It Works

The monitor counts the number of test failures on configured branches within a rolling time window. When a test reaches the configured failure count, it is flagged.

### Example

You configure a failure count monitor with:

| Setting | Value |
|---|---|
| Detection type | Broken |
| Failure count | 1 |
| Window | 30 minutes |
| Resolution timeout | 2 hours |
| Branches | `main` |

A developer merges a change that breaks `test_checkout`. Here is what happens:

1. `test_checkout` fails on the next CI run on `main`.
2. The monitor sees 1 failure within the 30-minute window, which meets the configured failure count of 1.
3. `test_checkout` is immediately flagged as **broken**.
4. The developer identifies the issue and merges a correction.
5. Two hours pass with no new failures for `test_checkout`.
6. The monitor automatically resolves the test back to **healthy**.

If another test, `test_signup`, also failed during that window, it would be flagged independently. Each test is evaluated on its own.

## Configuration

### Failure Count

The number of failures required to trigger detection. The default is **1**, meaning any single failure on a monitored branch flags the test.

Setting this higher (e.g., 3) requires multiple failures before the monitor reacts. This is useful if you want to filter out one-off infrastructure blips while still catching tests that fail repeatedly in a short window.

### Window Duration

The rolling time window over which failures are counted. Only test failures within this window contribute to the failure count.

A shorter window (e.g., 30 minutes) limits detection to very recent failures. A longer window (e.g., 6 hours) catches failures that are spread out over time but still accumulating.

The window should be long enough to capture the failures you care about but short enough that old failures roll off naturally. For a monitor with a failure count of 1, the window mainly controls how quickly a detection event is created after a failure. In practice, the pipeline evaluates frequently, so detection is near-immediate regardless of window size.

### Resolution Timeout

How long a flagged test must go without any new failures before it is automatically resolved. This is the only way a failure count monitor resolves. There is no "recovery rate" or sample-based resolution like the failure rate monitor.

For example, with a resolution timeout of 2 hours, a test that was flagged at 3:00 PM will resolve at 5:00 PM if no new failures occur. If a new failure arrives at 4:30 PM, the clock resets, and the test will not resolve until 6:30 PM.

The resolution timeout must be at least as long as the detection window. If the window is 30 minutes, the resolution timeout should be 30 minutes or longer.

Choose a resolution timeout that gives your team enough time to verify a fix has landed. A short timeout (e.g., 30 minutes) resolves quickly but may prematurely clear tests that fail intermittently. A longer timeout (e.g., 24 hours) is more conservative and ensures the test stays flagged until it has been clean for a full day.

### Branch Scope

Which branches the monitor evaluates. You can specify branch names or glob patterns. Only test failures on matching branches count toward the failure count.

Branch patterns work the same way as [failure rate monitor branch patterns](failure-rate-monitor.md#branch-pattern-syntax), including glob syntax and merge queue patterns. Refer to that section for pattern syntax, examples, and tips.

## Resolution Behavior

A failure count monitor resolves in one way: **the test stops failing for long enough.**

When the configured resolution timeout elapses without a new failure on any monitored branch, the test is resolved as healthy. There is no rate-based recovery and no stale timeout. If a test stops running entirely (e.g., it was deleted or renamed), it remains in its flagged state until the resolution timeout passes from the last observed failure.

This time-based approach means you don't need to wait for enough passing runs to bring a failure rate down. Once the test is quiet, it resolves.

## Muting

You can temporarily mute a failure count monitor for a specific test case. See [Muting monitors](README.md#muting-monitors) for details.

## Choosing Between Monitors

| Scenario | Recommended monitor |
|---|---|
| Any failure on `main` should be flagged immediately | **Failure count** with count = 1 |
| Tests failing at an elevated rate over many runs | **Threshold** with appropriate activation percentage |
| A test fails then passes on retry in the same commit | **Pass-on-retry** (enabled by default) |
| Consistently failing tests (80%+ failure rate) | **Threshold** with broken detection type |
| Quick alerting on merge queue failures | **Failure count** scoped to merge queue branches |
