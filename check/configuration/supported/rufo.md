---
description: rufo is a linter for Ruby
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

# rufo

**rufo** is a linter for Ruby.

You can enable the rufo plugin with

```shell
trunk check enable rufo
```

## Settings


rufo uses the same config files as the
upstream [rufo](https://github.com/ruby-formatter/rufo#readme) project, so you can continue to use any
existing configuration files (ex: `.rufo`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/rufo) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
