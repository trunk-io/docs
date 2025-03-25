---
description: Configure Flaky Tests using Travis CI
---

# Travis CI

Trunk Flaky Tests integrates with your CI by adding a step in your Travis CI Pipelines to upload tests with the [Trunk Uploader CLI](../../uploader.md).

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

### Add the Trunk Token as a Secret

Store the Trunk slug and API token obtained in the previous step as new secrets named `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add a script step after running tests in each of your CI jobs that run tests. This should be run on pull requests, as well as from jobs that run on your main or [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/you-must-upload-tests-from-....md" %}

#### Example Travis CI Workflow

The following is an example of a Travis CI workflow step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [Test Frameworks](https://docs.trunk.io/flaky-tests/frameworks) docs.

{% hint style="info" %}
Note that TravisCI requires a recent version of Linux to use the current NodeJS runtimes. You may need to set the `dist` to `jammy` or later. See this [forum note](https://travis-ci.community/t/node-lib-x86-64-linux-gnu-libm-so-6-version-glibc-2-27-not-found-required-by-node/13655/2) for more details.
{% endhint %}

{% tabs %}
{% tab title="XML" %}
```yaml
language: node_js
dist: jammy
node_js:
  - 20
script:
  - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
  - ./trunk flakytests upload --junit-paths "<XML_GLOB_PATH>" --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
```
{% endtab %}

{% tab title="Bazel" %}
```yaml
language: node_js
dist: jammy
node_js:
  - 20
script:
  - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
  - ./trunk flakytests upload --bazel-bep-path <BEP_JSON_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
```
{% endtab %}

{% tab title="XCode" %}
```yaml
language: node_js
dist: jammy
node_js:
  - 20
script:
  - curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
  - ./trunk flakytests upload --xcresults-path <XCRESULT_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN
```
{% endtab %}
{% endtabs %}

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.
