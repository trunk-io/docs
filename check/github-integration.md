---
description: >-
  Trunk Check integrates with GitHub to automatically identify linter issues,
  unformatted files, and vulnerabilities in your repositories without ever
  sending your code to Trunk.
---

# GitHub Integration

{% hint style="info" %}
If you don't use GitHub, we recommend you check out the [Continuous Integration](continuous-integration.md) guide.
{% endhint %}

## How it works

Trunk Check's GitHub integrations rely on the following:

* An installation of the Trunk.io GitHub app in your GitHub organization, and
* A `.trunk` repository in your GitHub organization.

### What is a `.trunk` repository?

The `.trunk` repository contains the workflows run to scan your codebase and pull requests. We recommend creating a `.trunk` repository in your GitHub organization using [this template repository](https://github.com/trunk-io/.trunk-template).

Your `.trunk` repository must be added to your Trunk GitHub app installation. You can verify this by navigating to: `https://github.com/organizations/<your_organization>/settings/installations`, clicking "configure" next to Trunk-io, and verifying that the repository access is either "All repositories" or that your `.trunk` repository is selected.

To find Check issues in your repositories and pull requests, we dispatch GitHub Actions workflows in your `.trunk` repository, which check out your repositories and pull requests and then run `trunk check` in them. This strategy allows you to:

* start using Trunk Check in all your repositories without any configuration, and
* be in full control over the environment where we analyze your code, since we're running on your GitHub Actions runners.

> 🚧 `.trunk` should have private visibility
>
> Since we use workflow runs in `.trunk` to analyze any repository in your organization and record Check findings, you should think carefully about who has permissions to view workflow runs in your `.trunk` repository. For most organizations, simply making your `.trunk` repository private will be sufficient.

If you want to version the linter configuration for a given repo or enable linters that require more manual configuration, you can always [create and commit your Trunk configuration in said repository](get-started-cli.md).

## Checking pull requests

Trunk Check can automatically detect new Check issues on your pull requests and flag them so that you can prevent pull requests from introducing any new issues in your repository.

When running on a pull request, Trunk Check will only flag _new_ issues, not existing ones, so that your engineers don't have to fix pre-existing linter issues in every file they touch - this is the same [hold-the-line technology](./#hold-the-line) that our VSCode extension and CLI use.

> 📘 Skipping Trunk Check
>
> You can include `/trunk skip-check` in the body of a PR description (i.e. the first comment on a given PR) to mark Trunk Check as "skipped". This will allow the PR to pass a GitHub required status check on `Trunk Check`.
>
> This can be helpful if Check is flagging known issues in a given PR which you don't want to [ignore](ignoring-issues.md), which if you're doing a large refactor, can come in very handy.

If you don't want Trunk Check to run on pull requests, turn it off in [your repository's settings](https://app.trunk.io).

## Scanning your repository

Trunk Check can scan your repository for Check issues on a daily cadence, upload them to Trunk for you to review at your convenience, and notify you via Slack whenever new issues are discovered in your repository.

This allows you to build confidence in the code health of your repositories:

* You will be alerted quickly in a Heartbleed-type event, giving you assurances about whether or not a newly discovered vulnerability affects any of your repositories, and
* You can monitor how many Check issues exist in each of your repositories and make data-driven decisions about prioritizing efforts to reduce tech debt

If you don't want Trunk Check to scan your repository on a daily cadence or notify you, you can turn it off in [your repository's settings](https://app.trunk.io).

## (optional) Custom setup logic

If you need to do some setup before `trunk check` runs in `your-org/your-repo`, you can [define a GitHub composite action](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) in `.trunk/setup-ci/action.yaml` in `your-repo`. This can be important if, for example, a linter needs some generated code to be present before it can run:

```yaml
name: Trunk Check setup
description: Set up dependencies for Trunk Check

runs:
  using: composite
  steps:
    - name: Build required trunk check inputs
      shell: bash
      run: bazel build ... --build_tag_filters=pre-lint
      
    - name: Install eslint dependencies
      shell: bash
      run: npm install
```

Read more in the documentation for [our GitHub Action](https://github.com/trunk-io/trunk-action#custom-setup).
