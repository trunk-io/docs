---
description: Configure Google Cloud Build to upload test results to Trunk Flaky Tests
---

# Google Cloud Build

Trunk Flaky Tests integrates with your CI by adding a step in your Google Cloud Build configuration to upload tests with the [Trunk Uploader CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

### Checklist

By the end of this guide, you should achieve the following.

* [ ] Get your Trunk organization slug and token
* [ ] Store your token in GCP Secret Manager
* [ ] Connect your GitHub repos to Cloud Build
* [ ] Create Cloud Build triggers for PR and push events
* [ ] Configure your `cloudbuild.yaml` to upload to Trunk
* [ ] Validate your uploads in Trunk

After completing these checklist items, you'll be integrated with Trunk.&#x20;

### Trunk Organization Slug and Token

Before setting up uploads to Trunk, you must sign in to [app.trunk.io](https://app.trunk.io/login?intent=flaky%20tests) and obtain your Trunk organization slug and token.

#### Trunk Slug

You can find your organization slug under **Settings > Organization > Manage > Organization Name > Slug**. You'll save this as a variable in CI in a later step.

#### Trunk Token

You can find your token under **Settings > Organization > Manage > Organization API Token > View Organization API Token > View**. Since this is a secret, do not leak it publicly. Ensure you get your _organization token_, not your project/repo token.

### Store the Trunk Token in GCP Secret Manager

Store your Trunk API token in [GCP Secret Manager](https://console.cloud.google.com/security/secret-manager) so Cloud Build can securely access it during builds.

1. Open **GCP Console > Secret Manager**.
2. Click **Create Secret**.
3. Name the secret (for example, `trunk-api-token`) and paste your Trunk organization API token as the value.
4. Click **Create**.

You'll reference this secret in your `cloudbuild.yaml` using the `availableSecrets` and `secretEnv` fields.

### Connect GitHub Repos to Cloud Build

Ensure your GitHub repositories are connected to Cloud Build through the [Cloud Build GitHub App](https://cloud.google.com/build/docs/automating-builds/github/connect-repo-github).

1. Open **GCP Console > Cloud Build > Repositories**.
2. Connect your GitHub repository using the Cloud Build GitHub App.

### Create Cloud Build Triggers

Create two Cloud Build triggers for each repository you want to upload test results from:

1. Open **GCP Console > Cloud Build > Triggers**.
2. Create a trigger for **pull request events** — this uploads test results from PR branches.
3. Create a trigger for **push events** to your stable branch (for example, `main`) — this uploads test results from your stable branch.

{% hint style="danger" %}
It is important to upload test results from CI runs on [**stable branches**](../../detection.md#stable-branches), such as `main`, `master`, or `develop`. This will give you a stronger signal about the health of your code and tests.

Trunk can also detect test flakes on PR and merge branches. To best detect flaky tests, it is recommended to upload test results from stable, PR, and merge branch CI runs.

[Learn more about detection](../../detection.md)
{% endhint %}

### Upload to Trunk

Add an upload step in your `cloudbuild.yaml` that runs after your test steps. The Trunk CLI automatically detects Google Cloud Build when the `TRIGGER_NAME` environment variable is set.

{% hint style="warning" %}
Google Cloud Build does not automatically provide environment variables to build steps. You must explicitly pass the required substitution variables in your `cloudbuild.yaml` using the `env` field. Without these variables, the CLI cannot detect your CI platform or link uploads to the correct branches and pull requests.
{% endhint %}

#### Required Environment Variables

The following environment variables must be passed to the upload step:

| Variable | Description |
|----------|-------------|
| `TRIGGER_NAME` | Name of the Cloud Build trigger (used for CI platform detection) |
| `PROJECT_ID` | GCP project ID (used to construct the CI job link) |
| `BUILD_ID` | Cloud Build build ID (used to construct the CI job link) |
| `BRANCH_NAME` | Git branch being built (used for push/stable branch uploads) |
| `_HEAD_BRANCH` | Head branch for PR-triggered builds |
| `_PR_NUMBER` | Pull request number for PR-triggered builds |

#### Example `cloudbuild.yaml`

The following is an example of a `cloudbuild.yaml` configuration that runs tests and uploads results to Trunk. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.&#x20;

{% tabs %}
{% tab title="XML" %}
```yaml
steps:
  - name: gcr.io/cloud-builders/npm
    id: run-tests
    script: |
      #!/bin/bash
      set -euo pipefail
      npm install
      npm test
    timeout: 600s
    allowExitCodes: [0, 1]

  - name: gcr.io/cloud-builders/gcloud
    id: upload-test-results
    script: |
      #!/bin/bash
      set -euo pipefail
      curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
      ./trunk flakytests upload \
        --junit-paths "<XML_GLOB_PATH>" \
        --org-url-slug <TRUNK_ORG_SLUG> \
        --token "${TRUNK_API_TOKEN}"
    waitFor:
      - run-tests
    timeout: 300s
    env:
      - "PROJECT_ID=${PROJECT_ID}"
      - "BUILD_ID=${BUILD_ID}"
      - "TRIGGER_NAME=${TRIGGER_NAME}"
      - "COMMIT_SHA=${COMMIT_SHA}"
      - "REPO_FULL_NAME=${REPO_FULL_NAME}"
      - "BRANCH_NAME=${BRANCH_NAME}"
      - "_HEAD_BRANCH=${_HEAD_BRANCH}"
      - "_PR_NUMBER=${_PR_NUMBER}"
    secretEnv: ["TRUNK_API_TOKEN"]

options:
  logging: CLOUD_LOGGING_ONLY
timeout: 1200s
availableSecrets:
  secretManager:
    - versionName: projects/${PROJECT_ID}/secrets/<YOUR_SECRET_NAME>/versions/latest
      env: TRUNK_API_TOKEN
```
{% endtab %}

{% tab title="Bazel" %}
```yaml
steps:
  - name: gcr.io/cloud-builders/bazel
    id: run-tests
    args: ['test', '//...', '--build_event_json_file=bep.json']
    timeout: 600s
    allowExitCodes: [0, 1]

  - name: gcr.io/cloud-builders/gcloud
    id: upload-test-results
    script: |
      #!/bin/bash
      set -euo pipefail
      curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x ./trunk
      ./trunk flakytests upload \
        --bazel-bep-path bep.json \
        --org-url-slug <TRUNK_ORG_SLUG> \
        --token "${TRUNK_API_TOKEN}"
    waitFor:
      - run-tests
    timeout: 300s
    env:
      - "PROJECT_ID=${PROJECT_ID}"
      - "BUILD_ID=${BUILD_ID}"
      - "TRIGGER_NAME=${TRIGGER_NAME}"
      - "COMMIT_SHA=${COMMIT_SHA}"
      - "REPO_FULL_NAME=${REPO_FULL_NAME}"
      - "BRANCH_NAME=${BRANCH_NAME}"
      - "_HEAD_BRANCH=${_HEAD_BRANCH}"
      - "_PR_NUMBER=${_PR_NUMBER}"
    secretEnv: ["TRUNK_API_TOKEN"]

options:
  logging: CLOUD_LOGGING_ONLY
timeout: 1200s
availableSecrets:
  secretManager:
    - versionName: projects/${PROJECT_ID}/secrets/<YOUR_SECRET_NAME>/versions/latest
      env: TRUNK_API_TOKEN
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Important:** Set `allowExitCodes: [0, 1]` on your test step so the upload step runs even when tests fail. Without this, Cloud Build stops the pipeline on test failures and your results won't be uploaded.
{% endhint %}

Replace the following placeholders in the example:

| Placeholder | Description |
|-------------|-------------|
| `<XML_GLOB_PATH>` | Glob pattern matching your JUnit XML test report files (for example, `**/junit.xml`) |
| `<TRUNK_ORG_SLUG>` | Your Trunk organization slug |
| `<YOUR_SECRET_NAME>` | The name of the secret you created in GCP Secret Manager |

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

{% hint style="success" %}
**Have questions?**

Join us and 1500+ fellow engineers [on Slack](https://slack.trunk.io/) to get help with Trunk.
{% endhint %}
