---
description: Checks playbooks for practices and behavior that could potentially be improved and can fix some of the most common ones for you
title: Trunk | How to run Ansible-lint
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

# Ansible-lint

[**Ansible-lint**](https://github.com/ansible/ansible-lint) is a linter for Ansible.

You can enable the Ansible-lint linter with:

```shell
trunk check enable ansible-lint
```

## Settings

**Ansible-lint** uses the same config files as the
upstream [Ansible-lint](https://github.com/ansible/ansible-lint) project, so you can continue to use any
existing configuration files (ex: `.ansible-lint`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/ansible-lint) if your project does not already have one,
which you can see in our [open source plugins repo]().

**Ansible-lint** must be configured with a trigger. See the [trigger rules](../#trigger-rules) documentation for more information.

If your ansible setup is not contained within a single folder you would list all files and directories belonging to your ansible setup.





## Links

* [Ansible-lint site](https://github.com/ansible/ansible-lint)
* Ansible-lint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/ansible-lint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
