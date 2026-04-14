---
title: Stale files warning
---

#### Stale files

Report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. Clean up all your results files after every upload step.
