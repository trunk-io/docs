---
description: gokart is a linter for Go
title: Trunk | How to run gokart
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

# gokart

**gokart** is a linter for Go.

You can enable the gokart plugin with

```shell
trunk check enable gokart
```

## Settings


**gokart** uses the same config files as the
upstream [gokart](https://github.com/praetorian-inc/gokart) project, so you can continue to use any
existing configuration files (ex: `analyzers.yml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/gokart) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
