---
description: Explore our guide on Trivy, the comprehensive vulnerability scanner. Learn about its features, installation, and configuration.
---

**Trivy** is a linter for Security.

You can enable the Trivy plugin with

```shell
trunk check enable trivy
```

# Settings

Trivy uses the same config files as the 
upstream [Trivy](https://github.com/aquasecurity/trivy) project, so you can continue to use any
existing configuration files (ex: `trivy-secret.yaml`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/trivy) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).


Trivy has the following subcommands:

* `config`

* Runs `trivy config` ([docs) ](https://aquasecurity.github.io/trivy/latest/docs/scanner/misconfiguration/))to scan for misconfigurations in infrastructure-as-code files. Enabled by default

* `fx-vuln`

* Runs `trivy fs --scanners vuln `([docs](https://aquasecurity.github.io/trivy/latest/docs/target/filesystem/)) to scan for  security vulnerabilities. Disabled by default.

* `fs-secret`

* Runs `trivy fs --scanners secret `  ([docs](https://aquasecurity.github.io/trivy/latest/docs/target/filesystem/)) to scan for secrets. Disabled by default.

To enable/disable these, add the subcommands you want enabled in your `.trunk/trunk.yaml` as such:

```yaml
lint:
  enabled:
    - trivy@0.45.1:
        commands: [config, fs-vuln]
```
