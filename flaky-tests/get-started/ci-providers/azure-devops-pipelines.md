# Azure DevOps Pipelines

Trunk Flaky Tests integrates with your CI by adding a step in your Azure DevOps Pipelines to upload tests with the [Trunk Uploader CLI](../../uploader.md).

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

{% include "../../../.gitbook/includes/trunk-organization-slug-and....md" %}

### Add the Trunk Token as a Secret

Store the Trunk slug and API token obtained in the previous step in your Azure DevOps Pipelines as new variables named `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an upload step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/you-must-upload-tests-from-....md" %}

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
    curl -fsSLO --retry 3 https://trunk.io/releases/trunk
    chmod +x ./trunk
    ./trunk flakytests upload --junit-paths "<XML_GLOB_PATH>" \
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
    curl -fsSLO --retry 3 https://trunk.io/releases/trunk
    chmod +x ./trunk
    ./trunk flakytests upload --bazel-bep-path <BEP_JSON_PATH> \
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
    curl -fsSLO --retry 3 https://trunk.io/releases/trunk
    chmod +x ./trunk
    ./trunk flakytests upload --xcresults-path <XCRESULT_PATH> \
    --org-url-slug $(TRUNK_ORG_SLUG) \
    --token $(TRUNK_TOKEN)
  condition: always() # this should always run
  displayName: Upload test results to Trunk.io
```
{% endtab %}
{% endtabs %}

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

[Learn more about cleaning up artifacts in Azure DevOps Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/pipeline-options-for-git?view=azure-devops\&tabs=yaml#clean-the-local-repo-on-the-agent)

{% include "../../../.gitbook/includes/have-questions-join-us-and-....md" %}

