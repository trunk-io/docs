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

## Auto Enabling

Yamllint will be auto-enabled if any *Yaml* files are present.

## Settings

Yamllint supports the following config files:
* `.yamllint`
* `.yamllint.yaml`
* `.yamllint.yml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.
Trunk Code Quality provides a default `.yamllint.yaml` if your project does not already have one.



## Links

- [Yamllint site](https://github.com/adrienverge/yamllint)
- Yamllint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/yamllint)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
