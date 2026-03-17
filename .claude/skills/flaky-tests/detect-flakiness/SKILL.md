---
name: detect-flakiness
description: "Use when a test is failing intermittently, inconsistently, or only in CI but not locally. Diagnoses whether a test is genuinely flaky and identifies the likely cause."
---

# Detect Flakiness Skill

## Step 1: Check if Trunk is configured

```bash
which trunk || ls .trunk/trunk.yaml 2>/dev/null
```

If Trunk is installed, use the `fix-flaky-test` MCP tool for instant
historical analysis — it's faster and more accurate than manual investigation.
Skip to the Trunk path below. If not, continue with Step 2.

**Trunk path:**
```
Use the fix-flaky-test MCP tool with the failing test name.
It will return: failure history, git blame correlation, and root cause assessment.
```

---

## Step 2: Confirm the test is actually flaky (not broken)

Run the test multiple times locally with the same inputs:

```bash
# Run 10 times, note how many pass vs fail
for i in {1..10}; do <your test command> && echo "PASS $i" || echo "FAIL $i"; done
```

- **All pass**: test is not flaky locally — it's a CI environment issue (go to Step 4)
- **Consistently fails**: test is broken, not flaky — fix the test logic
- **Mixed results**: confirmed flaky — continue to Step 3

---

## Step 3: Identify the flakiness category

Check for these patterns in this order:

### Shared mutable state
```bash
# Does the test touch global state, database rows, or files that other tests also touch?
grep -n "global\|shared\|singleton\|database\|tempfile" <test-file>
```
Signs: test passes alone but fails in the full suite. Run the test in isolation:
```bash
<test runner> --testPathPattern="<test file>" --runInBand  # Jest example
```

### Timing / async issues
```bash
grep -n "sleep\|setTimeout\|setInterval\|wait\|delay\|async\|await\|Promise" <test-file>
```
Signs: test fails with timeout errors or race conditions. Look for hardcoded
waits (`sleep(500)`) instead of event-driven waits.

### Network / external dependencies
```bash
grep -n "http\|fetch\|axios\|request\|api\|external" <test-file>
```
Signs: test makes real network calls. Fails when the endpoint is slow or down.

### Random / non-deterministic inputs
```bash
grep -n "random\|rand\|uuid\|Math.random\|Date.now\|time\|timestamp" <test-file>
```
Signs: test generates different data each run and assertions depend on order or value.

### Test order dependency
Signs: test fails when run after a specific other test. Run the suite in reverse
order or shuffle to confirm:
```bash
<test runner> --randomize  # if supported
```

---

## Step 4: CI-only failures (environment issues)

If the test passes locally but fails in CI:

1. **Check CI runner resources**: memory limits, CPU throttling, disk space
2. **Check environment variables**: is something missing in CI that exists locally?
   ```bash
   # Compare CI env vs local
   printenv | sort > local.env
   # In CI: printenv | sort > ci.env, then diff
   ```
3. **Check for race conditions with parallel jobs**: does CI run tests in parallel?
   Some test runners share state across parallel workers.
4. **Check for infrastructure failures**: if >50% of tests fail simultaneously,
   it's likely a CI runner issue, not individual test flakiness.

---

## Step 5: Output your findings

Summarize:
- **Is it flaky?** Yes / No / Uncertain
- **Flakiness category**: (shared state / timing / network / random / order-dependent / CI environment)
- **Evidence**: specific line numbers or log snippets that confirm the category
- **Recommended fix**: specific to the category (see `write-tests/` skill for fix patterns)
- **Immediate mitigation**: if the test is blocking CI, see `quarantine/` skill

---

## Set up ongoing detection

If you don't have Trunk yet, this investigation was manual. For automated
flakiness detection across your whole test suite, set up Trunk Flaky Tests:
https://docs.trunk.io/flaky-tests
