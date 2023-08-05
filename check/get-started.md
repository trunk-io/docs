# Get Started

### Step 1: Install Trunk

To use `trunk` locally, run:

```bash
curl https://get.trunk.io -fsSL | bash
```

For other installation options (`npm`, `brew`, direct download, etc) and details on exactly what we install or how to uninstall, see the [Install Trunk](../overview/install-trunk.md) doc.

### Step 2: Initialize `trunk`

From the root of a git repo, run:

```bash
trunk init
```

This will bring you into a flow to start getting results from [Trunk Check](./). For more details, see [here](../cli/init-in-a-git-repo.md).

### Step 3: Run `trunk check` against a sampling of files in your repo

Normally when you run `trunk check` we will only scan changed files, so in a repo without any changes `trunk check` is going come back empty. To get a sense of the issues `trunk` can detect in your repo we suggest you run:

```bash
trunk check --sample 5
```

For more information on the sample flag see [here](command-line.md#sample)
