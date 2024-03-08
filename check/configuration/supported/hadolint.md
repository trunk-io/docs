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

## Settings

**hadolint** uses the same config files as the
upstream [hadolint](https://github.com/hadolint/hadolint#readme) project, so you can continue to use any
existing configuration files (ex: `.hadolint.yaml`, `.hadolint.yml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/hadolint) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [hadolint site](https://github.com/hadolint/hadolint#readme)
* hadolint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/hadolint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
