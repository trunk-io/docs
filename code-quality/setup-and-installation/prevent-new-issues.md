# Linting in CI

Trunk Code Quality can be run in CI to prevent new issues form being introduced by PRs and on a nightly/scheduled cadence to report on existing issues.

### Configuring base branch

Trunk operates in **hold-the-line** mode by default. This means Trunk will run linters only on the **files that have changed** according to Git, by comparing it to the appropriate upstream branch.

If you're not using `main` or `master` as the base branch, make sure it's specified in `.trunk/trunk.yaml`.

```yaml
version: 0.1
cli:
  version: 1.22.2
repo:
  # specify the base branch for hold-the-line
  trunk_branch: develop
```

### Linting on pull requests

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
        with:
          post-annotations: true 
      # ... other CI steps
```

This step will automatically run Trunk Code Quality to reveal problems found when comparing the branch to `main` or another base branch you configured.

If you want to run the `trunk check` command directly in your workflow, or you're not using GitHub, you can run the following commands:

<pre><code><strong>curl -fsSLO --retry 3 https://trunk.io/releases/trunk \
</strong>chmod +x trunk \
./trunk check --ci
</code></pre>

Trunk Code Quality can be run in CI to prevent new issues form being introduced by PRs and on a nightly/scheduled cadence to report on existing issues.

### Configuring base branch

Trunk operates in **hold-the-line** mode by default. This means Trunk will run linters only on the **files that have changed** according to Git, by comparing it to the appropriate upstream branch.

If you're not using `main` or `master` as the base branch, make sure it's specified in `.trunk/trunk.yaml`.

```yaml
version: 0.1
cli:
  version: 1.22.2
repo:
  # specify the base branch for hold-the-line
  trunk_branch: develop
```

### Linting on pull requests

#### GitHub Actions Workflows

If you're already running linters on your PRs, you can replace your lint step with the [Trunk Code Quality action](https://github.com/trunk-io/trunk-action) step. For example:

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
        with:
          post-annotations: true 
      # ... other CI steps
```

This step will automatically run Trunk Code Quality to reveal problems found when comparing the branch to `main` or another base branch you configured.

When `post-annotations` is set to `true` Code Quality will also **annotate** the PR with comments for where lint issues are found.

<figure><img src="../../.gitbook/assets/Annotations.png" alt=""><figcaption><p>Example of inline annotations</p></figcaption></figure>

#### Manual configuration and Non-GitHub CI

If you want to run the `trunk check` command directly in your workflow, or you're not using GitHub, you can run the following commands:

```
curl -fsSLO --retry 3 https://trunk.io/releases/trunk \
chmod +x trunk \
./trunk check --ci
```

#### Skipping Trunk Code Quality on pull requests

You can include `/trunk skip-check` in the body of a PR description (i.e. the first comment on a given PR) to mark Trunk Code Quality as "skipped". Trunk Code Quality will still run on your PR and report issues, but this will allow the PR to pass a GitHub-required status check on `Trunk Check`.

This can be helpful if Code Quality is flagging known issues in a given PR that you don't want to ignore, which can come in handy if you're doing a large refactor.

{% hint style="warning" %}
If you use GitHub, we recommend you follow the GitHub Integration guide. If you don't use GitHub or cannot install the Trunk GitHub app, you can still run Trunk Code Quality using these manual setup steps.
{% endhint %}

### Caching and persistence

* Trunk caches the version of `trunk` itself, linters, formatters, and lint results in `~/.cache/trunk`
* If your build machines are persistent, make sure this directory is not wiped out between CI jobs for best performance. If Trunk has to re-download every linter for every job because this directory is wiped out, it will be very slow.
* If your build machines are ephemeral, there are a few options for caching:
  * CI systems have support for caching between CI jobs on ephemeral runners:
    * [GitHub Actions](https://github.com/actions/cache)
    * [CircleCI](https://circleci.com/docs/caching/)
    * [Travis CI](https://docs.travis-ci.com/user/caching/)
  * You can include a seeded trunk cache in a regularly updated image used for CI by running `trunk check download`, which will download all requirements to `~/.cache/trunk`

{% hint style="warning" %}
If you use GitHub, we recommend you follow the GitHub Integration guide. If you don't use GitHub or cannot install the Trunk GitHub app, you can still run Trunk Code Quality using these manual setup steps.
{% endhint %}

### Hourly and nightly builds

If you'd like to set Code Quality to run on an hourly/nightly CI, you can run

<pre class="language-yaml"><code class="lang-yaml"><strong>name: Trunk Code Quality
</strong>on:
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
</code></pre>

You can do the same without Trunk's GitHub Action using the following command:

```bash
curl -fsSLO --retry 3 https://trunk.io/releases/trunk \
chmod +x trunk \
./trunk check --all --ci-progress --monitor=false
```

`--ci-progress` will print out the tool's progress every 30 seconds, whereas `--no-progress` will suppress any progress reporting.

You can also explicitly set the upstream branch if needed via `--upstream`, but we do detect your main branch by default.
