# Overview

### Getting Started

To use `trunk` locally, install via:

```bash
curl https://get.trunk.io -fsSL | bash
```

For other installation options (`npm`, `brew`, direct download, etc) and details on exactly what we install or how to uninstall, see the [Install Trunk](doc:install) doc.

Also check out the other ways to use Trunk:

- [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=trunk.io)
- [GitHub Action](https://github.com/marketplace/actions/trunk-check)
- [Web App (app.trunk.io)](https://app.trunk.io)

### What can it do?

The Trunk CLI can be used for:

- [Trunk Merge](../merge): a merge queue to make merging code in github safer and easier
- [Trunk Check](doc:check): a pluginable superlinter with a builtin language server and preexisting issue detection
- [Trunk Actions](doc:actions): workflow automation for software engineers

[Trunk Check](doc:check) and [Trunk Actions](doc:actions) can be used entirely locally without depending on hosted services or even having a Trunk account

### Initialize Trunk in your repo

Whether you aim to use [Trunk Check](doc:check), [Trunk Merge](../merge), [Trunk Actions](doc:actions), or all of the above, the first step is to initialize Trunk in your git repo:

```bash
trunk init
```

Note: for an extra layer of security you can optionally run `trunk init --lock` instead of `trunk init` which adds sha256s of the trunk cli to the trunk config file. This is then used by the Trunk Launcher when it downloads the `trunk` binary.

`init` scans the files in your repo and generates a `.trunk/trunk.yaml` configuration file tailored to your repo (it may also generate linter-specific config files, such as `.shellcheckrc`). The scan will identify all the particular languages and technologies you use and automatically configure the correct set of linters / formatters to run.

If you only want to use [Trunk Merge](../merge), you can safely ignore the linter setup, or even strip enabled linters from `.trunk/trunk.yaml`. You will additionally need to login to use [Trunk Merge](../merge) via `trunk login`.

### Next Steps

Check out the docs for [Trunk Merge](../merge), [Trunk Check](doc:check), and [Trunk Actions](doc:actions).
