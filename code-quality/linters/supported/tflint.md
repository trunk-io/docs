---
description: tflint is a linter for Terraform
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

# tflint

[**tflint**](https://github.com/terraform-linters/tflint#readme) is a linter for Terraform.

You can enable the tflint linter with:

```shell
trunk check enable tflint
```

## Auto Enabling

tflint will be auto-enabled if any _Terraform_ files are present.

## Settings

tflint supports the following config files:

* `.tflint.hcl`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](broken-reference) for more info.

## Links

* [tflint site](https://github.com/terraform-linters/tflint#readme)
* tflint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/tflint)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
