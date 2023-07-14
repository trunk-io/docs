# Configuration

Actions are defined and enabled in the `actions` section of [`trunk.yaml`](../reference/trunk-yaml.md).

Here is an example of the actions section of `trunk.yaml`. If you are curious what your resolved configuration for actions looks like, run `trunk config print`.

```yaml
actions:
  enabled:
    - trunk-announce
    - trunk-upgrade-available
    - npm-install
    - seed-database
    - custom-git-hook
    - login
  definitions:
    - id: npm-install
      triggers:
        - files: [package.json]
      run: npm install
    - id: seed-database
      triggers:
        - schedule: 24h
      run: python3 seed_database.py
      runtime: python
      run_from: utils
      packages_file: requirements.txt
    - id: custom-git-hook
      triggers:
        - git_hooks: [pre-push, pre-commit]
      run: my_script.sh
    - id: login
      run: my_complicated_login_script.sh
      interactive: true
```

### Action Definitions

Now we'll walk through the process of creating your own action.

Actions are required to have a `id` and `run` command.

The command will implicitly run relative to your workspace, but you can also specify a `run_from` if you'd prefer to execute from a sub-directory.

#### Runtime management

We sandbox action executions and allow you to control the runtime. You can do this by specifying a `runtime` and `packages_file`.

You can specify one of our built-in runtimes (`node`, `python`, ...) or a system runtime that you define. See the [runtimes documentation](../reference/trunk-yaml.md#runtimes)for more information.

For the `python` and `node` runtimes, we additionally provide the ability to install a requirements file like `requirements.txt` or `package.json`.

### Triggers

You may run an action manually by running `trunk run <action_id> <args>` or `trunk actions run <action_id> <args>`. However, you can also provide a set of triggers so that actions run in response to some event. They are documented below.

#### Time-based triggers

We provide the ability to run actions in the background on a schedule.

Under `triggers`, you can add one or more `schedule` entries. For example:

```yaml
id: my-action
triggers:
  - schedule: 1d
```

The `schedule` entry should be in the Duration format specified [here](https://pkg.go.dev/time#ParseDuration). The action will be run once per `duration`.

This is a short-hand for specifying schedule as an object. You can also write -

```yaml
id: my-action
triggers:
  - schedule:
      interval: 1d
```

The action may occasionally run more often than the specified duration depending on the Trunk daemon's lifetime.

If you wish to stagger the execution of an action from others on a similar schedule, you may use the `delay` field -

```yaml
id: my-action
triggers:
  - schedule:
      interval: 1d
      delay: 1h
```

You may also use cron syntax:

```yaml
id: my-action
 triggers:
    # run every 2 hours
    - schedule: "0 0 */2 * * ?"
```

or equivalently:

```yaml
id: my-action
 triggers:
    # run every 2 hours
    - schedule:
        cron: "0 0 */2 * * ?"
```

#### File-based triggers

We provide the ability to run actions automatically based on a file edit.

You may provide exact filenames, or globs.

```yaml
id: my-action
triggers:
  - files: [foo.txt, bar/**]
```

In this case `my-action` will execute if either `foo.txt` is edited (or created), or if a file inside `bar` is edited or created.

Note: We only provide file triggers for files inside of your workspace.

#### Git hooks

You can also configure trunk to manage your git hooks. More detail is provided on this in our [git hooks reference](../actions/git-hooks.md).

### Interactivity

Actions can read from `stdin` if they are marked as interactive (define `interactive: true` on the action). Note - this feature is only available for git hooks and manually run actions - since file-triggered and scheduled actions run in the background, you cannot interact with their execution.
