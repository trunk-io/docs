---
description: Trufflehog: Enhance Your Code's Security
---

# Trufflehog

Trufflehog is a linter for Security.

You can enable the Trufflehog plugin with

```shell
trunk check enable trufflehog
```

# Settings

Trufflehog uses the same config files as the 
upstream [Trufflehog](https://github.com/trufflesecurity/trufflehog) project, so you can continue to use any
existing configuration files (ex: ${direct_configs}).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/trufflehog) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
