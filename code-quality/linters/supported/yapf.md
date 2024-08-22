---
description: yapf is a linter for Python
title: Trunk | How to run yapf
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

# yapf

[**yapf**](https://github.com/google/yapf#readme) is a linter for Python.

You can enable the yapf linter with:

```shell
trunk check enable yapf
```

## Auto Enabling

yapf will be auto-enabled if any of its config files are present: *`.style.yapf`, `.yapfignore`*.

## Settings

yapf supports the following config files:
* `.style.yapf`
* `.yapfignore`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [yapf site](https://github.com/google/yapf#readme)
- yapf Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/yapf)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
