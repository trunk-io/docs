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

## Settings

**yapf** uses the same config files as the
upstream [yapf](https://github.com/google/yapf#readme) project, so you can continue to use any
existing configuration files (ex: `.style.yapf`, `.yapfignore`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/yapf) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [yapf site](https://github.com/google/yapf#readme)
* yapf Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/yapf)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
