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

## Settings

**semgrep** uses the same config files as the
upstream [semgrep](https://github.com/returntocorp/semgrep#readme) project, so you can continue to use any
existing configuration files (ex: `.semgrep.yaml`, `.semgrep.yml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/semgrep) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [semgrep site](https://github.com/returntocorp/semgrep#readme)
* semgrep Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/semgrep)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
