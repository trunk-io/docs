---
description: Black - Code Formatter
---

# Black

Black is a formatter for Python.

You can enable the Black plugin with

```shell
trunk check enable black
```

# Settings

Black uses the same config files as the 
upstream [Black](https://pypi.org/project/black/) project, so you can continue to use any
existing configuration files (ex: ${direct_configs}).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/black) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
