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


The `ruff` linter actually has multiple linters for different purposes.
    
`ruff` is for formatting general python code.

You can enable the `ruff` linter with:

```shell
trunk check enable ruff
```
      
`ruff-nbqa` is for extra support for Jupyter notebooks.

You can enable the `ruff-nbqa` linter with:

```shell
trunk check enable ruff-nbqa
```
      




## Auto Enabling

Ruff will be auto-enabled if any *Python* files are present.

## Settings

Ruff supports the following config files:
* `ruff.toml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.
Trunk check provides a default `ruff.toml` if your project does not already have one.



## Links

- [Ruff site](https://github.com/astral-sh/ruff)
- Ruff Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/ruff)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
