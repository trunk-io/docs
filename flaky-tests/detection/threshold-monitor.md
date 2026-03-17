---
description: Detect flaky or broken tests based on failure rate over a configurable time window
---

# Threshold Monitor

The threshold monitor detects tests based on failure rate over a rolling time window. Unlike pass-on-retry, which looks for a specific pattern on a single commit, the threshold monitor identifies tests that fail too often over a period of time, even if no individual failure looks like a retry.

You can create multiple threshold monitors with different configurations. This is how you tailor detection to different branches, test volumes, sensitivity levels, and detection types.

## Detection Type

Each threshold monitor has a **detection type** — either **flaky** or **broken** — which controls what status a test receives when the monitor flags it:

- **Flaky monitors** catch tests that fail intermittently (e.g., 20–50% failure rate). These are typically caused by timing issues, shared state, or non-deterministic behavior.
- **Broken monitors** catch tests that fail consistently at a high rate (e.g., 80%+ failure rate). These usually indicate a real regression — something in the code or environment is genuinely broken and needs a fix.

The detection type is set at creation and cannot be changed afterward. If you need to switch a monitor's type, create a new monitor with the desired type and disable the old one.

This distinction matters because the two problems call for different responses. Flaky tests might be quarantined while you investigate the root cause. Broken tests represent real failures that should be fixed, not hidden.

## How It Works

The monitor periodically calculates the failure rate for each test within a time window you define. If the rate meets or exceeds your activation threshold and the test has enough runs to be statistically meaningful, the test is flagged as flaky or broken depending on the monitor's detection type.

### Example

You configure a threshold monitor with:
- Detection type: Flaky
- Activation threshold: 30%
- Window: 6 hours
- Minimum sample size: 50 runs
- Branches: `main`

Over the last 6 hours, `test_checkout` ran 120 times on `main` and failed 42 times (35% failure rate). Since 35% exceeds the 30% threshold and 120 runs exceeds the 50-run minimum, the test is flagged as flaky.

Meanwhile, `test_signup` ran 8 times with 3 failures (37.5%). Even though the failure rate is above 30%, the test is **not** flagged because it hasn't reached the 50-run minimum sample size. The monitor needs enough data before making a call.

## Configuration

<!-- SCREENSHOT: Threshold monitor creation form.
Show the full creation form with all fields visible: detection type, name,
activation threshold, resolution threshold, window duration, minimum sample size,
stale timeout, and branch scope. Capture it with realistic example values filled
in (e.g., "Broken on main", Broken detection type, 80% activation, 60% resolution,
6 hour window, 50 min sample, main branch). -->

### Detection Type

