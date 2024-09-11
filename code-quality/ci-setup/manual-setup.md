# Manual Setup

{% hint style="warning" %}
If you use GitHub, we recommend you follow the GitHub Integration guide. If you don't use GitHub or cannot install the Trunk GitHub app, you can still run Trunk Code Quality using these manual setup steps.
{% endhint %}

### Running Trunk Code Quality on PRs

{% tabs %}
{% tab title="GitHub Actions" %}
If you're using GitHub but wish to setup up your own GitHub Actions Workflows, you can use the provided [Trunk GitHub Action](https://github.com/marketplace/actions/trunk-check).

```yaml
name: Linter
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
      - name: Trunk Check
        uses: trunk-io/trunk-action@v1
        with:
          post-annotations: true
      # ... other CI steps
```
{% endtab %}

{% tab title="GitLab" %}
GitLab performs a shallow clone by default which limits trunk's ability to detect the upstream commit to compute changes from. This is easily solved by simply fetching your main branch before running `trunk`:

```bash
git fetch origin main
trunk check --ci
```

{% hint style="info" %}
If your default branch is named something else (e.g. `master`), you should `fetch` that branch instead
{% endhint %}
{% endtab %}

{% tab title="Other Providers" %}
`trunk check --ci` will work on any CI provider.

You may also want to specify `--upstream` if, for example, your PRs are not merged into your default branch, but into a `develop` branch.
{% endtab %}
{% endtabs %}

#### Caching and Persistence

* Trunk caches the version of `trunk` itself, linters, formatters, and lint results, in `~/.cache/trunk`
* If your build machines are persistent, make sure this directory is not wiped out between CI jobs for best performance. If Trunk has to re-download every linter for every job because this directory is wiped out, it will be very slow.
* If your build machines are ephemeral, there are a few options for caching:
  * CI systems have support for caching between CI jobs on ephemeral runners:
    * [GitHub Actions](https://github.com/actions/cache)
    * [CircleCI](https://circleci.com/docs/caching/)
    * [Travis CI](https://docs.travis-ci.com/user/caching/)
  * You can include a seeded trunk cache in a regularly updated image used for CI by running `trunk check download`, which will download all requirements to `~/.cache/trunk`

#### Running `trunk check` on Hourly/Nightly Builds

If you'd like to setup `trunk check` to run on a hourly/nightly CI run or release branch we recommend running with the following command:

```bash
trunk check --all --ci-progress --monitor=false
```

`--ci-progress` will print out the tool's progress every 30 seconds, whereas `--no-progress` will suppress any progress reporting.

You can also explicitly set the upstream branch if needed via `--upstream`, but we do detect your main branch by default.

### Uploading results to the Trunk web app

{% hint style="info" %}
After your first upload to the Trunk Web App _without_ the Trunk GitHub App installed, you'll see the web app populate and be aware of the repo you uploaded from. We don't send or store your repo in the Trunk backend, see [security.md](../security.md "mention") for more info.
{% endhint %}

Trunk Code Quality has the ability to post its results to [app.trunk.io](https://app.trunk.io). This will enable you to view your repository's Code Quality history over time so you can track the trend of issues in your code, as well as browse the issues in your repository to help you understand which issues should be prioritized to fix.

In order to keep the data up-to-date, you should upload Trunk Code Quality results regularly in an automated fashion. Depending on the size of your repository and the linters you have configured to run, running Trunk Code Quality on your whole repository may take a while. Because this run may take a while, we recommend uploading Trunk Code Quality results once daily. However, the system supports uploading results for every commit, so the granularity of upload is up to you.

**Uploading using the** [**Trunk GitHub Action**](https://github.com/trunk-io/trunk-action)

By providing a `trunk-token` (as seen below) and running on a `schedule` workflow dispatch ([example](https://github.com/trunk-io/trunk-action/blob/main/.github/workflows/nightly.yaml)), Trunk will infer to run with `check-mode` as `all` and to upload results to Trunk.

```yaml
- name: Trunk Check
  uses: trunk-io/trunk-action@v1
  with:
    trunk-token: ${{ secrets.TRUNK_TOKEN }}
```

Note: When run as a periodic workflow on a branch, Trunk will automatically infer `check-mode` to be `all`.

**Uploading without using the** [**Trunk GitHub Action**](https://github.com/trunk-io/trunk-action)

In a nightly CI job, run:

```bash
trunk check --all --upload --series main --token REDACTED
```

Notes:

1. `trunk check --upload` is different than a normal `trunk check` invocation because we explicitly want the Trunk CLI to find all of the issues in the repository. Because of this, we recommend adding the `--all` flag to your `trunk check --upload` invocation. Keep in mind, this won't override the ignore settings in your `trunk.yaml` file. Any linter or file-level ignores you have configured will be honored by `trunk check --upload`.
2. `trunk check --upload` accepts the same flags and filters as `trunk check` that you run locally and for CI, and it also has the same runtime dependencies.
3. You should run your `trunk check --upload` command locally without the `--upload` flag to verify that it is working as expected. If you have a large repository or many checks enabled, `--all` may take a long time. In this case, remember to use `--sample`.
4. Required command line parameters
   1. `--token`: The Trunk API token for this repository. You can find this by navigating to Settings → Repositories → {your repository} and clicking "View Api Token". Alternatively, you can use the Trunk API token for your organization, by navigating to Settings and clicking "View Organization API Token". This will allow you to upload results without first connecting your GitHub repository to Trunk.
   2. `--series`: This is the name of the time-series this upload run is a part of. We recommend using the name of the branch you are running `trunk check` on. For example, we run `trunk check --upload` regularly on our `main` branch, so we use `--series main`. You may instead prefer to track specific releases or tags, or create an experimental series. The series name does not need to match any git object, it is available as a way to organize your upload data. If you're unsure of what to use for `--series`, just use the name of your main branch (typically `main` or `master`)

**Troubleshooting**

Normally we infer repo information from the `origin` remote, however if you don't have an `origin` or for another git configuration reason it can't be inferred, it can be explicitly defined in `trunk.yaml`:

1. Add a `repo` section to your Trunk config. This allows the Trunk CLI to connect with the appropriate repository in the Trunk system.
   1. `host`: Where your repository is hosted. Currently only Github is supported, so this value should be `github.com`,
   2. `owner`: The Github Owner of the repository, typically the first path section of your repository URL. For example, if we were connecting with [https://github.com/google/googletest](https://github.com/google/googletest), the `owner` would be `google`.
   3. `name`: The name of the repository. Continuing with our example above, the `name` would be `googletest`.

This is what the `repo` section of your config would look like if your repository was hosted at [https://github.com/google/googletest](https://github.com/google/googletest)

```yaml
repo:
  repo:
    host: github.com
    owner: google
    name: googletest
```

Note the repo/repo nested structure.
