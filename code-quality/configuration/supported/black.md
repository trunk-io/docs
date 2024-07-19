---
title: Trunk | How to run Black
description: >-
  Discover Black, the Python code formatter.  Learn how to integrate it with
  Trunk Check for seamless coding style enforcement.
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

# Black

[**Black**](https://pypi.org/project/black/) is a formatter for Python.

You can enable the Black formatter with:

```shell
trunk check enable black
```

![black example output](../../../check/configuration/supported/black.gif)

## Auto Enabling

Black will be auto-enabled if any _Python, Jupyter or Python-interface_ files are present.

## Links

* [Black site](https://pypi.org/project/black/)
* Black Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/black)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
