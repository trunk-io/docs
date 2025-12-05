---
hidden: true
---

# Nightly report (Deprecated)

{% hint style="danger" %}
**Deprecation Warning**\
The Trunk Code Quality web app, Code Quality on PRs, and Code Quality Nightly will soon be deprecated. Follow our [migration guide](../prevent-new-issues/migration-guide.md) to migrate off these features.
{% endhint %}

Trunk Code Quality can post its results to the [Trunk Code Quality web app](https://app.trunk.io/login?intent=code%20quality). This allows you to view your repository's Code Quality history over time, track quality trends, and browse issues to help prioritize fixes.

### Connect your Trunk organization to GitHub

Sign up at [app.trunk.io](https://app.trunk.io/signup?intent=code%20quality), create a Trunk organization, and connect it to your repositories. You will need to grant the following GitHub App permissions.

{% @supademo/embed demoid="HXyBmoBn0_OX9Xite2fqd" url="https://app.supademo.com/demo/HXyBmoBn0_OX9Xite2fqd" %}

### Set Up Trunk Code Quality

Once your Trunk organization is connected to GitHub, create a .trunk repo in your account or organization and grant Trunk permissions to access the repo. The .trunk repo will hold the workflows to scan your codebase and pull requests. [Learn more about the .trunk repo](github-integration.md#uploading-results).

{% @supademo/embed demoid="pRr_eDzh-klIQdK_yW3se" url="https://app.supademo.com/demo/pRr_eDzh-klIQdK_yW3se" %}

### Configure Slack Notifications (optional)

If you would like to receive notifications for new issues Trunk finds in your repo, you can configure Trunk to be connected to Slack.

{% @supademo/embed demoid="cllpdjqhy1jf1051a1nff1a3y" url="https://app.supademo.com/demo/cllpdjqhy1jf1051a1nff1a3y" %}

### **How Trunk Uploads Results**

The upload feature of Trunk Code Quality will upload all of the issues found by Trunk to the Trunk services. To get an accurate picture of the state of your repository, you'll want to upload all of the Trunk Code Quality issues for your whole repository.

Generally, this is done within your Continuous Integration system (CI) automatically whenever **pull requests are filed or pushed to a specific branch** in your repo. Trunk Code Quality can also **run periodically** to check for new vulnerabilities in your dependencies.

#### **How Does It Work?**

Under the hood, the GitHub integration does the following for your organization to enable Trunk Code Quality in GitHub Actions Workflows:

* An installation of the Trunk.io GitHub app in your GitHub organization
* A `.trunk` repository in your GitHub organization.

#### **What is a `.trunk` repository?**

The `.trunk` repository contains the workflows run to scan your codebase and pull requests. We recommend creating a `.trunk` repository in your GitHub organization using [this template repository](https://github.com/trunk-io/.trunk-template).

Your `.trunk` repository must be added to your Trunk GitHub app installation. You can verify this by navigating to: `https://github.com/organizations/<your_organization>/settings/installations`, clicking "configure" next to Trunk-io, and verifying that the repository access is either "All repositories" or that your `.trunk` repository is selected.

To find Code Quality issues in your repositories and pull requests, we dispatch GitHub Actions workflows in your `.trunk` repository, which checks out your repositories and pull requests and then run `trunk check` in them. This strategy allows you to:

* start using Trunk Code Quality in all your repositories without any configuration, and
* be in full control over the environment where we analyze your code, since we're running on your GitHub Actions runners.

{% hint style="info" %}
🚧 `.trunk` should have private visibility

Since we use workflow runs in `.trunk` to analyze any repository in your organization and record Code Quality findings, you should think carefully about who has permission to view workflow runs in your `.trunk` repository. For most organizations, simply making your `.trunk` repository private will be sufficient.
{% endhint %}

#### (optional) Custom setup logic

If you need to do some setup before `trunk check` runs in `your-org/your-repo`, you can [define a GitHub composite action](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) in `.trunk/setup-ci/action.yaml` in `your-repo`. This can be important if, for example, a linter needs some generated code to be present before it can run:

```yaml
name: Trunk Code Quality setup
description: Set up dependencies for Trunk Code Quality

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
