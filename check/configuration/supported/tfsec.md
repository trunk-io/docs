---
description: tfsec is a linter for Terraform
---

**tfsec** is a linter for Terraform.

You can enable the tfsec plugin with

```shell
trunk check enable tfsec
```

# Settings

tfsec uses the same config files as the
upstream [tfsec](https://github.com/aquasecurity/tfsec) project, so you can continue to use any
existing configuration files (ex: `tfsec.yml`, `tfsec.yaml`, `.tfsec/config.json`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/tfsec) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
