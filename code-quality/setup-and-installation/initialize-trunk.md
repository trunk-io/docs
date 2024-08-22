# Initialize Trunk

Before you can start using Trunk Code Quality, you need to install and initialize Trunk in your repo. This page covers the initialization process.

### Install the CLI

The Trunk CLI can be installed in many different ways depending on your use case.

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

{% tabs %}
{% tab title="bash" %}
```bash
curl https://get.trunk.io -fsSL | bash
```
{% endtab %}

{% tab title="bash (no prompts)" %}
```bash
curl https://get.trunk.io -fsSL | bash -s -- -y
```
{% endtab %}
{% endtabs %}

To allow your teammates to use `trunk` without installing anything, the launcher can be committed directly into your repo:

```
curl -LO https://trunk.io/releases/trunk
chmod +x ./trunk
git commit ./trunk -m "Commit Trunk to our repo"
```

When the launcher is called for the first time by your teammates, the Trunk Launcher will download, manage, and run the appropriate binary for the environment.

#### Other Environments

<details>

<summary>Using homebrew</summary>

You can run the following command if you prefer to install this tool via homebrew. Keep in mind that other developers on your team will also have to install manually.

```bash
brew install trunk-io
```

</details>

<details>

<summary>Windows</summary>

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

You will also need to install [C and C++ runtime libraries](https://aka.ms/vs/17/release/vc\_redist.x64.exe) in order to run some linters.

</details>

### Initializing Trunk

Before you can use Trunk, you need to initialize Trunk in your repo. Initializing Trunk will generate the necessary config files, recommend linters based on your project files, and configure githooks.

#### NPM installs

If you installed `trunk` via NPM, you will need to run it by using `npm exec`. In the rest of the documentation, all commands will be shown as `trunk <subcommand>` for brevity.

```sh
npm exec trunk init
```

#### Other installs

```bash
trunk init
```

Follow the wizard, you'll be prompted with the following options:

1. `Sign up or log in`: If you plan to upload runner results to the Trunk Web App for tracking, login, otherwise this can be skipped.
2. Trunk will automatically[ recommend some common linters](initialize-trunk.md#recommended-linters) according to files in your repo.
3. `Would you like Trunk to manage your git hooks and enable some built-in hooks? (Y/n)`: If you wish to run Trunk on commit and before push automatically, you and respond `Y` otherwise `n`.
4. `Would you like Trunk to scan your repo for issues? (Y/n)`: Run newly enabled linters with Trunk Code Quality immediately with `Y`, otherwise, existing issues are hidden by default with hold-the-line. You can still [scan for existing issues in the next step](deal-with-existing-issues.md).

{% hint style="info" %}
#### Trunk is Git aware

Trunk speeds up your linting process by running on only the files that have changed in your branch compared to upstream. This means if you're using a base/trunk branch that's not `master` or `main`, you will need to specify it in your `.trunk/trunk.yaml`

```yaml
version: 0.1
cli:
  version: 1.22.2
repo:
  # develop is the branch that everyone's work is merged into
  trunk_branch: develop
... rest of configs
```
{% endhint %}



### The .trunk Directory

After initialization, a new folder `.trunk` will be generated with the following content.

```
.trunk
├── actions/ 
├── configs/ # This is where linter configs live
├── logs/ # Logs for debugging
├── notifications/
├── out/
├── plugins/
├── tools/ 
└── trunk.yaml # Top-level Trunk config
```

You will spend most of your time configuring Trunk Code Quality's linter definitions  `trunk.yaml` and individual linter configurations in `configs`.&#x20;

### Recommended Linters

During initialization, Trunk Code Quality will recommend some linters based on files found in your project. Trunk Code Quality will recommend common linters for your language, but the [full list of supported linters can be found here](../linters/supported/).

You can enable and disable individual linters by running:

```bash
trunk check enable <linter>
trunk check disable <linter>
```

You can also see all linters and whether they're enabled by running:

```bash
trunk check list
```

### IDE Integration

Trunk Code Quality supports [VSCode](../ide-integration/vscode.md) and [Neovim](../ide-integration/neovim.md) through extensions. Using VSCode and Neovim will provide inline linter annotations as you code.

### Move Existing Configs

If you have existing linter configs in your repo, you can move them into the `.trunk/configs` folder. These config files will be symlinked in during any `trunk check` run.&#x20;

{% hint style="warning" %}
If you're using an IDE Extension like `clangd` with an LSP that relies on those configs being in the root, you must create an additional symlink from the hidden config to the workspace root.
{% endhint %}

### Next Steps

After initializing Trunk Code Quality, you can check for issues and configure Code Quality. The next steps in Setup & Installation will walk you through this process.
