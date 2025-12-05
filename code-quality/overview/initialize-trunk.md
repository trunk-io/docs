# Initialize Trunk

Before you can start using Trunk Code Quality, you need to install and initialize Trunk in your repo. This page covers the initialization process.

### Install the CLI

The Trunk CLI can be installed in many different ways depending on your use case.

{% hint style="info" %}
We recommend installing the CLI via **NPM** if you’re already using NPM, or using **cURL** and **committing the launcher to Git** for all other projects. Both methods allow your teammates to use Trunk without needing an additional install step.
{% endhint %}

#### The Trunk Launcher

The easiest way to give everyone access to Trunk is to use the Trunk launcher. The Trunk launcher is a small script that will automatically install and run Trunk when invoked for the first time, similar to other command line tools like the [Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html).

You can install the [Trunk Launcher](cli/getting-started/install.md#the-trunk-launcher) script directly by downloading it through cURL. The launcher script supports both macOS and Linux environments.

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
curl -fsSLO --retry 3 https://trunk.io/releases/trunk
chmod +x ./trunk
git commit ./trunk -m "Commit Trunk to our repo"
```

#### Other ways to install

<details>

<summary>NPM</summary>

If your project uses a `package.json`, you can specify the Trunk Launcher as a dependency so your developers can start using Trunk after installing Node dependencies.

```sh
# npm
npm install -D @trunkio/launcher
# pnpm
pnpm add -D @trunkio/launcher
# yarn
yarn add -D @trunkio/launcher
# bun
bun install -D @trunkio/launcher
```

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

</details>

<details>

<summary>macOS (using homebrew)</summary>

You can run the following command if you prefer to install this tool via [homebrew](https://brew.sh/). Keep in mind that other developers on your team will also have to install manually.

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

```
Invoke-RestMethod -Uri https://trunk.io/releases/trunk.ps1 -OutFile trunk.ps1
```

Ensure you can execute powershell scripts:

```
Set-ExecutionPolicy Bypass -Scope CurrentUser
```

You can then execute trunk as `.\trunk.ps1`.

**Compatibility**

Only some versions of Trunk are compatible with Windows. See the compatibility page for [Windows](cli/getting-started/compatibility.md) to learn more.

You will also need to install [C and C++ runtime libraries](https://aka.ms/vs/17/release/vc_redist.x64.exe) in order to run some linters.

</details>

### Initializing Trunk

Before you can use Trunk, you need to initialize Trunk in your repo. Initializing Trunk will generate the necessary config files, recommend linters based on your project files, and configure githooks.

Initialize Trunk by running the `init` command.

```bash
./trunk init
```

Follow the wizard. You'll be prompted with the following options:

1. `Sign up or log in`: Connect the CLI with your Trunk account to enable all of Trunk's features.
2. Trunk will automatically [enable the most useful linters](https://docs.trunk.io/code-quality/setup-and-installation/initialize-trunk#recommended-linters) based on the files in your repo.
3. `Trunk will manage your git hooks and enable some built-in hooks.`: This sets up Trunk to run automatically on commit and before you push, saving you time waiting for CI only to have it fail.
4. `Trunk will now run a local, one-time scan of your code and report any issues it finds`: This initial scan will give you a good overview of the problem areas in your code. Subsequent scans will only run on changed lines using hold-the-line.

{% hint style="info" %}
**Trunk is Git aware**

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

### Run Linters

After initialization, you can run the [recommended set of linters](initialize-trunk.md#recommended-linters) by running:

```
./trunk check
```

:tada: And just like that, you're ready to start using Trunk Code Quality.

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

You will spend most of your time configuring Trunk Code Quality's linter definitions `trunk.yaml` and individual linter configurations in `configs`.

### Recommended Linters

During initialization, Trunk Code Quality will recommend some linters based on files found in your project. Trunk Code Quality will recommend common linters for your language, but the [full list of supported linters can be found here](linters/supported/).

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

Trunk Code Quality supports [VSCode](ide-integration/vscode.md) and [Neovim](ide-integration/neovim.md) through extensions. Using VSCode and Neovim will provide inline linter annotations as you code.

### Move Existing Configs

If you have existing linter configs in your repo, you can move them into the `.trunk/configs` folder. These config files will be symlinked in during any `trunk check` run.

{% hint style="warning" %}
If you're using an IDE Extension like `clangd` with an LSP that relies on those configs being in the root, you must create an additional symlink from the hidden config to the workspace root.
{% endhint %}

### Next Steps

After initializing Trunk Code Quality, you can check for issues and configure Code Quality. The [next steps](deal-with-existing-issues.md) in Setup & Installation will walk you through this process.
