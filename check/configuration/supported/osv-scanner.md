---
description: OSV-Scanner: Install and Configuration Guide
---

# OSV-Scanner

OSV-Scanner is a linter for Security.

You can enable the OSV-Scanner plugin with

```shell
trunk check enable osv-scanner
```

# Settings

OSV-Scanner uses the same config files as the 
upstream [OSV-Scanner]() project, so you can continue to use any
existing configuration files (ex: `osv-scanner.toml`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/osv-scanner) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
