---
description: Enabling and Writing your own Actions
---

# Overview

\*\*You can think of Trunk Actions as IFTTT for your repository. An action is a command that is run in reaction to a specified [trigger](../actions/overview.md#triggers) \*\*

#### Triggers

\[block:parameters] { "data": { "h-0": "trigger", "h-1": "description", "0-0": "time based", "0-1": "run on a schedule (once an hour, once per day, once per week)", "1-0": "file modification", "1-1": "run whenever a file or directory in your repo changes.", "2-0": "[githooks](../actions/git-hooks.md)", "2-1": "run whenever a listed githook event fires (e.g. pre-commit, on-push)", "3-0": "manual", "3-1": "run from the command line `trunk run <action-name>`" }, "cols": 2, "rows": 4 } \[/block]

#### Command Line

\[block:parameters] { "data": { "0-0": "list", "h-0": "trunk actions `<command>`", "h-1": "description", "0-1": "list all available actions in the repository", "1-0": "history `<action-name>`", "1-1": "print the history for execution of the provided action", "2-0": "enable `<action-name>`", "2-1": "enable the provided action", "3-0": "disable `<action-name>`", "3-1": "disable the provided action", "4-0": "run `<action-name>`", "4-1": "manually trigger the provided action" }, "cols": 2, "rows": 5 } \[/block]

#### Discovering Actions

The trunk [plugins](https://github.com/trunk-io/plugins) repo ships with a collection of actions that can help supercharge your repository and provide examples for how to write your own actions. To see a list of actions that you can enable in your own repo run:

```bash
trunk actions list
```

\[block:image] { "images": \[ { "image": \[ "https://files.readme.io/df8a9ba-Screen\_Shot\_2022-08-18\_at\_6.10.41\_PM.png", "Screen Shot 2022-08-18 at 6.10.41 PM.png", 863, 297, "#282929" ], "caption": "List of actions reported by `trunk actions list`" } ] } \[/block]

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
