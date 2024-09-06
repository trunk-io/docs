---
description: ansible-lint is a linter for Ansible
title: Trunk | How to run ansible-lint
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

# ansible-lint

[**ansible-lint**](https://github.com/ansible/ansible-lint#readme) is a linter for Ansible.

You can enable the ansible-lint linter with:

```shell
trunk check enable ansible-lint
```

## Auto Enabling

ansible-lint will never be auto-enabled. It must be enabled manually.

## Settings

ansible-lint supports the following config files:
* `.ansible-lint`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [ansible-lint site](https://github.com/ansible/ansible-lint#readme)
- ansible-lint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/ansible-lint)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
