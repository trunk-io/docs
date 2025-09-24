---
title: Trunk | How to run Gitleaks
description: >-
  Explore Gitleaks, an open-source tool for identifying secrets in codebases.
  Learn about its file type support and integration with Trunk.
---

# Gitleaks

[**Gitleaks**](https://gitleaks.io/) is a linter for All.

You can enable the Gitleaks linter with:

```shell
trunk check enable gitleaks
```

![gitleaks example output](../../../.gitbook/assets/gitleaks.gif)

## Auto Enabling

Gitleaks will be auto-enabled if any of its config files are present: _`.gitleaks.config`, `.gitleaks.toml`, `.gitleaksignore`_.

## Settings

Gitleaks supports the following config files:

- `.gitleaks.config`
- `.gitleaks.toml`
- `.gitleaksignore`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.

## Usage Notes

Gitleaks v7 only works with Go 1.16, not Go 1.18 while Gitleaks v8 works with 1.18. We recommend using v8, but if you specifically need to use v7 you can override the go runtime version like so:

```yaml
runtimes:
  enabled:
    - go@1.16.7
```

Again, this is not recommended. Just use Gitleaks v8 or later with go 1.18 or later.

## Links

- [Gitleaks site](https://gitleaks.io/)
- Gitleaks Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/gitleaks)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
