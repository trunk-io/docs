# Azure DevOps Pipelines

Trunk Flaky Tests integrates with your CI by adding a step in your Azure DevOps Pipelines to upload tests with the [Trunk Analytics CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

{% include "../../../.gitbook/includes/trunk-organization-slug-and....md" %}

### Add the Trunk Token as a Secret

Store the Trunk slug and API token obtained in the previous step in your Azure DevOps Pipelines as new variables named `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an upload step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your [stable branches](../../detection/), for example, `main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/stable-branches-hint.md" %}

#### Add Uploader to Testing Pipelines

The following is an example of a workflow step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [Test Frameworks](https://docs.trunk.io/flaky-tests/frameworks) docs.

{% tabs %}
{% tab title="XML" %}
```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
# ... Omitted steps

- script: |
    curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz
    chmod +x trunk-analytics-cli
    ./trunk-analytics-cli upload --junit-paths "<XML_GLOB_PATH>" \
    --org-url-slug $(TRUNK_ORG_SLUG) \
    --token $(TRUNK_TOKEN)
  condition: always() # this should always run
  displayName: Upload test results to Trunk.io
```
{% endtab %}

{% tab title="Bazel" %}
```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
# ... Omitted steps

- script: |
    curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz
    chmod +x trunk-analytics-cli
    ./trunk-analytics-cli upload --bazel-bep-path <BEP_JSON_PATH> \
    --org-url-slug $(TRUNK_ORG_SLUG) \
    --token $(TRUNK_TOKEN)
  condition: always() # this should always run
  displayName: Upload test results to Trunk.io
```
{% endtab %}

{% tab title="XCode" %}
```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
# ... Omitted steps

- script: |
    curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz
    chmod +x trunk-analytics-cli
    ./trunk-analytics-cli upload --xcresult-path <XCRESULT_PATH> \
    --org-url-slug $(TRUNK_ORG_SLUG) \
    --token $(TRUNK_TOKEN)
  condition: always() # this should always run
  displayName: Upload test results to Trunk.io
```
{% endtab %}

{% tab title="RSpec plugin" %}
```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
# ... Omitted steps

- script: |
    TRUNK_ORG_URL_SLUG=$(TRUNK_ORG_SLUG) \
    TRUNK_API_TOKEN=$(TRUNK_TOKEN) \
    bundle exec rspec
  displayName: Run RSpec tests and upload results to Trunk.io
```
{% endtab %}
{% endtabs %}

{% include "../../../.gitbook/includes/platform-hint.md" %}

{% include "../../../.gitbook/includes/stale-files-warning.md" %}

[Learn more about cleaning up artifacts in Azure DevOps Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/pipeline-options-for-git?view=azure-devops\&tabs=yaml#clean-the-local-repo-on-the-agent)

{% include "../../../.gitbook/includes/have-questions-join-us-and-....md" %}
