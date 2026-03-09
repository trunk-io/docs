---
description: Manually mark tests as flaky or healthy
---

# Manual Monitor

The manual monitor lets you explicitly mark tests as flaky. This is useful for tests you know are unreliable but that don't trigger automated detection, for example, tests that only flake in specific environments or under certain conditions that aren't visible in the test run data.

## How it works

You can mark any test as flaky or healthy from the test case view in the Trunk app.

<!-- SCREENSHOT: Manual flaky toggle on the test case view.
Show the test case detail page with the new manual monitor toggle/button.
Capture a test that is currently marked as manually flaky, showing how the
manual monitor appears in the monitor status list alongside any automated
monitors. This replaces the old "pencil dropdown" override UI that was
previously documented on the detection page. -->

When you mark a test as flaky, the manual monitor activates immediately and the test is flagged. When you mark a test as healthy, the manual monitor deactivates.

{% hint style="info" %}
The manual monitor replaces the previous "Override test status" pencil dropdown on the Tests tab. The behavior is similar, but manual overrides now participate in the monitor system. Marking a test as flaky creates an active manual monitor, and marking it as healthy deactivates the manual monitor. See [Interaction with automated monitors](#interaction-with-automated-monitors) below for how this differs from a simple status toggle.
{% endhint %}

## Interaction with automated monitors

The manual monitor follows the same rules as every other monitor. It's additive, not an override.

**Marking a test as flaky** always works. Even if no automated monitor has flagged the test, the manual monitor will make it flaky.

**Marking a test as healthy** deactivates the manual monitor, but it does not override automated monitors. If a threshold or pass-on-retry monitor is also active for the test, the test remains flaky until those monitors resolve on their own. This is intentional: if the system is detecting real flaky behavior, manually marking the test as healthy shouldn't suppress that signal. Address the underlying flakiness instead.

| Scenario | Test status |
|---|---|
| Manual active, no automated monitors active | Flaky |
| Manual active, threshold monitor also active | Flaky |
| Manual resolved, threshold monitor still active | Flaky |
| Manual resolved, no automated monitors active | Healthy |

## Muting

The manual monitor cannot be muted. If you want to suppress a test's flaky status temporarily, you can mark it as healthy with the manual monitor. To temporarily suppress an automated monitor's contribution, use [monitor muting](README.md#muting-monitors) on that specific monitor instead.

## When to use it

- A test is flaky in ways that don't show up in pass-on-retry or threshold patterns (environment-specific failures, timing-sensitive tests)
- You want to flag a test before automated detection catches up
- You're tracking a known issue while working on a fix
