# Init in a git repo

Initializing `trunk` in a git repo is as simple as running:

```bash
trunk init
```

#### Security

When initializing you can secure your trunk installation which will write the sha256 signatures of the trunk binary to the `trunk.yaml` file. These signatures are verified by the <\<glossary:Trunk Launcher>> to guarantee the binary has not been tampered with. To add this extra layer of protection to your `trunk` setup init like this:

```bash
trunk init --lock
```

#### Code Scanning

`init` scans the files in your repo and generates a `.trunk/trunk.yaml` configuration file tailoring the `trunk check` product to your repo. The scan will identify all the particular languages and technologies you use and automatically configure the correct set of static-analyzers, code security tools, linters and formatters to run.

The `init` flow will also generate linter-specific config files for tools that require configuration and no configuration file already exists.

#### Tweak the Configuration

`trunk` is completely control through the `trunk.yaml` file. If for example you are not using the `check` tool you can safely remove the `lint` section from the file.

#### Single-player Mode

If you want to run `trunk` inside your repository but are not ready to roll it out team-wide, you can run `trunk` in what we call single-play mode. When in single-player mode, the `.trunk` directory will be listed in `.git/info/exclude`, which will cause git to ignore its contents. When trunk is automatically initialized by the vscode extension, you will be started in this mode. You can also initialize this way explicitly with the `trunk init --single-player-mode` command. If at any time you wish to toggle single-player mode on or off, it can be done with the following two commands:

```bash
# Turn single-player mode on.
trunk config hide
```

```bash
# Turn single-player mode off.
trunk config share
```
