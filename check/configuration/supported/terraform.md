---
description: The command line interface to Terraform is the terraform command, which accepts a variety of subcommands such as terraform validate or terraform fmt
title: Trunk | How to run Terraform
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

# Terraform

**Terraform** is a formatter for Terraform.

You can enable the Terraform plugin with

```shell
trunk check enable terraform
```

## Settings



Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/terraform) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).

We currently support `terraform validate` and `terraform fmt`, but only `fmt` is enabled by default when you add `terraform` to your enabled list in `trunk.yaml`. To enable `validate`, add this to your `trunk.yaml`:

```yaml
lint:
  enabled:
    - terraform@<version>:
        commands: [validate, fmt]
```
Note: you must run `terraform init` before running `trunk check` with `terraform validate` enabled (both locally, or on CI).



