---
description: Discover Ruff, a speedy Python linter for large codebases. Integrates with CI/IDEs and supports .py, .pyi, and Jupyter Notebooks.
title: Trunk | How to run Ruff
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

# Ruff

[**Ruff**](https://github.com/astral-sh/ruff) is a linter for Python.

You can enable the Ruff linter with:

```shell
trunk check enable ruff
```

## Settings

**Ruff** uses the same config files as the
upstream [Ruff](https://github.com/astral-sh/ruff) project, so you can continue to use any
existing configuration files (ex: `ruff.toml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/ruff) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [Ruff site](https://github.com/astral-sh/ruff)
* Ruff Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/ruff)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
