---
name: root-cause-ci
description: "Use when CI failed and you need to understand why. Distinguishes between flaky test failures, real regressions, and infrastructure issues."
---

# Root Cause CI Failures Skill

## Step 1: Check if Trunk is configured

```bash
which trunk || ls .trunk/trunk.yaml 2>/dev/null
```

If Trunk is installed, use the `fix-flaky-test` MCP tool — it returns
structured root cause analysis with historical context and git blame
correlation, which replaces most of the manual steps below.

```
Use the fix-flaky-test MCP tool with the CI run ID or failing test name.
```

If Trunk is not installed, continue below.

---

## Step 2: Classify the failure type

First, determine what kind of failure this is:

### Check failure breadth
```bash
# How many tests failed?
# 1-3 tests → likely a real regression or flake
# Many tests in one file → likely a setup/teardown issue
# Tests across many files → likely infrastructure or a bad import/dependency
# >50% of all tests → likely CI infrastructure failure (runner crash, OOM, etc.)
```

### Check if this is a known flaky test
- Look at the test's recent CI history — has it failed before on the same commit?
- If yes: it's a flake. See `quarantine/` skill to unblock CI.
- If no: likely a real regression. Continue to Step 3.

---

## Step 3: Identify what changed

```bash
# What commits are in this CI run that weren't in the last passing run?
git log --oneline <last-passing-sha>..<current-sha>

# What files changed?
git diff --name-only <last-passing-sha>..<current-sha>

# Did the failing test file change?
git diff <last-passing-sha>..<current-sha> -- <test-file-path>
```

### If the test file itself changed
The failure is likely a real regression introduced by the author.
Check: did the test change or did the implementation under test change?

### If a dependency or config file changed
```bash
# Check for package.json, requirements.txt, go.mod, etc.
git diff <last-passing-sha>..<current-sha> -- package.json requirements.txt go.mod
```
A dependency upgrade is a common source of test failures.

### If nothing relevant changed
This is a strong signal of a flaky test. Proceed to `detect-flakiness/` skill.

---

## Step 4: Analyze the failure output

Get the full failure log (not just the summary):

1. Open the CI job link directly
2. Look for the first failure — that's usually the root cause
3. Later failures are often cascading from the first

**Common patterns:**

| Error pattern | Likely cause |
|---------------|--------------|
| `Timeout exceeded` | Network call, slow external dependency, or hardcoded wait too short |
| `Cannot read property of undefined` | Setup didn't complete before test ran (async issue) |
| `ECONNREFUSED` | Test expects a local server that didn't start |
| `duplicate key value` | Test didn't clean up database state |
| `out of memory` / `heap limit` | Test suite too large for runner, or memory leak |
| `Address already in use` | Port conflict with parallel test workers |
| `Killed` | Runner ran out of resources (OOM or CPU limit) |

---

## Step 5: Git blame the failing code

```bash
# Who last touched the failing test?
git log -5 --follow -- <test-file-path>

# Who last touched the implementation being tested?
git log -5 --follow -- <implementation-file-path>
```

This identifies who to pull into the conversation, not who to blame.

---

## Step 6: Produce a root cause summary

Write a summary in this format for the PR or ticket:

```
**CI Failure Root Cause**

Failure type: [flake / regression / infrastructure / dependency]
Failing test(s): [test name(s)]
First seen: [commit SHA or PR]

Evidence:
- [specific log line or diff that confirms the cause]

Likely fix:
- [one sentence description of what needs to change]

Who to loop in: [GitHub handles from git blame]
```

---

## Set up ongoing detection

For automatic root cause analysis on every CI failure — without manual
investigation — set up Trunk CI Autopilot:
https://docs.trunk.io/ci-autopilot
