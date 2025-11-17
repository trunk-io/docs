---
hidden: true
---

# Migration Guide

### What's deprecated

The Code Quality dashboard in the Trunk web app has been deprecated, along with the ability to configure and manage CI workflows in the web app.

### Breaking Changes

⚠️ **The `--upload` flag has been removed from the Trunk CLI**

If you're using `--upload` in your scripts or CI configurations, you must remove it. This flag was previously used to send data to our backend for the deprecated Code Quality dashboard but is no longer supported.

**Action required:** Remove `--upload` from any `trunk check` commands in your CI pipelines or scripts.

### Migrating nightly and PR jobs

Nightly and PR jobs configured through the Trunk web app will no longer be supported. However, you can still run these checks by migrating these workflows to run as a step in your existing CI pipelines.

#### Run on PRs on GitHub Actions

Trunk provides a [GitHub action](https://github.com/trunk-io/trunk-action) to help you lint your code in CI. You add it as a step to your workflows. To run on pull requests or on a schedule, you can configure the appropriate triggers for your workflow.&#x20;

```yaml
name: Trunk Code Quality
on:
  push:
    branches: main
  pull_request:
    branches: main
	
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # ... other setup steps
      - name: Trunk Code Quality
        uses: trunk-io/trunk-action@v1
      # ... other CI steps
```

You will still receive inline comments about your errors if you run the action with the `post-annotations` argument.

#### Run on PRs using other CI providers

You can also set up checks on PR without using the provided GitHub action. Download the CLI in line and run the Code Quality CLI in CI mode to check a PR. Note that you will not receive inline arguments with this approach.

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk 
chmod +x trunk 
./trunk check --ci
```

Here’s an example of the commands in a GitHub Actions workflow, but you can do the same in virtually any CI pipeline.

```yaml
name: Trunk Code Quality
on:
  push:
    branches: main
  pull_request:
    branches: main

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # ... other setup steps
      - run: |
              curl -fsSLO --retry 3 https://trunk.io/releases/trunk 
              chmod +x trunk 
              ./trunk check --ci --ci-progress
      # ... other CI steps
```

#### Run nightly on GitHub Actions

To run Trunk’s [GitHub action](https://github.com/trunk-io/trunk-action) to lint your entire code base nightly or on a schedule, you can specify the \`check-mode: all\` argument when running the action.

```yaml
name: Trunk Code Quality
on:
  schedule:
    # Run at 4 PM UTC daily (cron uses UTC time)
    - cron: '0 16 * * *'
	
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # ... other setup steps
      - name: Trunk Code Quality
        uses: trunk-io/trunk-action@v1
        with:
    		check-mode: all
      # ... other CI steps
```

#### Run nightly using other CI providers

Specify the `--all` flag on your `trunk check` command to run on your entire codebase. Trunk is Git aware and checks only files changed in a PR by default. Specifying `--all` will instead check the whole code base.

```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk 
chmod +x trunk 
./trunk check --all --ci --ci-progress
```

Here’s an example of the command in a GitHub Actions workflow. This command will also work in any other CI provider.

```yaml
name: Trunk Code Quality
on:
  schedule:
    # Run at 4 PM UTC daily (cron uses UTC time)
    - cron: '0 16 * * *'
	
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # ... other setup steps
      - run: |
              curl -fsSLO --retry 3 https://trunk.io/releases/trunk 
              chmod +x trunk 
              ./trunk check --all --ci --ci-progress
      # ... other CI steps
```

### Caching

You can cache Trunk’s binary and install tools to speed up your CI runs. Trunk caches the version of `trunk` itself, linters, formatters, and lint results in the `~/.cache/trunk` folder. Consult the documentation for your CI provider to learn about caching this folder.
