---
description: Configure Flaky Tests using Jenkins
---

# Jenkins

Trunk Flaky Tests integrates with your CI by adding a step in your Jenkins Pipelines to upload tests with the [Trunk Analytics CLI](../../uploader.md).

{% include "../../../.gitbook/includes/not-using-github-for-source....md" %}

Before you start on these steps, see the [Test Frameworks](../frameworks/) docs for instructions on producing a Trunk-compatible output for your test framework.

{% include "../../../.gitbook/includes/ci-provider-checklist.md" %}

{% include "../../../.gitbook/includes/trunk-organization-slug-and....md" %}

### Add the Trunk Token as a Secret

Store the Trunk slug and API token obtained in the previous step in your Jenkins as new credentials named `TRUNK_ORG_SLUG` and `TRUNK_TOKEN` respectively.

### Upload to Trunk

Add an `Upload Test Results` step after running tests in each of your CI jobs that run tests. This should be minimally all jobs that run on pull requests, as well as from jobs that run on your main or [stable branches](../../detection/), for example, `main`, `master`, or `develop`.

{% include "../../../.gitbook/includes/stable-branches-hint.md" %}

#### Example Jenkins Pipeline

The following is an example of a Jenkins pipeline step to upload test results after your tests run. Note: you must either run `trunk` from the repo root when uploading test results or pass a `--repo-root` argument.

To find out how to produce the report files the uploader needs, see the instructions for your test framework in the [Test Frameworks](../frameworks/) docs

{% tabs %}
{% tab title="XML" %}
```groovy
pipeline {
  environment {
    TRUNK_TOKEN = credentials('TRUNK_TOKEN')
  }
  stages {
    stage('Run Tests'){
      ...
    }
    stage('Upload Test Results'){
      sh 'curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz && chmod +x trunk-analytics-cli'
      sh './trunk-analytics-cli upload --junit-paths "<XML_GLOB_PATH>" --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN'
    }
  }
}
```
{% endtab %}

{% tab title="Bazel" %}
```yaml
pipeline {
  environment {
    TRUNK_TOKEN = credentials('TRUNK_TOKEN')
  }
  stages {
    stage('Run Tests'){
      ...
    }
    stage('Upload Test Results'){
      sh 'curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz && chmod +x trunk-analytics-cli'
      sh './trunk-analytics-cli upload --bazel-bep-path <BEP_JSON_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN'
    }
  }
}
```
{% endtab %}

{% tab title="XCode" %}
```yaml
pipeline {
  environment {
    TRUNK_TOKEN = credentials('TRUNK_TOKEN')
  }
  stages {
    stage('Run Tests'){
      ...
    }
    stage('Upload Test Results'){
      sh 'curl -fL --retry 3 "https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux.tar.gz" | tar -xz && chmod +x trunk-analytics-cli'
      sh './trunk-analytics-cli upload --xcresult-path <XCRESULT_PATH> --org-url-slug <TRUNK_ORG_SLUG> --token $TRUNK_TOKEN'
    }
  }
}
```
{% endtab %}

{% tab title="RSpec plugin" %}
```groovy
pipeline {
  environment {
    TRUNK_ORG_SLUG = credentials('TRUNK_ORG_SLUG')
    TRUNK_TOKEN = credentials('TRUNK_TOKEN')
  }
  stages {
    stage('Run Tests and Upload Results to Trunk.io'){
      sh 'TRUNK_ORG_URL_SLUG=$TRUNK_ORG_SLUG TRUNK_API_TOKEN=$TRUNK_TOKEN bundle exec rspec'
    }
  }
}
```
{% endtab %}
{% endtabs %}

{% include "../../../.gitbook/includes/platform-hint.md" %}

{% include "../../../.gitbook/includes/stale-files-warning.md" %}

{% include "../../../.gitbook/includes/have-questions-join-us-and-....md" %}
