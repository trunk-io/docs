---
description: >-
  How to integrate Trunk Check into CI for non-GitHub providers, or for GitHub
  without using the Trunk GitHub App
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

# Non-GitHub Integration

{% hint style="info" %}
If you use GitHub, we recommend you follow the [GitHub Integration](../get-started/github-integration.md) guide.
{% endhint %}

{% tabs %}
{% tab title="All" %}
`trunk check --ci` will work on any CI provider.

You may also want to specify `--upstream` if, for example, your PRs are not merged into your default branch, but into a `develop` branch.
{% endtab %}

{% tab title="Gitlab" %}
Gitlab performs a shallow clone by default which limits trunk's ability to detect the upstream commit to compute changes from. This is easily solved by simply fetching your main branch before running `trunk`:

```bash
git fetch origin main
trunk check --ci
```

{% hint style="info" %}
If your default branch is named something else (e.g. `master`), you should `fetch` that branch inst
{% endhint %}
{% endtab %}
{% endtabs %}

## Caching and Persistence

* Trunk caches the version of `trunk` itself, linters, formatters, and lint results, in `~/.cache/trunk`
* If your build machines are persistent, make sure this directory is not wiped out between CI jobs for best performance. If Trunk has to re-download every linter for every job because this directory is wiped out, it will be very slow.
* If your build machines are ephemeral, there are a few options for caching:
  * CI systems have support for caching between CI jobs on ephemeral runners:
    * [GitHub Actions](https://github.com/actions/cache)
    * [CircleCI](https://circleci.com/docs/2.0/guides/caching/)
    * [Travis CI](https://docs.travis-ci.com/user/caching/)
  * You can include a seeded trunk cache in a regularly updated image used for CI by running `trunk check download`, which will download all requirements to `~/.cache/trunk`

## Running `trunk check` on hourly/nightly builds

If you'd like to setup `trunk check` to run on a hourly/nightly CI run or release branch we recommend running with the following command:

```bash
trunk check --all --ci-progress --monitor=false
```

`--ci-progress` will print out the tool's progress every 30 seconds, whereas `--no-progress` will suppress any progress reporting.

You can also explicitly set the upstream branch if needed via `--upstream`, but we do detect your main branch by default.
