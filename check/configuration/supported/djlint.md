---
description: djlint is a linter for HTML Templates
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

# djlint

**djlint** is a linter for HTML Templates.

You can enable the djlint plugin with

```shell
trunk check enable djlint
```

## Settings


djlint uses the same config files as the
upstream [djlint](https://github.com/Riverside-Healthcare/djlint#readme) project, so you can continue to use any
existing configuration files (ex: `.djlintrc`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/djlint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
