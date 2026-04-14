---
title: Configuring cargo-nextest
description: A guide for generating Trunk-compatible test reports for Rust
---

# cargo-nextest

You can automatically [detect and manage flaky tests](../../detection/) in your Rust projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

`cargo-nextest` has built-in reporting for JUnit XML reports, which is trunk-compatible. You can enable JUnit reporting by adding the following to your nextest config:

{% code title=".config/nextest.toml" %}
```toml
[profile.ci.junit]
path = "junit.xml"
```
{% endcode %}

You can invoke this profile when running tests with:

```sh
cargo nextest run --profile ci
```

#### Report File Path

`cargo-nextest` outputs artifacts at `target/nextest` by default. When you provide a profile and a file name via the config example above, it produces a report at `target/nextest/ci/junit.xml`.

{% include "../../../.gitbook/includes/retries.md" %}

Omit the `--retries` option.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
