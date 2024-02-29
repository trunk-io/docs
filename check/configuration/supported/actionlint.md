---
description: Actionlint: A Linter for Github Actions
---

# Actionlint

Actionlint is a linter for infra.

You can enable the Actionlint plugin with

```shell
trunk check enable actionlint
```

# Settings

Actionlint uses the same config files as the 
upstream [Actionlint]() project, so you can continue to use any
existing configuration files (ex: `.github/actionlint.yaml`, `.github/actionlint.yml`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/actionlint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
