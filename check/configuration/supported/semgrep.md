---
description: semgrep is a linter for Go, Java, Javascript, JSON, Python, Ruby, Typescript and YAML
---

**semgrep** is a linter for Go, Java, Javascript, JSON, Python, Ruby, Typescript and YAML.

You can enable the semgrep plugin with

```shell
trunk check enable semgrep
```

# Settings

semgrep uses the same config files as the
upstream [semgrep](https://github.com/returntocorp/semgrep#readme) project, so you can continue to use any
existing configuration files (ex: `.semgrep.yaml`, `.semgrep.yml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/semgrep) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
