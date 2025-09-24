---
title: Trunk | How to run OSV-Scanner
description: >-
  OSV-Scanner is an open-source tool created by Google to detect vulnerabilities
  in projects by scanning dependencies against the OSV database.
---

# OSV-Scanner

[**OSV-Scanner**](https://github.com/google/osv-scanner) is a linter for Security.

You can enable the OSV-Scanner linter with:

```shell
trunk check enable osv-scanner
```

## Auto Enabling

OSV-Scanner will be auto-enabled if any _Lockfile_ files are present.

## Settings

OSV-Scanner supports the following config files:

* `osv-scanner.toml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.

{% hint style="warning" %}
Moving `osv-scanner.toml` to `.trunk/configs` can cause issues because `osv-scanner.toml` is only applied to projects in the root folder by default. This can cause issues with any projects in subfolders, such as in a multi-module repository.
{% endhint %}

To properly configure OSV scanner if you decide to move its config file, you can specify the path to `osv-scanner.toml` using the `--config` flag.\
\
Example override to add to `trunk.yaml` : &#x20;

```yaml
commands:
  - name: scan
    run: |
      osv-scanner \
        --lockfile=${target} \
        --format json \
        --config=.trunk/configs/osv-scanner.toml
```

## Links

* [OSV-Scanner site](https://github.com/google/osv-scanner)
* [OSV-Scanner Configuration](https://google.github.io/osv-scanner/configuration/)
* OSV-Scanner Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/osv-scanner)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
