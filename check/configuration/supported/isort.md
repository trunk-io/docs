---
description: Isort is a Python utility for sorting imports alphabetically and automatically separating them into sections and by type. 
---

**Isort** is a formatter for Python.

You can enable the Isort plugin with

```shell
trunk check enable isort
```

# Settings

Isort uses the same config files as the 
upstream [Isort](https://pycqa.github.io/isort/) project, so you can continue to use any
existing configuration files (ex: `.isort.cfg`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/isort) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
