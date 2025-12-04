---
title: Trunk | How to run Terraform
description: >-
  The command line interface to Terraform is the terraform command, which
  accepts a variety of subcommands such as terraform validate or terraform fmt
---

# Terraform

[**Terraform**](https://developer.hashicorp.com/terraform/cli/commands) is a formatter for Terraform.

You can enable the Terraform formatter with:

```shell
trunk check enable terraform
```

## Auto Enabling

Terraform will never be auto-enabled. It must be enabled manually.

## Usage Notes

We currently support `terraform validate` and `terraform fmt`, but only `fmt` is enabled by default when you add `terraform` to your enabled list in `trunk.yaml`. To enable `validate`, add this to your `trunk.yaml`:

```yaml
lint:
  enabled:
    - terraform@<version>:
        commands: [validate, fmt]
```

Note: you must run `terraform init` before running `trunk check` with `terraform validate` enabled (both locally, or on CI).

## Links

* [Terraform site](https://developer.hashicorp.com/terraform/cli/commands)
* Terraform Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/terraform)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
