# Continuous Integration

Once setup in your repo, Trunk can run on any CI system and post inline annotations on your GitHub Pull Requests.

### Running `trunk check` on GitHub Pull Requests

Running on CI differs a bit depending on your CI system:

#### On GitHub Actions

Use our GitHub Action as a step in one of your workflows triggered on pull requests: [https://github.com/marketplace/actions/trunk-check](https://github.com/marketplace/actions/trunk-check)

#### On Gitlab CI

Gitlab performs a shallow clone by default which limits trunk's ability to detect the upstream commit to compute changes from. This is easily solved by simply fetching your main branch before running `trunk`:

```bash
git fetch origin main
trunk check --ci
```

> Note: if your default branch is named something else (such as `master`), you should fetch that instead of `main`.

#### On other CI systems

**Without inline annotations**

You can always run `trunk check` directly on CI. We recommend running with these flags:

```bash
trunk check --ci
```

You can additionally pass a `--upstream` branch if needed (for example, if your PR is not merging to your main branch, your CI system may have an environment variable indicating what the upstream branch should be).

**With inline annotations**

Trunk is capable of posting inline annotations to GitHub from any CI system, if you provide your own `GITHUB_TOKEN` from your own GitHub app. This requires passing trunk some additional information:

```bash
trunk check \
  --ci \
  --github-repository <your_owner/your_repo> \
  --github-commit "$(git rev-parse HEAD)" \
  --github-annotate
```

`--github-repository` should be set to the owner/repo of the repo you're running trunk on. For example, if your github repository is `https://github.com/some_org/some_repo/`, then this should be set to `some_org/some_repo`.

We also we require the `GITHUB_TOKEN` environment variable to be set to a valid GitHub token that has read/write permissions for check runs on your repository.

By default, the details URL for your annotation will point to `https://trunk.io/check/ci` (this page). You can override this value with the flag `--github-annotate-details-url`, if you prefer.

**Jenkins**

Jenkins now supports [GitHub App authentication](https://www.jenkins.io/blog/2020/04/16/github-app-authentication/) via the [GitHub Branch Source Plugin](https://github.com/jenkinsci/github-branch-source-plugin)(installed by default, so you likely already have it).

Please follow [this Jenkins guide](https://github.com/jenkinsci/github-branch-source-plugin/blob/master/docs/github-app.adoc) to get a `GITHUB_TOKEN` in a Jenkins step. Refer to the Jenkins guide for full details, but here's an overview of the process:

1. Create a GitHub App (or use an existing one). It needs `Read and Write` access to `Checks`.
2. Install it in your GitHub org, and give it permissions to your repo(s).
3. Create & download a `Private Key` for your GitHub App (bottom of the [GitHub App](https://github.com/settings/apps) settings page)
4. Add credentials to Jenkins in the Jenkins UI, of type `GitHub App`, using the `Private Key` you downloaded (convert the key to pkcs8 first - [docs](https://github.com/jenkinsci/github-branch-source-plugin/blob/master/docs/github-app.adoc))
5. Use your GitHub app credentials in a Jenkins step to run `trunk check` via:

```bash
withCredentials([usernamePassword(credentialsId: 'githubapp-jenkins',
                                  usernameVariable: 'GITHUB_APP',
                                  passwordVariable: 'GITHUB_TOKEN')]) {
  sh '''
  trunk check \
    --ci \
    --github-repository <your_owner/your_repo> \
    --github-commit "$(git rev-parse HEAD)" \
    --github-annotate
  '''
}
```

#### Caching / Persistence

* Trunk caches the version of trunk itself, linters, formatters, and lint results, in `~/.cache/trunk`
* If your build machines are persistent, make sure this directory is not wiped out between CI jobs for best performance. If Trunk has to re-download every linter for every job because this directory is wiped out, it will be very slow.
* If your build machines are ephemeral, there are a few options for caching:
  * CI systems have support for caching between CI jobs on ephemeral runners:
    * [GitHub Actions](https://github.com/actions/cache)
    * [CircleCI](https://circleci.com/docs/2.0/guides/caching/)
    * [Travis CI](https://docs.travis-ci.com/user/caching/)
  * You can include a seeded trunk cache in a regularly updated image used for CI by running `trunk check download`, which will download all requirements to `~/.cache/trunk`

### Bypass `trunk check` on a Pull Request

Sometimes you need to bypass a failing `trunk check` job on an individual pull request. To bypass the failing pull request add `/trunk skip-check` as a comment or in the description of the pull request before Trunk Check runs (if it has already run, restart it).

> Note:`trunk check` will still run in this case and report issues, but the job will always return a passing exit code.

### Running `trunk check` on hourly/nightly builds

If you'd like to setup `trunk check` to run on a hourly/nightly CI run or release branch we recommend running with the following command:

```bash
trunk check --ci-progress --monitor=false
```

`--ci-progress` will print out the tool's progress every 30 seconds, whereas `--no-progress` will suppress any progress reporting.

You can also explicitly set the upstream branch if needed via `--upstream`, but we do detect your main branch by default.
