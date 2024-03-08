---
description: mypy is a linter for Python
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

# mypy

**mypy** is a linter for Python.

You can enable the mypy plugin with

```shell
trunk check enable mypy
```

## Settings


**mypy** uses the same config files as the
upstream [mypy](https://github.com/python/mypy#readme) project, so you can continue to use any
existing configuration files (ex: `mypy.ini`, `.mypy.ini`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/mypy) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
