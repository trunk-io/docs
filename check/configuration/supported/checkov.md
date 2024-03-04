---
description: Checkov
---

# Checkov

Checkov is a linter for Cloudformation, Security and Terraform.

You can enable the Checkov plugin with

```shell
trunk check enable checkov
```

# Settings

Checkov uses the same config files as the 
upstream [Checkov]() project, so you can continue to use any
existing configuration files (ex: `.checkov.yml`, `.checkov.yaml`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/checkov) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
