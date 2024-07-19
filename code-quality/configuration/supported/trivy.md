---
title: Trunk | How to run Trivy
description: >-
  Explore our guide on Trivy, the comprehensive vulnerability scanner. Learn
  about its features, installation, and configuration.
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

# Trivy

[**Trivy**](https://github.com/aquasecurity/trivy) is a linter for Security.

You can enable the Trivy linter with:

```shell
trunk check enable trivy
```

![trivy example output](../../../check/configuration/supported/trivy.gif)

## Auto Enabling

Trivy will be auto-enabled if any _Lockfile, ALL, Docker, Yaml or Terraform_ files are present.

## Settings

Trivy supports the following config files:

* `trivy-secret.yaml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](../#moving-linter-configs) for more info.

## Usage Notes

Trivy has the following subcommands:

* `config`
* Runs `trivy config` ([docs) ](https://aquasecurity.github.io/trivy/latest/docs/scanner/misconfiguration/))to scan for misconfigurations in infrastructure-as-code files. Enabled by default
* `fx-vuln`
* Runs `trivy fs --scanners vuln` ([docs](https://aquasecurity.github.io/trivy/latest/docs/target/filesystem/)) to scan for security vulnerabilities. Disabled by default.
* `fs-secret`
* Runs `trivy fs --scanners secret` ([docs](https://aquasecurity.github.io/trivy/latest/docs/target/filesystem/)) to scan for secrets. Disabled by default.

To enable/disable these, add the subcommands you want enabled in your `.trunk/trunk.yaml` as such:

```yaml
lint:
  enabled:
    - trivy@0.45.1:
        commands: [config, fs-vuln]
```

## Links

* [Trivy site](https://github.com/aquasecurity/trivy)
* Trivy Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/trivy)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
