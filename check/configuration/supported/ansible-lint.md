---
description: Checks playbooks for practices and behavior that could potentially be improved and can fix some of the most common ones for you
---

**Ansible-lint** is a linter for Ansible.

You can enable the Ansible-lint plugin with

```shell
trunk check enable ansible-lint
```

# Settings

Ansible-lint uses the same config files as the
upstream [Ansible-lint](https://github.com/ansible/ansible-lint) project, so you can continue to use any
existing configuration files (ex: `.ansible-lint`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/ansible-lint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).

**Ansible-lint** must be configured with a trigger. See the [trigger rules](../#trigger-rules) documentation for more information.

If your ansible setup is not contained within a single folder you would list all files and directories belonging to your ansible setup.



