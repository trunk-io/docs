---
description: rubocop is a linter for Ruby
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

# rubocop

**rubocop** is a linter for Ruby.

You can enable the rubocop plugin with

```shell
trunk check enable rubocop
```

## Settings


rubocop uses the same config files as the
upstream [rubocop](https://github.com/rubocop/rubocop#readme) project, so you can continue to use any
existing configuration files (ex: `.rubocop.yml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/rubocop) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
