---
title: Trunk | How to run TFLint
description: >-
  TFLint is an essential linter designed for Terraform. It helps improve code
  quality, maintainability, and security in infrastructure as code (IaC)
  projects.
---

# TFLint

[**TFLint**](https://github.com/rhysd/actionlint) is a linter for Terraform.

You can enable the TFLint linter with:

```shell
trunk check enable tflint
```

## Auto Enabling

TFLint will be auto-enabled if any _Terraform_ files are present.

## Settings

TFLint supports the following config files:

* `.tflint.hcl`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.

## Links

* [TFLint site](https://github.com/rhysd/actionlint)
* TFLint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/tflint)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
