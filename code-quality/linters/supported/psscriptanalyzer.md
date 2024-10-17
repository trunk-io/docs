---
description: psscriptanalyzer is a linter for PowerShell
title: Trunk | How to run psscriptanalyzer
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

# psscriptanalyzer

[**psscriptanalyzer**](https://github.com/PowerShell/PSScriptAnalyzer) is a linter for PowerShell.

You can enable the psscriptanalyzer linter with:

```shell
trunk check enable psscriptanalyzer
```

## Auto Enabling

psscriptanalyzer will be auto-enabled if a `PSScriptAnalyzerSettings.psd1` config file is present.

## Settings

psscriptanalyzer supports the following config files:
* `PSScriptAnalyzerSettings.psd1`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.




## Links

- [psscriptanalyzer site](https://github.com/PowerShell/PSScriptAnalyzer)
- psscriptanalyzer Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/psscriptanalyzer)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
