---
description: Yamllint
---

# Yamllint

Yamllint is a linter for yaml.

You can enable the Yamllint plugin with

```shell
trunk check enable yamllint
```

# Settings

Yamllint uses the same config files as the 
upstream [Yamllint](https://github.com/adrienverge/yamllint) project, so you can continue to use any
existing configuration files (ex: `.yamllint`, `.yamllint.yaml`, `.yamllint.yml`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/yamllint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).