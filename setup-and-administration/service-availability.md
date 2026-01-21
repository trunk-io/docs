# Service Availability

### Service Availability and Graceful Degradation

Trunk's CLI is designed to fail safe when our quarantine service is unavailable. Your CI pipeline's integrity is never compromised by Trunk outages.

#### What happens if Trunk is unreachable?

When the CLI cannot fetch quarantine configuration from Trunk's API:



1. **Your original test exit code is preserved** — if tests fail, your CI fails
2. **No tests are quarantined** — failed tests are reported as failures, not suppressed
3. **A warning is displayed** in the CLI output:

> We were unable to determine the quarantine status for tests. Any failing tests will be reported as failures.

#### Why fail-safe?

We prioritize avoiding false positives over convenience. If Trunk is down, we'd rather your CI fails on a flaky test than silently passes on a real regression. You can always re-run the job once connectivity is restored.

#### What this means for you

| Scenario                             | CI Exit Code    | Tests Quarantined |
| ------------------------------------ | --------------- | ----------------- |
| API available, tests quarantined     | 0 (pass)        | Yes               |
| API available, tests not quarantined | Non-zero (fail) | No                |
| API unavailable                      | Non-zero (fail) | No                |

#### Caching behavior

The CLI does not cache quarantine configuration locally. Each invocation requires a successful API call to apply quarantining. This ensures you're always operating on the freshest quarantine state rather than potentially stale data.
