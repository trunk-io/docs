---
description: Terraform CLI
---

# Terraform

Terraform is a formatter for infra.

You can enable the Terraform plugin with

```shell
trunk check enable terraform
```

# Settings

Terraform uses the same config files as the 
upstream [Terraform](https://developer.hashicorp.com/terraform/cli/commands) project, so you can continue to use any
existing configuration files (ex: ${direct_configs}).

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



