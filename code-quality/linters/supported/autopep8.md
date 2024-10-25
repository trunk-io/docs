---
description: Autopep8 automatically formats Python code to meet PEP 8 standards, using pycodestyle to identify and correct formatting issues for cleaner code.









title: Trunk | How to run Autopep8
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

# Autopep8

[**Autopep8**](https://github.com/hhatto/autopep8#readme) is a formatter for Python.

You can enable the Autopep8 formatter with:

```shell
trunk check enable autopep8
```
![autopep8 example output](/.gitbook/assets/autopep8.gif)
## Auto Enabling

Autopep8 will be auto-enabled if a `.pep8` config file is present.

## Settings

Autopep8 supports the following config files:
* `.pep8`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.





asdfasdf



## Links

- [Autopep8 site](https://github.com/hhatto/autopep8#readme)
- Autopep8 Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/autopep8)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
