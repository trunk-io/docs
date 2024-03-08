---
description: taplo is a linter for TOML
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

# taplo

**taplo** is a linter for TOML.

You can enable the taplo plugin with

```shell
trunk check enable taplo
```

## Settings


**taplo** uses the same config files as the
upstream [taplo](https://github.com/tamasfe/taplo#readme) project, so you can continue to use any
existing configuration files (ex: `.taplo.toml`, `taplo.toml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/taplo) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
