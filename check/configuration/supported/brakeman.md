---
description: Brakeman- A security scanner for Ruby on Rails applications
---

# Brakeman

Brakeman is a linter for Ruby.

You can enable the Brakeman plugin with

```shell
trunk check enable brakeman
```

# Settings

Brakeman uses the same config files as the 
upstream [Brakeman](https://github.com/presidentbeef/brakeman) project, so you can continue to use any
existing configuration files (ex: `brakeman.ignore`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/brakeman) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
