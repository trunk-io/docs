---
description: cmake-format is a linter for C, C++
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

# cmake-format

[**cmake-format**](https://github.com/cheshirekow/cmake\_format) is a linter for C, C++.

You can enable the cmake-format linter with:

```shell
trunk check enable cmake-format
```

## Auto Enabling

cmake-format will be auto-enabled if any of its config files are present: _`.cmake-format.json`, `.cmake-format.py`, `.cmake-format.yaml`_.

## Settings

cmake-format supports the following config files:

* `.cmake-format.json`
* `.cmake-format.py`
* `.cmake-format.yaml`
* `cmake-format.json`
* `cmake-format.py`
* `cmake-format.yaml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](broken-reference) for more info.

## Links

* [cmake-format site](https://github.com/cheshirekow/cmake\_format)
* cmake-format Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/cmake-format)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
