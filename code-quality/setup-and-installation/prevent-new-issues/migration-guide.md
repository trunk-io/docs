---
hidden: true
---

# Migration Guide

### What's deprecated

The Code Quality dashboard in the Trunk web app has been deprecated, along with the ability to configure and manage CI workflows in the web app.

This means the Code Quality tab in the Trunk web app has been deprecated.

<figure><img src="../../../.gitbook/assets/CQ Deprecation (2).png" alt=""><figcaption><p>The Code Quality tab in the Trunk Web App.</p></figcaption></figure>

This deprecation impacts the following Code Quality features configured in the web app:

* Checking for issues nightly.
* Checking for issues on pull requests.

**You can still run Code Quality in CI and on PRs.** See the [guide below](migration-guide.md#migrating-nightly-and-pr-jobs) for step-by-step migration instructions.

You only need to migrate if you have configured these features with the web app. You can check if you use these features through the web app in the Code Quality section of your repo settings.

<figure><img src="../../../.gitbook/assets/CQ Nightly Deprecation.png" alt=""><figcaption><p>You can check in the Code Quality settings of your repo to see if you're currently using deprecated features.</p></figcaption></figure>

Lastly, Trunk will no longer collect your linting issues. You will also stop receiving Slack notifications about new issues discovered by linters.

If you're using the `--upload` flag on your `trunk check` command, it will no longer work:

```
trunk check --upload --series=main
```

### Why we’re deprecating these features

From both usage data and community feedback, we know the core value of Code Quality is in the CLI, IDE, and native CI integrations. We’ve deprecated some features to better support these key integrations with limited resources.&#x20;

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

<figure><img src="../../../.gitbook/assets/CQ Deprecation (1).png" alt=""><figcaption><p>Inline linter errors and warnings as you review PRs. </p></figcaption></figure>

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

#### Turn off web app services after migrating

After you have migrated off the web app, you can manually turn off **Check for issues in pull requests** in your repo settings in the web app.

If you do not turn these off, you will continue to get warnings in your PRs until the services are shut down.

### Caching

You can cache Trunk’s binary and install tools to speed up your CI runs. Trunk caches the version of `trunk` itself, linters, formatters, and lint results in the `~/.cache/trunk` folder. Consult the documentation for your CI provider to learn about caching this folder.

### Limitations

Uploads and web reports based on Code Quality issues are no longer supported after this deprecation. These less-used features are deprecated so we can better maintain the core metalinter features of Code Quality. While an online report is no longer available, Trunk still produces standardized output by reformatting each linter’s output.

You will also stop receiving Slack notifications about new issues in your repo. Since Trunk no longer ingests uploads about your linter runs, it can’t send Slack notifications about them.

If you have additional questions or concerns, please reach out to us on [Slack](https://slack.trunk.io/).
