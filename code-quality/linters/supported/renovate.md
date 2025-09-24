---
title: Trunk | How to run renovate
description: renovate is a linter for Renovate
---

# renovate

[**renovate**](https://github.com/renovatebot/renovate#readme) is a linter for Renovate.

You can enable the renovate linter with:

```shell
trunk check enable renovate
```

## Auto Enabling

renovate will be auto-enabled if any of its config files are present: _`renovate.json`, `renovate.json5`, `.github/renovate.json`_.

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

* [renovate site](https://github.com/renovatebot/renovate#readme)
* renovate Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/renovate)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
