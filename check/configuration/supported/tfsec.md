---
description: tfsec is a linter for Security and Terraform
title: Trunk | How to run tfsec
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

# tfsec

[**tfsec**](https://github.com/aquasecurity/tfsec) is a linter for Security and Terraform.

You can enable the tfsec linter with:

```shell
trunk check enable tfsec
```

## Settings

**tfsec** uses the same config files as the
upstream [tfsec](https://github.com/aquasecurity/tfsec) project, so you can continue to use any
existing configuration files (ex: `tfsec.yml`, `tfsec.yaml`, `.tfsec/config.json`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/tfsec) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [tfsec site](https://github.com/aquasecurity/tfsec)
* tfsec Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/tfsec)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
