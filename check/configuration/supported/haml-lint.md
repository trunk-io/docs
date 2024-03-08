---
description: haml-lint is a linter for HAML
title: Trunk | How to run haml-lint
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

# haml-lint

**haml-lint** is a linter for HAML.

You can enable the haml-lint plugin with

```shell
trunk check enable haml-lint
```

## Settings


**haml-lint** uses the same config files as the
upstream [haml-lint](https://github.com/sds/haml-lint#readme) project, so you can continue to use any
existing configuration files (ex: `.haml-lint.yml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/haml-lint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
