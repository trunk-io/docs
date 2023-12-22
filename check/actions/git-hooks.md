---
description: Trunk supports triggering actions on all githooks
---

# Git Hooks

### Features

* Seamlessly bring `git-hooks` under version control. `git-hooks`  can be a major headache for organizations - they require manual installation and are not easily versioned along with the rest of your code.
* Take advantage of Trunk's powerful sandboxing and environment management to write and execute hooks using the programming language and runtime of your choice, as opposed to dealing with complicated bash scripts.

### Manual Installation

```bash
trunk git-hooks sync
```

### Automatic Installation

Trunk will automatically install and begin managing your `githooks` if you have any actions enabled in `trunk.yaml` which trigger from git events.

### Triggering an action from a githook

As an example let's examine how we implement the `git-lfs` action in the [plugins repo](https://github.com/trunk-io/plugins).

#### Definition

{% code lineNumbers="true" %}
```yaml
- id: git-lfs
  display_name: Git LFS
  description: Git LFS hooks
  run: git lfs "${hook}" "${@}"
  triggers:
    - git_hooks: [post-checkout, post-commit, post-merge, pre-push]
```
{% endcode %}

#### Template resolution

As documented by [git](https://git-scm.com/docs/githooks), each githook generates a variable number of parameters that can be referenced in the `run` entry for the action.

The following special variables are made available for template resolution when reacting to a git event:

| Variable                      | Description                                                     |
| ----------------------------- | --------------------------------------------------------------- |
| `${hook}`                     | Hook that triggered this action (e.g. `pre-commit`, `pre-push`) |
| `${1}`,`${2}`, `${3}`, etc... | Positional parameters passed by `git` to the hook               |
| `${@}`                        | All parameters passed to the hook                               |

#### Interactivity

```yaml
interactive: true
```

Setting `interactive` to true will allow your githook action to be run from an interactive terminal. This enables you to write more complicated hooks to react to user input.

#### Testing a `githook` action

The following command will simulate a githook event and execute all of the enabled actions for the provided hook in the order you defined them.

```bash
trunk git-hooks callback <hook> -- <args>
```

Alternatively, once an action is enabled you can call `git` and debug with the actual `git` provided data. This is sometimes easier since some git parameters point to txt files etc...and fabricating those formats through manual testing can be tricky.

#### Debugging a `githook` action

You can observe the actions that are triggered by a `git` event by calling:

```bash
trunk actions history <action-name>
```

Which will print out the last 10 executions including timestamps of the specified action \\

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption><p>trunk actions history for git-lfs action</p></figcaption></figure>

### Uninstalling

Remove all actions that are triggered by githooks from `trunk.yaml` and run

```bash
git config --unset core.hooksPath
```

### Trunk Announce

Does your commit carry some important information to share with the rest of your organization? Now you can easily share it with the rest of the org by including `/trunk announce` at the beginning of one of the lines of your commit message (if your org squashes commit messages, you should put it in your PR description). Any additional text on that line will form an optional title, and the remaining text of the commit message will form the commit body (both are optional, but either a title or body is required). These will then be displayed to other users when they pull or rebase.

If you want to see what your announcement would look like locally, just create a commit with the desired message and then run `trunk show-announcements since HEAD~1` (`trunk show-announcements since <ref>` will show all trunk announcements since the provided ref).

Just run `trunk actions enable trunk-announce` to start using Trunk Announce.
