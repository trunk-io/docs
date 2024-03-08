---
description: cmake-format is a linter for C, C++
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

# cmake-format

**cmake-format** is a linter for C, C++.

You can enable the cmake-format plugin with

```shell
trunk check enable cmake-format
```

## Settings


cmake-format uses the same config files as the
upstream [cmake-format](https://github.com/cheshirekow/cmake_format) project, so you can continue to use any
existing configuration files (ex: `.cmake-format.json`, `.cmake-format.py`, `.cmake-format.yaml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/cmake-format) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
