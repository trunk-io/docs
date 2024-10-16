---
description: mypy is a linter for Python
title: Trunk | How to run mypy
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

[**mypy**](https://github.com/python/mypy#readme) is a linter for Python.

You can enable the mypy linter with:

```shell
trunk check enable mypy
```
![mypy example output](/.gitbook/assets/mypy.gif)
## Auto Enabling

mypy will be auto-enabled if any of its config files are present: *`mypy.ini`, `.mypy.ini`*.

## Settings

mypy supports the following config files:
* `mypy.ini`
* `.mypy.ini`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.




## Links

- [mypy site](https://github.com/python/mypy#readme)
- mypy Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/mypy)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
