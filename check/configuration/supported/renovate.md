---
description: renovate is a linter for Renovate
title: Trunk | How to run renovate
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

# renovate

**renovate** is a linter for Renovate.

You can enable the renovate plugin with

```shell
trunk check enable renovate
```

## Settings


**renovate** uses the same config files as the
upstream [renovate](https://github.com/renovatebot/renovate#readme) project, so you can continue to use any
existing configuration files (ex: `renovate.json`, `renovate.json5`, `.github/renovate.json`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/renovate) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
