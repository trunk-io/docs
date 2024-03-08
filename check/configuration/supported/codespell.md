---
description: codespell is a linter for All
title: Trunk | How to run codespell
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

# codespell

**codespell** is a linter for All.

You can enable the codespell plugin with

```shell
trunk check enable codespell
```

## Settings


**codespell** uses the same config files as the
upstream [codespell](https://github.com/codespell-project/codespell#readme) project, so you can continue to use any
existing configuration files (ex: `.codespellrc`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/codespell) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
