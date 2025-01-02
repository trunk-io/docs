# Install

### The Trunk Launcher

Trunk uses a launcher to automatically install the appropriate CLI for your platform. The launcher is a bash script that downloads the appropriate Trunk CLI version and runs it. The launcher invisibly runs the Trunk CLI version specified in a project's `.trunk/trunk.yaml` file. The actual Trunk CLI is a single binary that is cached locally in `~/.cache/trunk` and is updated automatically.

### Install the Launcher

The Trunk CLI can be installed in many different ways, depending on your use case.

{% include "../.gitbook/includes/slack-callout.md" %}

#### Using NPM

If your project uses a `package.json`, you can specify the Trunk Launcher as a dependency so your developers can start using Trunk after installing Node dependencies.

{% tabs %}
{% tab title="npm" %}
```sh
npm install -D @trunkio/launcher
```
{% endtab %}

{% tab title="pnpm" %}
```sh
pnpm add -D @trunkio/launcher
```
{% endtab %}

{% tab title="yarn" %}
```sh
yarn add -D @trunkio/launcher
```
{% endtab %}

{% tab title="bun" %}
```sh
bun install -D @trunkio/launcher
```
{% endtab %}
{% endtabs %}

Then add Trunk Launcher in your `package.json` as a script:

```json
{
  "scripts": {
    "trunk": "trunk",
    "lint": "trunk check",
    "fmt": "trunk fmt"
  }
}
```

#### Using cURL

You can install the Trunk Launcher script directly by downloading it through cURL. The launcher script supports both macOS and Linux environments.

{% include "../.gitbook/includes/curl-https-get.trunk.io-....md" %}

To allow your teammates to use `trunk` without installing anything, the launcher can be committed directly into your repo:

```
curl -LO https://trunk.io/releases/trunk
chmod +x trunk
git commit ./trunk -m "Commit Trunk to our repo"
```

When the launcher is called for the first time by your teammates, the Trunk Launcher will download, manage, and run the appropriate binary for the environment.

#### Using Homebrew

You can run the following command if you prefer to install this tool via homebrew. Keep in mind that other developers on your team will also have to install manually.

```bash
brew install trunk-io
```

#### Using Windows

From **`git-bash` or `msys2`**, download the Bash launcher and add it to your `PATH`:

```bash
curl https://get.trunk.io -fsSL | bash
```

From **`powershell`**, download the powershell launcher:

```Text
Invoke-RestMethod -Uri https://trunk.io/releases/trunk.ps1 -OutFile trunk.ps1
```

Ensure you can execute powershell scripts:

```Text
Set-ExecutionPolicy Bypass -Scope CurrentUser
```

You can then execute trunk as `.\trunk.ps1`.

#### Compatibility

Trunk only supports Windows with the following versions and above:

<table><thead><tr><th width="112.33333333333331">Tool</th><th width="397">Where to Modify</th><th>Minimum Required Version</th></tr></thead><tbody><tr><td>CLI</td><td><code>cli</code> <code>version</code> in <code>.trunk/trunk.yaml</code></td><td><code>1.13.0</code></td></tr><tr><td>Plugins</td><td><code>ref</code> for the <code>trunk</code> plugin in <code>.trunk/trunk.yaml</code></td><td><code>v1.0.0</code></td></tr><tr><td>VSCode</td><td>Reload VSCode to update</td><td><code>3.4.4</code></td></tr></tbody></table>

You will also need to install [C and C++ runtime libraries](https://aka.ms/vs/17/release/vc_redist.x64.exe) in order to run some linters.

### Uninstall instructions

#### From your system

Trunk has a very minimal installation, and therefore, there's not much to uninstall. The two system paths we use are:

* `/usr/local/bin/trunk`: the [Trunk Launcher](install.md#the-trunk-launcher)
* `~/.cache/trunk`: cached versions of the trunk cli, linters, formatters, etc.

You can delete those two paths to uninstall.

#### From a repo

To cleanly remove Trunk from a particular repo, run:

```bash
trunk deinit
```

#### VS Code extension

To uninstall the Trunk VS Code extension, do so as you would any extension ([docs](https://code.visualstudio.com/docs/editor/extension-marketplace)). Then reload VS Code.

### Binary download (not recommended)

You can directly download the `trunk` binary. _We don't recommend this mode of operation because your ability to version the tool through_ `trunk.yaml` _will not function when launching_ `trunk` _directly from a downloaded binary._ Regardless you can bypass the launcher support by downloading the prebuilt binaries here:

<table><thead><tr><th width="178">variable</th><th>options</th></tr></thead><tbody><tr><td>version</td><td>the semver of the binary you want to download</td></tr><tr><td>platform</td><td>'darwin`, 'linux'</td></tr></tbody></table>

```bash
# for example https://trunk.io/releases/1.0.0/trunk-1.0.0-linux-x86_64.tar.gz
https://trunk.io/releases/${version}/trunk-${version}-${platform}-x86_64.tar.gz
```

### Pre-installing tools

Trunk hermetically manages all the tools that it runs. To do this, it will download and install them into its cache folder only when they are needed. If you would like to ensure that all tools are installed ahead of time, then you can use the `trunk install` command. This may be useful if you want to prepare to work offline or if you would like to include the tools in a docker image. On Linux and macOS you may find the cache folder at `$HOME/.cache/trunk`.
