---
description: Checkov is a static code analysis tool for scanning infrastructure as code. It identifies misconfigurations in IaC files that could lead to security breaches.
title: Trunk | How to run Checkov
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

# Checkov

[**Checkov**](https://github.com/bridgecrewio/checkov) is a linter for Cloudformation, Security, Terraform and Docker.

You can enable the Checkov linter with:

```shell
trunk check enable checkov
```

## Auto Enabling

Checkov will be auto-enabled if any of the following filetypes are present: *terraform, cloudformation, docker, yaml, json*

## Settings

Checkov supports the following config files:
* `.checkov.yml`
* `.checkov.yaml`

 You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.



## Links

- [Checkov site](https://github.com/bridgecrewio/checkov)
- Checkov Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/checkov)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
