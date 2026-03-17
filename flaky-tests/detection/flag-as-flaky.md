---
description: Manually mark a test as flaky from the test detail page
---

# Flag as Flaky

Manually mark a test as flaky when you know it's unreliable but automated monitors haven't detected it yet — or when you want to override the system's assessment.

## When to Use It

- A test is intermittently failing but hasn't been flagged by threshold or pass-on-retry monitors.
- You want to immediately quarantine a test while investigating.
- You've identified a flaky test through code review or local observation.

## How It Works

### Flagging a Test

1. Navigate to the test detail page for the test you want to flag.
2. Click the **Flag as Flaky** button in the header row, next to the status badge.
3. In the popover that appears, optionally add a reason (up to 256 characters) explaining why you're flagging it.
4. Click **Flag** to confirm.

Once flagged:

- The test is immediately marked as **flaky**, regardless of what automated monitors report.
- An amber banner appears below the header showing who flagged it, when, and the reason (if provided).
- The flag is additive — if automated monitors later detect the test as flaky too, both signals coexist.

### Removing the Flag

1. On the test detail page, find the amber "Manually flagged as flaky" banner.
2. Click the **Remove flag** button on the right side of the banner.
3. Confirm by clicking **Remove flag** in the popover.

After removing:

- The test's status reverts to whatever the automated monitors determine.
- If monitors are still detecting the test as flaky, it remains flaky. The flag removal only clears the manual override.

## Relationship to Monitors

The "Flag as Flaky" action is independent of automated monitors (threshold-based, pass-on-retry). It does not appear in the Monitors tab.

| Scenario                            | Test status              |
| ----------------------------------- | ------------------------ |
| No monitors active, no flag         | Healthy                  |
| Monitors active, no flag            | Flaky (detected)         |
| No monitors active, flag set        | Flaky (manually flagged) |
| Monitors active, flag set           | Flaky (both)             |
| Flag removed, monitors still active | Flaky (detected)         |
| Flag removed, monitors inactive     | Healthy                  |

## Flag History

All flag and unflag actions are recorded as events. You can view the history by opening the Flag History panel from the test detail page. Each entry shows who performed the action, when, and the reason (if one was provided).

