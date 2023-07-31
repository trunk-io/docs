---
description: Enabling and Writing your own Actions
---

# Overview

**You can think of Trunk Actions as IFTTT for your repository. An action is a command that is run in reaction to a specified** [**trigger**](overview.md#triggers)

#### Triggers

<table><thead><tr><th width="186">trigger</th><th>description</th></tr></thead><tbody><tr><td>time based</td><td>run on a schedule (once an hour, once per day, once per week)</td></tr><tr><td>file modification</td><td>run whenever a file or directory in your repo changes.</td></tr><tr><td><a href="git-hooks.md">githooks</a></td><td>run whenever a listed githook event fires (e.g. pre-commit, on-push)</td></tr><tr><td>manual</td><td>run from the command line trunk run</td></tr></tbody></table>

**Command Line**

<table><thead><tr><th width="253">trunk actions &#x3C;command></th><th>description</th></tr></thead><tbody><tr><td>list</td><td>list all available actions in the repository</td></tr><tr><td>history <code>&#x3C;action-name></code></td><td>print the history for execution of the provided action</td></tr><tr><td>enable <code>&#x3C;action-name></code></td><td>enable the provided action</td></tr><tr><td>disable <code>&#x3C;action-name></code></td><td>disable the provided action</td></tr><tr><td>run <code>&#x3C;action-name></code></td><td>manually trigger the provided action</td></tr></tbody></table>

#### Discovering Actions

The trunk [plugins](https://github.com/trunk-io/plugins) repo ships with a collection of actions that can help supercharge your repository and provide examples for how to write your own actions. To see a list of actions that you can enable in your own repo run:

```bash
trunk actions list
```

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption><p>List of actions reported by <code>trunk actions list</code></p></figcaption></figure>

#### Enable/Disable Actions

Trunk only runs actions listed in the `enabled` section of your `trunk.yaml`. Some built-in actions are enabled by default and can be disabled explicitly by adding them to the disabled list. You can always run `trunk actions list` to check the enabled status of an action.

```yaml
actions:
  enabled:
    - trunk-announce
    - git-lfs
    - trunk-check-pre-push
    - trunk-fmt-pre-commit
    - trunk-cache-prune
    - trunk-upgrade-available
```
