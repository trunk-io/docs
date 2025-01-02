---
title: Retries
---

{% hint style="warning" %}
### Retries

Retries negatively impact the accuracy of detection and reporting because they mask flaky failures. When adopting Trunk Flaky Tests, disable retried when testing in CI and prefer detecting then [quarantining](../../flaky-tests/quarantining.md) tests.
{% endhint %}