Choose **Flaky** or **Broken**. This determines the status a test receives when the monitor flags it. See [Detection Type](#detection-type) above for guidance on which to use.

### Activation Threshold

The failure rate that triggers detection, expressed as a percentage. A test is flagged when its failure rate meets or exceeds this value within the time window.

For flaky monitors, setting this lower (e.g., 10%) catches more intermittent failures but may produce false positives. Setting it higher (e.g., 50%) is more conservative and only flags tests that fail frequently.

For broken monitors, a high threshold (e.g., 80–100%) is appropriate — you want to catch tests that are consistently failing, not ones with occasional failures.

### Resolution Threshold

The failure rate a test must drop below to be resolved. If not set, it defaults to the activation threshold, meaning a test resolves as soon as its failure rate drops below the activation level.

Setting this lower than the activation threshold creates a buffer that prevents tests from flapping between flagged and resolved. For example, if you activate at 30% and resolve at 15%, a test flagged at 30% must improve to below 15% before it's marked healthy again. A test hovering at 20% failure rate stays flagged rather than flipping back and forth.

```mermaid
graph LR
    subgraph " "
        direction LR
        H["Healthy"] -- "Failure rate ≥ 30%\n(activation threshold)" --> F["Flaky"]
        F -- "Failure rate < 15%\n(resolution threshold)" --> H
    end

    style H fill:#dcfce7,stroke:#16a34a,color:#166534
    style F fill:#fee2e2,stroke:#dc2626,color:#991b1b
```

The gap between activation (30%) and resolution (15%) is the buffer zone. A test with a failure rate in this range keeps its current status: a healthy test won't be flagged, but a test already flagged won't be resolved either.

### Window Duration

The rolling time window (in hours) over which failure rate is calculated. Only test runs within this window are considered.

A shorter window (e.g., 1 hour) reacts quickly to recent failures but may miss patterns that play out over longer periods. A longer window (e.g., 24 hours) smooths out short-term spikes and gives a more stable picture, but takes longer to detect new issues and longer to resolve.

### Minimum Sample Size

The minimum number of test runs required within the time window before the monitor will evaluate a test. Tests with fewer runs are skipped entirely. They won't be flagged or resolved until enough data accumulates.

This prevents the monitor from making decisions on insufficient data. A test that ran 3 times with 2 failures is a 66% failure rate, but that's not enough data to be confident. Setting a reasonable minimum (e.g., 20 to 50 runs) ensures the failure rate is meaningful.

The right minimum depends on your test volume. If your tests run hundreds of times per day, a minimum of 50 to 100 is reasonable. If tests only run a few times per day, you may need a lower minimum, but keep in mind that lower minimums mean less statistical confidence.

### Stale Timeout

How long (in hours) a flagged test can go without any runs before it's automatically resolved as stale. This clears out tests that have been deleted, renamed, or are no longer part of your test suite.

When not set, flagged tests remain in their detected state indefinitely until they run enough times to recover through the normal threshold check. Setting a stale timeout (e.g., 24 hours) ensures abandoned tests don't clutter your test list.

A test resolved as stale is simply no longer being tracked by this monitor. If the test starts running again and exceeds the activation threshold, it will be re-flagged.

### Branch Scope

Which branches the monitor evaluates. You can specify up to 10 branch patterns. Only test runs on matching branches are included in the failure rate calculation.

#### Branch Pattern Syntax

Branch patterns use glob-style matching with two special characters:

| Character | Meaning | Regex equivalent |
|---|---|---|
| `*` | Zero or more of any character, including `/` | `.*` |
| `?` | Exactly one of any character | `.` |

All other characters are matched literally. Special regex characters (like `.`, `+`, `(`, `)`, `[`, `]`) are treated as literal characters in patterns, not as regex operators. You don't need to escape them.

{% hint style="info" %}
Unlike some glob implementations, `*` matches across `/` separators. The pattern `feature/*` matches both `feature/login` and `feature/api/auth`.
{% endhint %}

#### Pattern Examples

| Pattern | Matches | Does not match |
|---|---|---|
| `main` | `main` | `main-v2`, `maint` |
| `feature/*` | `feature/login`, `feature/api/auth` | `feature` (no trailing path), `features/x` |
| `release-?.?.?` | `release-1.2.3` | `release-10.2.3` (10 is two characters), `release-1.2` |
| `*-hotfix` | `prod-hotfix`, `release/v1-hotfix` | `hotfix`, `hotfix-1` |
| `*` | All branches | |

A pattern with no special characters matches that exact branch name only. For example, `main` matches the branch named `main` and nothing else.

#### Stable Branch Patterns

For your main or stable branch, use the exact branch name:

| Your stable branch | Pattern |
|---|---|
| `main` | `main` |
| `master` | `master` |
| `develop` | `develop` |

#### Merge Queue Branch Patterns

If you use a merge queue, your queue creates temporary branches to test changes before merging. Each merge queue product uses a different branch naming convention:

| Merge queue | Branch pattern | Example branches matched |
|---|---|---|
| Trunk Merge Queue | `trunk-merge/*` | `trunk-merge/main/1`, `trunk-merge/main/2` |
| GitHub Merge Queue | `gh-readonly-queue/*` | `gh-readonly-queue/main/pr-123-abc` |
| Graphite Merge Queue | `graphite-merge/*` | `graphite-merge/main/1` |

GitLab Merge Trains run on the target branch directly rather than creating separate branches. To monitor merge train runs, scope your monitor to the target branch (e.g., `main`).

#### Tips for Branch Scoping

- You can add up to **10 patterns** per monitor. A test run is included if its branch matches any of the patterns.
- Since patterns can't express "everything except a branch," a practical approach is to create **separate monitors**: one scoped to `main` with strict settings, and another scoped to your PR branch naming patterns (e.g., `feature/*`, `fix/*`) with more lenient settings.
- `**` is treated as two consecutive `*` wildcards, which is functionally identical to a single `*`. There is no special multi-segment matching behavior.

<!-- SCREENSHOT: Branch scope configuration.
Show the branch pattern input with a few patterns entered (e.g.,
`main` and `release/*`), ideally showing the tag/chip-style UI for
each pattern. -->

## Resolution Behavior

A flagged test resolves in one of two ways:

**Healthy recovery:** The test's failure rate drops below the resolution threshold (or activation threshold, if no resolution threshold is set) and it still has enough runs to meet the minimum sample size. This means the test is actively running and has improved.

**Stale recovery:** If a stale timeout is configured and the test has no runs on matching branches within that period, it resolves as stale. This is an automatic cleanup mechanism, not an indication that the test has improved.

Tests that are still running but haven't accumulated enough runs to meet the minimum sample size remain in their current state. They won't be resolved until there's enough data to make a determination.

## Muting

You can temporarily mute a threshold monitor for a specific test case. See [Muting monitors](README.md#muting-monitors) for details.

## Recommended Configurations

A common setup is to pair two threshold monitors — one to catch broken tests quickly and one to catch flaky tests over a longer window:

| Monitor | Detection type | Activation threshold | Window | Purpose |
|---------|---------------|---------------------|--------|---------|
| Broken on main | Broken | 80–100% | 1–6 hours | Catch tests that are reliably failing — real regressions that need immediate attention |
| Flaky on main | Flaky | 20–50% | 12–72 hours | Catch intermittently failing tests — candidates for investigation or quarantine |

You can create as many monitors as you need. For example, you might want separate monitors for your main branch and pull request branches, or different thresholds for different levels of severity. The following sections provide starting points for common scenarios.

### Main Branch: Catch Flakiness Early

Failures on your stable branch are a strong signal. Tests should be passing before code is merged, so failures here are unexpected and likely indicate flakiness.

| Setting | Suggested value | Why |
|---|---|---|
| Activation threshold | 10 to 20% | Low threshold catches subtle flakiness early |
| Resolution threshold | 5 to 10% | Requires clear improvement before resolving |
| Window | 6 to 24 hours | Long enough to accumulate data, short enough to catch new issues |
| Min sample size | 20 to 50 | Depends on how often your tests run on main |
| Branches | `main` (or `master`, `develop`, etc.) | Use the exact name of your stable branch |

### Pull Requests: Flag Severe Flakiness Only

PR branches see a lot of churn. Tests fail for legitimate reasons during development, so you want a higher bar before flagging something as flaky here. Focus on tests that are failing at a rate that clearly isn't caused by code changes.

| Setting | Suggested value | Why |
|---|---|---|
| Activation threshold | 40 to 60% | High threshold avoids false positives from expected PR failures |
| Resolution threshold | 20 to 30% | Wide buffer prevents flapping |
| Window | 12 to 24 hours | Longer window smooths out short-lived development failures |
| Min sample size | 30 to 100 | Higher minimum avoids flagging tests that only ran a few times on PRs |
| Branches | `feature/*`, `fix/*`, `dependabot/*` | Match your team's PR branch naming conventions |

Since branch patterns can't express "everything except main," create one monitor scoped to `main` with strict settings and a second monitor scoped to your PR branch naming patterns with more lenient settings.

### Merge Queue: Strict Monitoring

Merge queue branches test code that has already passed PR checks. Failures here are suspicious. If you use a merge queue, consider a dedicated monitor with settings similar to or stricter than your main branch monitor.

| Setting | Suggested value | Why |
|---|---|---|
| Activation threshold | 10 to 15% | Low threshold, failures here are unexpected |
| Resolution threshold | 5% | Strict recovery |
| Window | 6 to 12 hours | Shorter window for faster detection |
| Min sample size | 10 to 20 | Merge queues may have fewer total test runs |
| Branches | `trunk-merge/*` or `gh-readonly-queue/*` | Use the pattern for your merge queue provider (see table above) |

### Other Patterns

- **Release branches:** A monitor scoped to `release/*` with strict thresholds catches flakiness before it ships.
- **Nightly or scheduled builds:** If you run comprehensive test suites on a schedule, a monitor with a longer window and higher minimum sample size can catch slow-burn flakiness that doesn't show up in faster CI runs.

<!-- SCREENSHOT: Monitor overview page with multiple threshold monitors.
Show the monitors list/card view with two or three configured threshold
monitors visible (e.g., "Broken on main", "Flaky on main", "Merge queue"),
displaying their key settings at a glance (detection type, threshold,
window, branch scope). Include the pass-on-retry monitor card as well
to show the full picture. -->

## FAQ

**What's the difference between a flaky test and a broken test?**

A flaky test fails intermittently — it sometimes passes and sometimes fails on the same code. A broken test fails consistently at a high rate because something in the code or environment is genuinely broken. Trunk lets you set different thresholds for each so you can respond to them differently.

**Can I change a monitor's detection type after creating it?**

No. The detection type is set at creation and cannot be changed. To switch, create a new monitor with the desired type and disable the old one.

**What happens to my existing monitors?**

Nothing changes. All existing threshold monitors default to the flaky detection type and continue to behave exactly as before. The broken detection type is opt-in — you only get it by creating a new monitor with that type selected.

**What should I do when a test is marked as Broken?**

Investigate and fix the underlying failure. A broken status means the test is consistently failing, which usually points to a real bug or regression. Once the failure rate drops below the resolution threshold (or the activation threshold, if no resolution threshold is configured), the monitor automatically resolves.

**Can a test be both flaky and broken?**

A test can be detected by both flaky and broken monitors at the same time, but it only shows one status. Broken takes priority — if any broken monitor is active, the test shows as Broken. When the broken monitor resolves, it may show as Flaky if a flaky monitor is still active.

**Can I have multiple broken monitors for the same repo?**

Yes. You can create multiple monitors with different configurations — for example, one scoped to your main branch and another for pull requests, or monitors with different thresholds for different levels of severity.

**What does the resolution threshold do?**

It adds hysteresis to prevent flapping. Without it, a test whose failure rate hovers right around the activation threshold will rapidly toggle between flagged and resolved. With a resolution threshold set lower than the activation threshold, the test must drop below the resolution threshold before it resolves — creating a stable buffer zone.

**What does the stale timeout do?**

It automatically resolves the monitor for tests that haven't run within the specified time period. This is useful for tests that have been deleted, renamed, or moved to a different suite — without it, those tests would stay flagged indefinitely.
