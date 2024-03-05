---
description: Oxipng is an open-source, CLI utility designed for optimizing PNG files. It applies lossless compression techniques to reduce file size.
---

**Oxipng** is a formatter for PNG.

You can enable the Oxipng plugin with

```shell
trunk check enable oxipng
```

# Settings

Oxipng uses the same config files as the 
upstream [Oxipng](https://github.com/shssoichiro/oxipng) project, so you can continue to use any
existing configuration files (ex: ${direct_configs}).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/oxipng) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
