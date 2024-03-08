---
description: Checkov is a static code analysis tool for scanning infrastructure as code. It identifies misconfigurations in IaC files that could lead to security breaches.
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

**Checkov** is a linter for Cloudformation, Security, Terraform and Docker.

You can enable the Checkov plugin with

```shell
trunk check enable checkov
```

## Settings


Checkov uses the same config files as the
upstream [Checkov](https://github.com/bridgecrewio/checkov) project, so you can continue to use any
existing configuration files (ex: `.checkov.yml`, `.checkov.yaml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/checkov) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
