---
description: Discover Ruff, a speedy Python linter for large codebases. Integrates with CI/IDEs and supports .py, .pyi, and Jupyter Notebooks.
---

**Ruff** is a linter for Python.

You can enable the Ruff plugin with

```shell
trunk check enable ruff
```

# Settings

Ruff uses the same config files as the 
upstream [Ruff](https://github.com/astral-sh/ruff) project, so you can continue to use any
existing configuration files (ex: `ruff.toml`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/ruff) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
