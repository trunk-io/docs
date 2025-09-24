---
title: Trunk | How to run Ansible-lint
description: >-
  Checks playbooks for practices and behavior that could potentially be improved
  and can fix some of the most common ones for you
---

# Ansible-lint

[**Ansible-lint**](https://github.com/ansible/ansible-lint) is a linter for Ansible.

You can enable the Ansible-lint linter with:

```shell
trunk check enable ansible-lint
```

## Auto Enabling

Ansible-lint will never be auto-enabled. It must be enabled manually.

## Settings

Ansible-lint supports the following config files:

* `.ansible-lint`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.

## Usage Notes

**Ansible-lint** must be configured with a trigger. See the [trigger rules](../#trigger-rules) documentation for more information.

If your ansible setup is not contained within a single folder you would list all files and directories belonging to your ansible setup.

## Links

* [Ansible-lint site](https://github.com/ansible/ansible-lint)
* Ansible-lint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/ansible-lint)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
