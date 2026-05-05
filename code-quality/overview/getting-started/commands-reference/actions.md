# Actions

### Trunk Actions

`trunk actions`: Workflow automation for your repo.

#### **Usage** **example**

```
trunk actions [options] [subcommand]
```

#### Options

* `--version`: The version
* `--monitor`: Enable the trunk daemon to monitor file changes in your repo
* `--ci`: Run in continuous integration mode
* `--no-progress`: Don't show progress updates
* `--ci-progress`: Rate limit progress updates to every 30s (implied by `--ci`)
* `--action_timeout`: Timeout for downloads, lint runs, etc
* `-v`, `--verbose`: Output details about what's happening under the hood
* `--color`: Enable/disable color output

### Trunk Actions run

`trunk actions run`: Run a specified trunk action. **Usage** **bash**

```
trunk actions run [options]
```

#### **Options**

* `--nolog`: Don't create a log file for the action run
* `--version`: The version
* `--monitor`: Enable the trunk daemon to monitor file changes in your repo
* `--ci`: Run in continuous integration mode
* `--no-progress`: Don't show progress updates
* `--ci-progress`: Rate limit progress updates to every 30s (implied by `--ci`)
* `--action_timeout`: Timeout for downloads, lint runs, etc.
* `-v`, `--verbose`: Output details about what's happening under the hood
* `--color`: Enable/disable color output
* `--name <action_name>`: Specify the name of the Trunk action to be executed
* `--branch <branch_name>`: Run the action on a specific branch
* `--retry <number>`: Number of times to retry the action on failure

### Trunk Actions history

`trunk actions history`: View the history of Trunk actions.

#### **Usage** example

```
trunk actions history [options]
```

#### **Options**

* `--count`: Number of logs to show
* `--version`: The version
* `--monitor`: Enable the trunk daemon to monitor file changes in your repo
* `--ci`: Run in continuous integration mode
* `--no-progress`: Don't show progress updates
* `--ci-progress`: Rate limit progress updates to every 30s (implied by `--ci`)
* `--action_timeout`: Timeout for downloads, lint runs, etc.
* `-v`, `--verbose`: Output details about what's happening under the hood
* `--color`: Enable/disable color output

### Trunk Actions list

`trunk actions list`: List all Trunk actions.

#### **Usage** example

```
trunk actions list [options]
```

#### **Options**

* `--version`: The version
* `--monitor`: Enable the trunk daemon to monitor file changes in your repo
* `--ci`: Run in continuous integration mode
* `--no-progress`: Don't show progress updates
* `--ci-progress`: Rate limit progress updates to every 30s (implied by `--ci`)
* `--action_timeout`: Timeout for downloads, lint runs, etc.
* `-v`, `--verbose`: Output details about what's happening under the hood
* `--color`: Enable/disable color output

### Trunk Actions enable

`trunk actions enable`: Enable a specified Trunk action.

#### **Usage** example

```
trunk actions enable [options]
```

#### **Options**

* `--version`: The version
* `--monitor`: Enable the trunk daemon to monitor file changes in your repo
* `--ci`: Run in continuous integration mode
* `--no-progress`: Don't show progress updates
* `--ci-progress`: Rate limit progress updates to every 30s (implied by `--ci`)
* `--action_timeout`: Timeout for downloads, lint runs, etc.
* `-v`, `--verbose`: Output details about what's happening under the hood
* `--color`: Enable/disable color output

### Trunk Actions disable

`trunk actions disable`: Disable a specified Trunk action.

#### **Usage** example

```
trunk actions disable [options]
```

#### **Options**

* `--version`: The version
* `--monitor`: Enable the trunk daemon to monitor file changes in your repo
* `--ci`: Run in continuous integration mode
* `--no-progress`: Don't show progress updates
* `--ci-progress`: Rate limit progress updates to every 30s (implied by `--ci`)
* `--action_timeout`: Timeout for downloads, lint runs, etc.
* `-v`, `--verbose`: Output details about what's happening under the hood
* `--color`: Enable/disable color output

### Trunk Shellhooks

`trunk shellhooks`: Let Trunk manage your shell hooks similar to `direnvs` trunk shellhooks install \<shell\_name>

#### **Usage** example

```
trunk shellhooks install <shell_name> [options]
```

### Trunk Git Hooks

`trunk git-hooks sync`: Sync githooks with what's defined in `trunk.yaml`

#### **Usage** example

```
trunk git-hook sync [options]
```

### Trunk show announcements since a commit

**`trunk show-announcements since`**: Show announcements since a specified commit

#### **Usage** example:

```sh
trunk show-announcements since --commit abc123
```

#### **Options**:

* `--color`: Enable/disable color output
* `-v`, `--verbose`: Output details about what's happening under the hood
* `--action_timeout`: Timeout for downloads, lint runs, etc.
* `--ci-progress`: Rate limit progress updates to every 30s (implied by `--ci`)
* `--no-progress`: Don't show progress updates
* `--ci`: Run in continuous integration mode
* `--monitor`: Enable the trunk daemon to monitor file changes in your repo
* `--version`: The version

### **Trunk show announcements post-merge**

**`trunk show-announcements post-merge`**: Run on git pull/merge, usually run by a git-hook and not directly.

**Usage Example**:

```sh
trunk show-announcements post-merge --verbose
```

### **Trunk show announcements pre-rebase**

**`trunk show-announcements pre-rebase`**: Run on git pre-rebase, usually run by a git-hook and not directly.

#### **Usage** example:

```sh
trunk show-announcements pre-rebase [options] [branch-refs...]
```

### **Trunk show announcements post-checkout**

**`trunk show-announcements post-checkout`**: Run on git checkout/switch, usually run by a git-hook and not directly.

#### **Usage** example::

```sh
trunk show-announcements post-checkout [options] [branch-refs...]
```
