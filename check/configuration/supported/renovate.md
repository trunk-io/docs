---
description: renovate is a linter for Renovate
title: Trunk | How to run renovate
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

# renovate

[**renovate**](https://github.com/renovatebot/renovate#readme) is a linter for Renovate.

You can enable the renovate linter with:

```shell
trunk check enable renovate
```

## Auto Enabling

renovate will be auto-enabled if any of its config files are present: *`renovate.json`, `renovate.json5`, `.github/renovate.json`*

## Settings

renovate supports the following config files:
* `renovate.json`
* `renovate.json5`
* `.github/renovate.json`
* `.github/renovate.json5`
* `.gitlab/renovate.json`
* `.gitlab/renovate.json5`
* `.renovaterc`
* `.renovaterc.json`
* `.renovaterc.json5`

 Unlike with most tools under `trunk check`, these files cannot be moved.



## Links

- [renovate site](https://github.com/renovatebot/renovate#readme)
- renovate Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/renovate)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
