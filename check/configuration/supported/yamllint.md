---
description: Yamllint is a linter that checks for formatting discrepancies, key-value pair issues, and syntax errors, ensuring your YAML files are syntactically correct. 
title: Trunk | How to run Yamllint
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

# Yamllint

[**Yamllint**](https://github.com/adrienverge/yamllint) is a linter for YAML.

You can enable the Yamllint linter with:

```shell
trunk check enable yamllint
```

## Settings

**Yamllint** uses the same config files as the
upstream [Yamllint](https://github.com/adrienverge/yamllint) project, so you can continue to use any
existing configuration files (ex: `.yamllint`, `.yamllint.yaml`, `.yamllint.yml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/yamllint) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [Yamllint site](https://github.com/adrienverge/yamllint)
* Yamllint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/yamllint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
