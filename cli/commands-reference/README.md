# Commands Reference

### trunk init

`trunk init`: Set up trunk in this repo.

#### **Usage** Example

```
trunk init
```

### trunk version

`trunk version`: Output the version.

#### **Usage** Example

```
trunk version
```

### trunk upgrade

`trunk upgrade`: Upgrade Trunk and its linters to the latest releases.&#x20;

#### **Usage** **example**

```
trunk upgrade [options]
```

#### **Options**

* `-y, --yes-to-all`: Answer yes to all upgrade prompts
* `-n, --no-to-all`: Answer no to all upgrade prompts
* `--apply-to`: Apply upgrades to a specified file
* `--filter`: Filter the upgraded linters
* `--dry-run`: Detect available upgrades, but do not apply changes

### trunk login

`trunk login`: Login to trunk.io.

#### **Usage** Example

```
trunk login
```

### trunk logout

`trunk logout`: Logout from trunk.io.

#### **Usage** Example

```
trunk logout
```

### trunk plugins add

`trunk plugins add`: Add a plugin by URI.

#### **Usage** Example

```
trunk plugins [uri] [ref] [options]
```

### trunk tools

`trunk tools`: Universal tool manager.

#### **Usage** Example

```
trunk tools [options]
```

### trunk daemon status

Report the status of the daemon.

#### **Usage Example**

```
trunk daemon status
```

### trunk daemon start

Start the trunk daemon in the background if it’s not already running.

#### **Usage Example**

<pre><code><strong>trunk daemon start
</strong></code></pre>

### **trunk daemon shutdown**

`trunk daemon shutdown`: Shutdown the trunk daemon if it is running.

#### **Usage Example**

```
trunk daemon shutdown
```

### **trunk daemon launch**

`trunk daemon launch`: Start the trunk daemon in the foreground if it’s not already running.

#### **Usage Example**

```
trunk daemon launch
```

### trunk whoami

`trunk whoami`: print who you're logged in as

#### **Usage** Example

```
trunk whoami
```

### trunk deinit

`trunk deinit`: Deinitialize Trunk in your repo

#### **Usage** Example

```
trunk deinit [options]
```

#### **Options**

* `-y`, `--yes`: Proceed unconditionally
* `-v`, `--verbose`: Output details about what's happening under the hood
* `--color`: Enable/disable color output

### trunk config share

`trunk config share`: Remove Trunk config files from your local git ignores.

#### **Usage Example**

```
trunk config share 
```

### trunk config hide

`trunk config hide`: Add Trunk config files to your local git ignores.

#### **Usage Example**

```
trunk config hide
```

### trunk config print

`trunk config print`: Print the resolved trunk config.

#### **Usage Example**

```
trunk config print
```

### trunk cache clean

`trunk cache clean`: Clean cached files used by Trunk.

#### **Usage** Example

```
trunk cache clean
```

### trunk cache prine

`trunk cache prune`: Prune unused cached files.

#### **Usage** Example

```
trunk cache clean
```

### trunk install

`trunk install`: Download & install enabled runtimes/linters.

#### **Usage** Example

```
trunk install [options]
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
