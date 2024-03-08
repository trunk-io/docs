---
description: Explore Gitleaks, an open-source tool for identifying secrets in codebases. Learn about its file type support and integration with Trunk.
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Gitleaks

**Gitleaks** is a linter for All.

You can enable the Gitleaks plugin with

```shell
trunk check enable gitleaks
```

## Settings


Gitleaks uses the same config files as the
upstream [Gitleaks](https://gitleaks.io/) project, so you can continue to use any
existing configuration files (ex: `.gitleaks.config`, `.gitleaks.toml`, `.gitleaksignore`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/gitleaks) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).

Gitleaks v7 only works with Go 1.16, not Go 1.18 while Gitleaks v8 works with 1.18. We recommend using v8, but if you specifically need to use v7 you can override the go runtime version like so:

```yaml
yaruntimes:
  enabled:
    - go@1.16.7
```
Again, this is not recommended. Just use Gitleaks v8 or later with go 1.18 or later.

