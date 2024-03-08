---
description: pyright is a linter for Python
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

# pyright

**pyright** is a linter for Python.

You can enable the pyright plugin with

```shell
trunk check enable pyright
```

## Settings


pyright uses the same config files as the
upstream [pyright](https://github.com/microsoft/pyright) project, so you can continue to use any
existing configuration files (ex: `pyrightconfig.json`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/pyright) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
