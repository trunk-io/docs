---
description: Configure Flaky Tests using Google Cloud Build
---

# Google Cloud Build

Trunk Flaky Tests integrates with your CI by adding a step in your Google Cloud Build configuration to upload tests with the [Trunk Uploader CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

### Checklist

By the end of this guide, you should achieve the following.

* [ ] Get your Trunk organization slug and token
* [ ] Store your Trunk token in GCP Secret Manager
* [ ] Connect your GitHub repos to Cloud Build
* [ ] Create Cloud Build triggers for PR and push events
* [ ] Configure your `cloudbuild.yaml` to upload test results to Trunk
* [ ] Validate your uploads in Trunk

After completing these checklist items, you'll be integrated with Trunk.

### Trunk Organization Slug and Token

Before setting up uploads to Trunk, you must sign in to [app.trunk.io](https://app.trunk.io/login?intent=flaky%20tests) and obtain your Trunk organization slug and token.

#### Trunk Slug

You can find your organization slug under **Settings > Organization > Manage > Organization Name > Slug**. You'll save this as a variable in CI in a later step.

#### Trunk Token

You can find your token under **Settings > Organization > Manage > Organization API Token > View Organization API Token > View**. Since this is a secret, do not leak it publicly. Ensure you get your _organization token_, not your project/repo token.

### Store Your Trunk Token in GCP Secret Manager

Store your Trunk API token in [GCP Secret Manager](https://cloud.google.com/security/products/secret-manager) so Cloud Build can securely access it during builds.

1. Go to **GCP Console > Secret Manager**.
2. Click **Create Secret**.
3. Name the secret (for example, `trunk-org-token`) and paste your Trunk organization API token as the value.
4. Click **Create Secret**.

You will reference this secret in your `cloudbuild.yaml` using the `availableSecrets` field.

### Connect Your GitHub Repos to Cloud Build

Ensure your GitHub repositories are connected to Google Cloud Build via the [Cloud Build GitHub App](https://cloud.google.com/build/docs/automating-builds/github/connect-repo-github).

1. Go to **GCP Console > Cloud Build > Repositories**.
2. Connect your GitHub repository if it is not already connected.

### Create Cloud Build Triggers

Create two triggers for each repository you want to track with Trunk Flaky Tests:

1. Go to **GCP Console > Cloud Build > Triggers**.
2. Create a trigger for **pull request** events.
3. Create a trigger for **push** events to your stable branch (for example, `main`, `master`, or `develop`).

Both triggers should point to the `cloudbuild.yaml` file in your repository.

### Upload to Trunk

Add an upload step in your `cloudbuild.yaml` that runs after your test steps. This step downloads the Trunk Analytics CLI and uploads your test results.

{% hint style="danger" %}
It is important to upload test results from CI runs on [**stable branches**](../../detection.md#stable-branches), such as `main`, `master`, or `develop`. This will give you a stronger signal about the health of your code and tests.

Trunk can also detect test flakes on PR and merge branches. To best detect flaky tests, it is recommended to upload test results from stable, PR, and merge branch CI runs.

[Learn more about detection](../../detection.md)
{% endhint %}

#### Example `cloudbuild.yaml`

The following is an example Cloud Build configuration that runs tests and uploads results to Trunk. Note: you must either run the CLI from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [frameworks](../frameworks/ "mention") docs.

```yaml
steps:
  - name: gcr.io/cloud-builders/npm
    id: jest-test
    script: |
      #!/bin/bash
      set -euo pipefail
      npm install -g pnpm
      pnpm install
      pnpm run jest-test
    timeout: 600s
    allowExitCodes: [0, 1] # allow test failures so upload step still runs

  - name: gcr.io/cloud-builders/gcloud
    id: analytics-upload
    script: |
      #!/bin/bash
      set -euo pipefail
      SKU="trunk-analytics-cli-x86_64-unknown-linux.tar.gz"
      curl -fL --retry 3 \
        "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
        | tar -xz
      chmod +x trunk-analytics-cli
      ./trunk-analytics-cli upload \
        --junit-paths "**/junitresults-*.xml" \
        --org-url-slug "<TRUNK_ORG_SLUG>" \
        --token "${TRUNK_API_TOKEN}"
    waitFor:
      - jest-test # add each test step that generates JUnit XML files
    timeout: 300s
    env:
      # Google Cloud Build default substitution variables
      - "PROJECT_ID=${PROJECT_ID}"
      - "BUILD_ID=${BUILD_ID}"
      - "PROJECT_NUMBER=${PROJECT_NUMBER}"
      - "LOCATION=${LOCATION}"
      - "TRIGGER_NAME=${TRIGGER_NAME}"
      - "COMMIT_SHA=${COMMIT_SHA}"
      - "REVISION_ID=${REVISION_ID}"
      - "SHORT_SHA=${SHORT_SHA}"
      - "REPO_NAME=${REPO_NAME}"
      - "REPO_FULL_NAME=${REPO_FULL_NAME}"
      - "BRANCH_NAME=${BRANCH_NAME}"
      - "TAG_NAME=${TAG_NAME}"
      - "REF_NAME=${REF_NAME}"
      # Google Cloud Build GitHub PR substitution variables
      - "_HEAD_BRANCH=${_HEAD_BRANCH}"
      - "_BASE_BRANCH=${_BASE_BRANCH}"
      - "_HEAD_REPO_URL=${_HEAD_REPO_URL}"
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

{% hint style="warning" %}
**Important:** Replace `<TRUNK_ORG_SLUG>` with your Trunk organization slug and `<YOUR_SECRET_NAME>` with the name of the secret you created in GCP Secret Manager.
{% endhint %}

#### Key Configuration Details

**Test step exit codes:** Use `allowExitCodes: [0, 1]` on your test steps so that the upload step runs even when tests fail. Without this, a test failure would stop the build before results are uploaded.

**Step dependencies:** Use `waitFor` on the upload step to list all test steps that produce JUnit XML files. This ensures the upload runs only after all tests complete.

**Environment variables:** Google Cloud Build provides [built-in substitution variables](https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values) that the Trunk CLI uses to associate uploads with the correct commit, branch, and PR. The variables listed in the example above are recommended for full functionality.

**Secret access:** The `availableSecrets` block makes your Trunk API token available as the `TRUNK_API_TOKEN` environment variable in the upload step via `secretEnv`.

See the [uploader.md](../../uploader.md "mention") for all available command line arguments and usage.

#### Stale files

Ensure you report every test run in CI and **clean up stale files** produced by your test framework. If you're reusing test runners and using a glob like `**/junit.xml` to upload tests, stale files not cleaned up will be included in the current test run, throwing off detection of flakiness. You should clean up all your results files after every upload step.

{% hint style="success" %}
**Have questions?**

Join us and 1500+ fellow engineers [on Slack](https://slack.trunk.io/) to get help with Trunk.
{% endhint %}
