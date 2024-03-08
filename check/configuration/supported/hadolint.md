---
description: hadolint is a linter for Docker
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

# hadolint

**hadolint** is a linter for Docker.

You can enable the hadolint plugin with

```shell
trunk check enable hadolint
```

## Settings


hadolint uses the same config files as the
upstream [hadolint](https://github.com/hadolint/hadolint#readme) project, so you can continue to use any
existing configuration files (ex: `.hadolint.yaml`, `.hadolint.yml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/hadolint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
