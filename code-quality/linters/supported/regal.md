---
description: regal is a linter for Rego
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

# regal

[**regal**](https://github.com/StyraInc/regal) is a linter for Rego.

You can enable the regal linter with:

```shell
trunk check enable regal
```

## Auto Enabling

regal will be auto-enabled if a `.regal/config.yaml` config file is present.

## Settings

regal supports the following config files:

* `.regal/config.yaml`

Unlike with most tools under `trunk check`, these files cannot be moved.

## Links

* [regal site](https://github.com/StyraInc/regal)
* regal Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/regal)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
