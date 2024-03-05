---
description: Uncover Flake8, a versatile Python linter for code style and error checking. Flake 8 checks against PEP 8 and more, with plugin support for broader analysis.
---

**Flake8** is a linter for Python.

You can enable the Flake8 plugin with

```shell
trunk check enable flake8
```

# Settings

Flake8 uses the same config files as the 
upstream [Flake8](https://flake8.pycqa.org/en/latest/) project, so you can continue to use any
existing configuration files (ex: `.flake8`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/flake8) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).


Flake8 has a plugin architecture where if you install a plugin, it gets used. You can enable Flake8 plugins via:

```yaml
enabled:
  - flake8@3.9.2:
      packages:
        - flake8-bugbear@21.4.3
```
`flake8-bugbear` is probably the most popular **flake8** plugin, we recommend it!. Here are a few other popular flake8 plugins you should consider.

* **flake8-comprehensions**: Helps in identifying unnecessary comprehensions in your code.

* **flake8-docstrings**: Checks for compliance with Python docstring conventions.

* **flake8-import-order**: Checks the order of your imports according to various configurable ordering styles.

Here's an updated code snippet with the above Plugins enabled:

```undefined
enabled:
  - flake8@3.9.2:
      packages:
        - flake8-bugbear@21.4.3
        - flake8-docstrings@1.7.0
        - flake8-import-order@0.18.2
        - flake8-comprehensions@3.14.0
```


