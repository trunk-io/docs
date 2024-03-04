---
description: Bandit- A Security Linter for Python 
---

# Bandit

Bandit is a linter for Python.

You can enable the Bandit plugin with

```shell
trunk check enable bandit
```

# Settings

Bandit uses the same config files as the 
upstream [Bandit](https://github.com/PyCQA/bandit) project, so you can continue to use any
existing configuration files (ex: `.bandit`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/bandit) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
