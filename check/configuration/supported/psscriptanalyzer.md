---
description: psscriptanalyzer is a linter for PowerShell
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

**psscriptanalyzer** is a linter for PowerShell.

You can enable the psscriptanalyzer plugin with

```shell
trunk check enable psscriptanalyzer
```

## Settings


**psscriptanalyzer** uses the same config files as the
upstream [psscriptanalyzer](https://github.com/PowerShell/PSScriptAnalyzer) project, so you can continue to use any
existing configuration files (ex: `PSScriptAnalyzerSettings.psd1`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/psscriptanalyzer) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
