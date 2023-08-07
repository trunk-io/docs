# Install Trunk

To install `trunk` run:

```bash
curl https://get.trunk.io -fsSL | bash
```

To install without prompting:

```bash
curl https://get.trunk.io -fsSL | bash -s -- -y
```

#### Commit the [Trunk Launcher ](../reference/components.md#trunk-launcher) directly into your repo

To allow your teammates to use `trunk` without installing anything, the launcher can be committed directly into your repo; Once committed, anyone working in your repository can use `trunk` without any additional installation. Fewer steps == less friction.

From your repo:

```bash
curl -LO https://trunk.io/releases/trunk
chmod +x trunk
```

#### With node package manager

| Package Manager | Command                         |
| --------------- | ------------------------------- |
| npm             | `npm i -D @trunkio/launcher`    |
| pnpm            | `pnpm add -D @trunkio/launcher` |
| yarn            | `yarn add -D @trunkio/launcher` |

#### With [homebrew](https://formulae.brew.sh/cask/trunk-io) (macOS only)

```bash
brew install trunk-io
```

### Uninstalling

Trunk has a very minimal installation, and therefore there's not much to uninstall. The two system paths we use are:

* `/usr/local/bin/trunk`: the [Trunk Launcher](../reference/components.md#trunk-launcher)
* `~/.cache/trunk`: cached versions of the trunk cli, linters, formatters, etc.

To cleanly uninstall:

```bash
trunk deinit
```

To uninstall the Trunk VS Code extension, do so as you would any extension ([docs](https://code.visualstudio.com/docs/editor/extension-marketplace)).

#### Binary download (not recommended)

You can directly download the trunk binary. \*\*We don't recommend this mode of operation because your ability to version the tool through `trunk.yaml` will not function when launching `trunk` directly from a downloaded binary. Regardless you can bypass the launcher support by downloading the prebuilt binaries here:

| variable | options                                       |
| -------- | --------------------------------------------- |
| version  | the semver of the binary you want to download |
| platform | 'darwin', 'linux'                             |

```bash
# for example https://trunk.io/releases/1.0.0/trunk-1.0.0-linux-x86_64.tar.gz
https://trunk.io/releases/${version}/trunk-${version}-${platform}-x86_64.tar.gz
```

#### Next Steps check out:

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Check</strong></td><td></td><td>An extendable superlinter with a builtin language server and preexisting issue detection</td><td><a href="../check/">check</a></td><td><a href="../.gitbook/assets/Check.svg">Check.svg</a></td></tr><tr><td>Actions</td><td></td><td>Workflow automation for your repository</td><td><a href="../actions/">actions</a></td><td><a href="../.gitbook/assets/Actions (2).svg">Actions (2).svg</a></td></tr><tr><td><strong>Merge</strong></td><td></td><td>A merge queue to make merging code in GitHub safer and easier</td><td><a href="../merge/">merge</a></td><td><a href="../.gitbook/assets/Merge.svg">Merge.svg</a></td></tr></tbody></table>

As well as the other ways to use Trunk:

* [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=trunk.io)
* [Web App (app.trunk.io)](https://app.trunk.io)
