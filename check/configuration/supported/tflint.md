---
description: tflint is a linter for Terraform
---

**tflint** is a linter for Terraform.

You can enable the tflint plugin with

```shell
trunk check enable tflint
```

# Settings

tflint uses the same config files as the
upstream [tflint](https://github.com/terraform-linters/tflint#readme) project, so you can continue to use any
existing configuration files (ex: `.tflint.hcl`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/tflint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
