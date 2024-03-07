---
description: OSV-Scanner is an open-source tool created by Google to detect vulnerabilities in projects by scanning dependencies against the OSV database.
---

**OSV-Scanner** is a linter for Security.

You can enable the OSV-Scanner plugin with

```shell
trunk check enable osv-scanner
```

# Settings

OSV-Scanner uses the same config files as the
upstream [OSV-Scanner](https://github.com/google/osv-scanner) project, so you can continue to use any
existing configuration files (ex: `osv-scanner.toml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/osv-scanner) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
