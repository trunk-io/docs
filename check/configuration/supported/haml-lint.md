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

[**haml-lint**](https://github.com/sds/haml-lint#readme) is a linter for HAML.

You can enable the haml-lint linter with:

```shell
trunk check enable haml-lint
```

## Settings

**haml-lint** uses the same config files as the
upstream [haml-lint](https://github.com/sds/haml-lint#readme) project, so you can continue to use any
existing configuration files (ex: `.haml-lint.yml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/haml-lint) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [haml-lint site](https://github.com/sds/haml-lint#readme)
* haml-lint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/haml-lint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
