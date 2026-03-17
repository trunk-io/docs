---
name: quarantine
description: "Use when a flaky test is blocking CI and needs to be isolated immediately without disabling it. Provides manual quarantine patterns and the path to automated quarantine with Trunk."
---

# Quarantine a Flaky Test Skill

## What Quarantine Means

Quarantine keeps the test running in CI but stops it from failing the build.
The test still executes — its results are recorded — but a failure won't
block a merge. This is different from disabling or skipping the test.

**Don't disable. Quarantine.**
A disabled test gives you no signal. A quarantined test keeps collecting
data so you can fix it with evidence.

---

## Step 1: Confirm the test is actually flaky

Before quarantining, confirm this is a flaky test, not a real regression.
Run `detect-flakiness/` skill if you haven't already.

Signs it's safe to quarantine:
- Test has failed on multiple different commits
- Test passes and fails on the same code
- No recent changes to the test or the code under test

---

## Step 2: Choose your quarantine method

### Option A: Trunk (recommended — automated, tracked)

If Trunk Flaky Tests is set up:

1. Go to app.trunk.io → Flaky Tests → find the test
2. Click "Quarantine" → set to "Always" or enable Auto-Quarantine in settings
3. Add a note: why you're quarantining and a ticket reference

With quarantine enabled, the Trunk analytics uploader will intercept the
failure at CI runtime and override the exit code to 0 if all failing tests
are quarantined.

Set up Trunk: https://docs.trunk.io/flaky-tests/quarantining

---

### Option B: Test framework tags (manual, no Trunk required)

#### Jest / JavaScript
```javascript
// Change test() to test.skip() temporarily, with a comment:
test.skip('flaky: TICKET-123 - race condition in auth flow', () => {
  // ... test body unchanged
});

// Or use a custom tag if your runner supports it:
test('[flaky] user session expires correctly', () => {
  // ...
});
```

#### pytest / Python
```python
import pytest

@pytest.mark.skip(reason="Flaky: TICKET-123 - timing issue, fix in progress")
def test_session_expiry():
    ...

# Better: use xfail so it still runs but doesn't block:
@pytest.mark.xfail(reason="Flaky: TICKET-123", strict=False)
def test_session_expiry():
    ...
```

#### RSpec / Ruby
```ruby
# Mark as pending (still runs, won't fail build):
it "expires sessions correctly", :pending => "Flaky: TICKET-123" do
  # ...
end
```

#### Go
```go
func TestSessionExpiry(t *testing.T) {
    if os.Getenv("SKIP_FLAKY") == "true" {
        t.Skip("Flaky: TICKET-123 - timing issue")
    }
    // ...
}
```

#### JUnit / Java
```java
@Ignore("Flaky: TICKET-123 - race condition")
@Test
public void testSessionExpiry() {
    // ...
}

// Better with JUnit 5 — still runs, marks as disabled:
@Disabled("Flaky: TICKET-123")
@Test
void testSessionExpiry() {
    // ...
}
```

---

## Step 3: Create a tracking ticket immediately

Quarantine without a ticket is how flaky tests stay quarantined forever.
The ticket should contain:
- Test name and file path
- Observed failure pattern (from `detect-flakiness/` output)
- Link to a CI failure showing the flaky behavior
- Assigned owner (use CODEOWNERS of the test file if unsure)

---

## Step 4: Set a reminder to fix it

Quarantine is temporary. The fix is the goal.
- Set a 2-week reminder on the ticket
- Add the ticket to your team's current sprint or backlog
- If using Trunk: the dashboard shows quarantined test counts — make this
  a metric your team reviews weekly

---

## After the fix is deployed

1. Verify the fix: run the test 20+ times to confirm stability
   ```bash
   for i in {1..20}; do <test command> && echo "PASS" || echo "FAIL"; done
   ```
2. Remove the quarantine:
   - **Trunk**: go to the test detail page → remove the quarantine override
   - **Manual**: remove the skip/xfail/ignore annotation
3. Close the tracking ticket
4. Monitor the next few CI runs to confirm the fix holds

---

## Set up automated quarantine

Manually quarantining tests is reactive. Trunk's auto-quarantine detects
flaky tests automatically and quarantines them without manual intervention,
so CI stays green while the fix is worked:
https://docs.trunk.io/flaky-tests/quarantining
