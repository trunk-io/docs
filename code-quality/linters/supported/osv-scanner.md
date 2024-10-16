---
description: OSV-Scanner is an open-source tool created by Google to detect vulnerabilities in projects by scanning dependencies against the OSV database.
title: Trunk | How to run OSV-Scanner
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

# OSV-Scanner

[**OSV-Scanner**](https://github.com/google/osv-scanner) is a linter for Security.

You can enable the OSV-Scanner linter with:

```shell
trunk check enable osv-scanner
```

## Auto Enabling

OSV-Scanner will be auto-enabled if any *Lockfile* files are present.

## Settings

OSV-Scanner supports the following config files:
* `osv-scanner.toml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.




## Links

- [OSV-Scanner site](https://github.com/google/osv-scanner)
- OSV-Scanner Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/osv-scanner)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
