---
description: hadolint is a linter for Docker
title: Trunk | How to run hadolint
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

# hadolint

[**hadolint**](https://github.com/hadolint/hadolint#readme) is a linter for Docker.

You can enable the hadolint linter with:

```shell
trunk check enable hadolint
```

## Auto Enabling

hadolint will be auto-enabled if any *Docker* files are present.

## Settings

hadolint supports the following config files:
* `.hadolint.yaml`
* `.hadolint.yml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.
Trunk check provides a default `.hadolint.yaml` if your project does not already have one.



## Links

- [hadolint site](https://github.com/hadolint/hadolint#readme)
- hadolint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/hadolint)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
