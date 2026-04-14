---
title: Stable branches hint
---

{% hint style="danger" %}
It is important to upload test results from CI runs on [**stable branches**](../../flaky-tests/detection/), such as `main`, `master`, or `develop`. This will give you a stronger signal about the health of your code and tests.

Trunk can also detect test flakes on PR and merge branches. To best detect flaky tests, it is recommended to upload test results from stable, PR, and merge branch CI runs.

[Learn more about detection](../../flaky-tests/detection/)
{% endhint %}
