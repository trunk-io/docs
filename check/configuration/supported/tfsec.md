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

## Auto Enabling

tfsec will never be auto-enabled. It must be enabled manually.

## Settings

tfsec supports the following config files:
* `tfsec.yml`
* `tfsec.yaml`
* `.tfsec/config.json`
* `.tfsec/config.yml`
* `.tfsec/config.yaml`

Unlike with most tools under `trunk check`, these files cannot be moved.




## Links

- [tfsec site](https://github.com/aquasecurity/tfsec)
- tfsec Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/tfsec)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
