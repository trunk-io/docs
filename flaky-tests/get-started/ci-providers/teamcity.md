# TeamCity

## Introduction

Trunk Flaky Tests integrates with your CI by uploading test results in each of your TeamCity pipeline steps with the [Trunk Uploader CLI](../../uploader.md).

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing JUnit XML output for your test runner, supported by virtually all test frameworks, which is what Trunk ingests.

### 1. Store a TRUNK\_TOKEN secret in your CI system

In [app.trunk.io](https://app.trunk.io/login/?intent=flaky+tests), navigate to:

**Settings > Organization > Manage > Organization API Token > View Organization API Token > View**

Store your API Token in your TeamCity project by navigating to **Admin > Build > Parameters > Add new parameter** and adding a new environment variable named `TRUNK_TOKEN`. Make sure you are getting your _organization token_, not your project/repo token.

### 2. Grab your Organization Slug

To upload test results to Trunk, you'll need to pass a **Trunk Organization Slug** to the upload command. To get your organization slug, In [app.trunk.io](https://app.trunk.io/login/?intent=flaky+tests), navigate to:

**Settings > Organization > Manage > Organization Name > Slug**

Your slug can just be pasted directly into your CI workflow; it's not a secret. In the example workflow in the next step, replace `TRUNK_ORG_SLUG` with your actual organization slug.

### 3. Modify workflows to upload test results

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your [stable branches](../../detection.md#stable-branches), for example, `main`, `master`, or `develop`.

#### Add Uploader to a Build Step

Add the following command as a build step after your test run to upload test results. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

```yaml
curl -fsSLO --retry 3 https://trunk.io/releases/trunk
chmod +x ./trunk
./trunk flakytests upload --junit-paths "**/junit.xml" \
    --org-url-slug <TRUNK_ORG_SLUG> \
    --token $TRUNK_TOKEN
```

In your build step settings under the **Show advanced options** toggle, find the **Execute step settings** and select `Always, even if build stop command was issued` to ensure that the Upload step will still run if tests have failed.&#x20;

To find out how to produce the JUnit XML files the uploader needs, see the instructions for your test framework in the [Test Frameworks](https://docs.trunk.io/flaky-tests/frameworks) docs.

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

You can do this in TeamCity by omitting your JUnit XML path in the saved artifacts. [Learn more about artifacts in TeamCity](https://www.jetbrains.com/help/teamcity/cloud/configure-and-run-your-first-build.html#Artifacts).

#### Need Help?

Join the [Trunk Slack Community](https://slack.trunk.io) for live support.
