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

## Settings

**psscriptanalyzer** uses the same config files as the
upstream [psscriptanalyzer](https://github.com/PowerShell/PSScriptAnalyzer) project, so you can continue to use any
existing configuration files (ex: `PSScriptAnalyzerSettings.psd1`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/psscriptanalyzer) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [psscriptanalyzer site](https://github.com/PowerShell/PSScriptAnalyzer)
* psscriptanalyzer Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/psscriptanalyzer)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
