# TeamCity

Trunk Flaky Tests integrates with your CI by adding a step in your TeamCity Pipelines to upload tests with the [Trunk Uploader CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

### Add the Trunk Token as a Secret

Store the Trunk slug and API token obtained in the previous step in your TeamCity project by navigating to **Admin > Build > Parameters > Add new parameter** and adding new environment variables as `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an upload step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/you-must-upload-tests-from-....md" %}

#### Add Uploader to a Build Step

Add the following command as a build step after your test run to upload test results. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

{% tabs %}
{% tab title="XML" %}
```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk
chmod +x ./trunk
./trunk flakytests upload --junit-paths "<XML_GLOB_PATH>" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token $TRUNK_TOKEN
```
{% endtab %}

{% tab title="Bazel" %}
```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk
chmod +x ./trunk
./trunk flakytests upload --bazel-bep-path <BEP_JSON_PATH> \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token $TRUNK_TOKEN
```
{% endtab %}

{% tab title="XCode" %}
```sh
curl -fsSLO --retry 3 https://trunk.io/releases/trunk
chmod +x ./trunk
./trunk flakytests upload --xcresults-path <XCRESULT_PATH> \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token $TRUNK_TOKEN
```
{% endtab %}
{% endtabs %}

In your build step settings under the **Show advanced options** toggle, find the **Execute step settings** and select `Always, even if build stop command was issued` to ensure that the Upload step will still run if tests have failed.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [Test Frameworks](https://docs.trunk.io/flaky-tests/frameworks) docs.

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

You can do this in TeamCity by omitting your JUnit XML path in the saved artifacts. [Learn more about artifacts in TeamCity](https://www.jetbrains.com/help/teamcity/cloud/configure-and-run-your-first-build.html#Artifacts).
