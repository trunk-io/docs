---
description: semgrep is a linter for Go, Java, JavaScript, JSON, Python, Ruby, TypeScript and YAML
title: Trunk | How to run semgrep
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

# semgrep

[**semgrep**](https://github.com/returntocorp/semgrep#readme) is a linter for Go, Java, JavaScript, JSON, Python, Ruby, TypeScript and YAML.

You can enable the semgrep linter with:

```shell
trunk check enable semgrep
```

## Auto Enabling

semgrep will be auto-enabled if any of its config files are present: *`.semgrep.yaml`, `.semgrep.yml`*.

## Settings

semgrep supports the following config files:
* `.semgrep.yaml`
* `.semgrep.yml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [semgrep site](https://github.com/returntocorp/semgrep#readme)
- semgrep Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/semgrep)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
