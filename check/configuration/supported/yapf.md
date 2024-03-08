---
description: yapf is a linter for Python
title: Trunk | How to run yapf
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

# yapf

**yapf** is a linter for Python.

You can enable the yapf plugin with

```shell
trunk check enable yapf
```

## Settings


**yapf** uses the same config files as the
upstream [yapf](https://github.com/google/yapf#readme) project, so you can continue to use any
existing configuration files (ex: `.style.yapf`, `.yapfignore`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/yapf) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
