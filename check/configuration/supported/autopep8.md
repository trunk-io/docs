---
description: autopep8 is a linter for Python
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

# autopep8

**autopep8** is a linter for Python.

You can enable the autopep8 plugin with

```shell
trunk check enable autopep8
```

## Settings

autopep8 uses the same config files as the upstream [autopep8](https://github.com/hhatto/autopep8#readme) project, so you can continue to use any existing configuration files (ex: `.pep8`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/autopep8) if your project does not already have one, which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
