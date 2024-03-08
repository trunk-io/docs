---
description: sourcery is a linter for Python
title: Trunk | How to run sourcery
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

# sourcery

**sourcery** is a linter for Python.

You can enable the sourcery plugin with

```shell
trunk check enable sourcery
```

## Settings


**sourcery** uses the same config files as the
upstream [sourcery](https://sourcery.ai/) project, so you can continue to use any
existing configuration files (ex: `.sourcery.yaml`, `sourcery.yaml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/sourcery) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
