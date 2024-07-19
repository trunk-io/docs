---
description: >-
  You can think of Trunk Actions as IFTTT for your repository. An action is a
  command that is run when a specified trigger occurs.
---

# Actions

The most common Trunk Actions are provided out of the box with trunk, and are triggered to invisibly autoformat (`trunk fmt`) your commits every time you `git commit`, and run `trunk check` when you `git push`.

### Triggers

There are several different types of Trunk Actions, based on when they are triggered:

<table><thead><tr><th width="186">Trigger</th><th>Description</th></tr></thead><tbody><tr><td>time-based</td><td>run on a schedule (once per hour, once per day, once per week)</td></tr><tr><td>file modification</td><td>run whenever a file or directory in your repo changes.</td></tr><tr><td><a href="git-hooks.md">githooks</a></td><td>run whenever a listed githook event fires (e.g. pre-commit, on-push)</td></tr><tr><td>manual</td><td><code>trunk run &#x3C;action-name></code></td></tr></tbody></table>

### **Command Line**

<table><thead><tr><th width="276.757174392936">trunk actions &#x3C;command></th><th>Description</th></tr></thead><tbody><tr><td><code>list</code></td><td>list all available actions in the repository</td></tr><tr><td><code>history &#x3C;action-name></code></td><td>print the history for execution of the provided action</td></tr><tr><td><code>enable &#x3C;action-name></code></td><td>enable the provided action</td></tr><tr><td><code>disable &#x3C;action-name></code></td><td>disable the provided action</td></tr><tr><td><code>run &#x3C;action-name></code></td><td>manually trigger the provided action<br>alias: <code>trunk run &#x3C;action-name></code></td></tr></tbody></table>

### Discovering Actions

The trunk [plugins](https://github.com/trunk-io/plugins) repo ships with a collection of actions that can help supercharge your repository and provide examples of how to write your own actions. To see a list of actions that you can enable in your repo run:

```bash
trunk actions list
```

<figure><img src="../../../.gitbook/assets/image (27).png" alt=""><figcaption><p>List of actions reported by <code>trunk actions list</code></p></figcaption></figure>

### Enable/Disable Actions

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
