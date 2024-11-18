---
description: >-
  How to integrate Trunk Code Quality into CI for GitLab and other non-GitHub
  providers, or for GitHub without using the Trunk GitHub App
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Manual Setup

{% hint style="info" %}
If you use GitHub, we recommend you follow the [GitHub Integration](get-started.md) guide.
{% endhint %}

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
If your default branch is named something else (e.g. `master`), you should `fetch` that branch inst
{% endhint %}
{% endtab %}

{% tab title="Other Providers" %}
`trunk check --ci` will work on any CI provider.

You may also want to specify `--upstream` if, for example, your PRs are not merged into your default branch, but into a `develop` branch.
{% endtab %}
{% endtabs %}

## Caching and Persistence

* Trunk caches the version of `trunk` itself, linters, formatters, and lint results, in `~/.cache/trunk`
* If your build machines are persistent, make sure this directory is not wiped out between CI jobs for best performance. If Trunk has to re-download every linter for every job because this directory is wiped out, it will be very slow.
* If your build machines are ephemeral, there are a few options for caching:
  * CI systems have support for caching between CI jobs on ephemeral runners:
    * [GitHub Actions](https://github.com/actions/cache)
    * [CircleCI](https://circleci.com/docs/caching/)
    * [Travis CI](https://docs.travis-ci.com/user/caching/)
  * You can include a seeded trunk cache in a regularly updated image used for CI by running `trunk check download`, which will download all requirements to `~/.cache/trunk`

## Running `trunk check` on Hourly/Nightly Builds

If you'd like to setup `trunk check` to run on a hourly/nightly CI run or release branch we recommend running with the following command:

```bash
trunk check --all --ci-progress --monitor=false
```

`--ci-progress` will print out the tool's progress every 30 seconds, whereas `--no-progress` will suppress any progress reporting.

You can also explicitly set the upstream branch if needed via `--upstream`, but we do detect your main branch by default.

### Uploading Results From Hourly/Nightly Builds

Trunk Code Quality has the ability to post its results to [app.trunk.io](https://app.trunk.io/login/?intent=code+quality). This will enable you to view your repository's Code Quality history over time so you can track the trend of issues in your code, as well as browse the issues in your repository to help you understand which issues should be prioritized to fix.

In order to keep the data up-to-date, you should upload Trunk Code Quality results regularly in an automated fashion. Depending on the size of your repository and the linters you have configured to run, running Trunk Code Quality on your whole repository may take a while. Because this run may take a while, we recommend uploading Trunk Code Quality results once daily. However, the system supports uploading results for every commit, so the granularity of upload is up to you.

### Running `trunk check --upload`

{% hint style="info" %}
Before running `trunk check --upload` you must have [connected your Github repository to your Trunk account](get-started.md).
{% endhint %}

#### CI Setup for nightly uploads

You can use the [Trunk GitHub Action](https://github.com/marketplace/actions/trunk-check) to upload results nightly for your main branch. You can provide it with a `trunk-token` by navigating to Settings → Repositories → {your repository} and clicking "View Api Token".

Example nightly workflow to upload results: [`nightly.yaml`](https://github.com/trunk-io/trunk-action/blob/main/.github/workflows/nightly.yaml)

#### Running `trunk check --upload` locally

1. `trunk check --upload` is different than a normal `trunk check` invocation because we explicitly want the Trunk CLI to find all of the issues in the repository. Because of this, we recommend adding the `--all` flag to your `trunk check --upload` invocation. Keep in mind, this won't override the ignore settings in your `trunk.yaml` file. Any linter or file-level ignores you have configured will be honored by `trunk check --upload`.
2. `trunk check --upload` accepts the same flags and filters as `trunk check` that you run locally and for CI, and it also has the same runtime dependencies.
3. You should run your `trunk check --upload` command locally without the `--upload` flag to verify that it is working as expected. If you have a large repository or many checks enabled, `--all` may take a long time. In this case, remember to use `--sample`.
4. Required command line parameters
   1. `--token`: The Trunk API token for this repository. You can find this by navigating to Settings → Repositories → {your repository} and clicking "View Api Token".
   2. `--series`: This is the name of the time-series this upload run is a part of. We recommend using the name of the branch you are running `trunk check` on. For example, we run `trunk check --upload` regularly on our `main` branch, so we use `--series main`. You may instead prefer to track specific releases or tags, or create an experimental series. The series name does not need to match any git object, it is available as a way to organize your upload data. If you're unsure of what to use for `--series`, just use the name of your main branch (typically `main` or `master`)

```bash
trunk check --all --upload --series main --token REDACTED
```

#### Troubleshooting

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
