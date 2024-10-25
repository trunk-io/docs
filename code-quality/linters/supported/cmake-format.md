---
description: Learn how to install, configure, and run CMake-Format with Trunk Check to ensure consistent formatting and best practices for your CMake scripts.








title: Trunk | How to run cmake-format
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

[**cmake-format**](https://github.com/cheshirekow/cmake_format) is a formatter for C, C++.

You can enable the cmake-format formatter with:

```shell
trunk check enable cmake-format
```

## Auto Enabling

cmake-format will be auto-enabled if any of its config files are present: *`.cmake-format.json`, `.cmake-format.py`, `.cmake-format.yaml`*.

## Settings

cmake-format supports the following config files:
* `.cmake-format.json`
* `.cmake-format.py`
* `.cmake-format.yaml`
* `cmake-format.json`
* `cmake-format.py`
* `cmake-format.yaml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.





asdfasdf



## Links

- [cmake-format site](https://github.com/cheshirekow/cmake_format)
- cmake-format Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/cmake-format)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
