---
description: Continuous Integration Setup
---

# CI Setup

Trunk Code Quality has the ability to post its results to the [Trunk Code Quality web app](https://app.trunk.io/login?intent=check). This will enable you to view your repository's Check history over time so you can track the trend of issues in your code, as well as browse the issues in your repository to help you understand which issues should be prioritized to fix.&#x20;

The upload feature of Trunk Code Quality will upload all of the issues found by Trunk to the Trunk services. In order to get an accurate picture of the state of your repository, you'll want to upload all of the Trunk Code Quality issues for your whole repository. Generally this should be done within your Continuous Integration system (CI) automatically whenever **pull requests are filed or pushed to a specific branch** in your repo. Trunk Code Quality can also **run periodically** (ex: every night) to check for new vulnerabilities in your dependencies.&#x20;

To run Trunk Code Quality automatically you must setup the [Trunk Code Quality web app](https://app.trunk.io/login?intent=check) to connect to your CI system.

If you are using GitHub see the [GitHub Integration Guide](get-started/).&#x20;

If you are using GitLab or another CI system, see the [GitLab and other CI Integration Guide](continuous-integration/).
