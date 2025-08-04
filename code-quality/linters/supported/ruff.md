---
title: Trunk | How to run Ruff
description: >-
  Discover Ruff, a speedy Python linter for large codebases. Integrates with
  CI/IDEs and supports .py, .pyi, and Jupyter Notebooks.
---

# Ruff

[**Ruff**](https://github.com/astral-sh/ruff) is a linter for Python.

ruff is composed of several linter commands.

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

Ruff will be auto-enabled if any _Python, Python-interface, Jupyter, Python, Python-interface, Python, Python-interface, Python, Python-interface, Python or Python-interface_ files are present.

## Settings

Ruff supports the following config files:

* `ruff.toml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info. Trunk Code Quality provides a default `ruff.toml` if your project does not already have one.

## Links

* [Ruff site](https://github.com/astral-sh/ruff)
* Ruff Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/ruff)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
