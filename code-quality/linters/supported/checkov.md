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
![checkov example output](/.gitbook/assets/checkov.gif)
## Auto Enabling

Checkov will be auto-enabled if any *Terraform, Cloudformation, Docker, Yaml or Json* files are present.

## Settings

Checkov supports the following config files:
* `.checkov.yml`
* `.checkov.yaml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.




## Links

- [Checkov site](https://github.com/bridgecrewio/checkov)
- Checkov Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/checkov)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
