---
description: isort is a Python utility for sorting imports alphabetically and automatically separating them into sections and by type. 
title: Trunk | How to run isort
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

# isort

[**isort**](https://pycqa.github.io/isort/) is a formatter for Python.

You can enable the isort formatter with:

```shell
trunk check enable isort
```

## Auto Enabling

isort will be auto-enabled if any of the following filetypes are present: *python*

## Settings

isort supports the following config files:
* `.isort.cfg`

 You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.Trunk check provides a default `.isort.cfg` if your project does not already have one.



## Links

- [isort site](https://pycqa.github.io/isort/)
- isort Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/isort)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
