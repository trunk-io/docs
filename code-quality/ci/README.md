---
description: Continuous Integration Setup
---

# CI Setup

Trunk Check has the ability to post its results to the [Trunk Check web app](https://app.trunk.io/login?intent=check). This will enable you to view your repository's Check history over time so you can track the trend of issues in your code, as well as browse the issues in your repository to help you understand which issues should be prioritized to fix.

The upload feature of Trunk Check will upload all of the issues found by Trunk to the Trunk services. In order to get an accurate picture of the state of your repository, you'll want to upload all of the Trunk Check issues for your whole repository. Generally this should be done within your Continuous Integration system (CI) automatically whenever **pull requests are filed or pushed to a specific branch** in your repo. Trunk Check can also **run periodically** (ex: every night) to check for new vulnerabilities in your dependencies.

To run Trunk Check automatically you must setup the [Trunk Check web app](https://app.trunk.io/login?intent=check) to connect to your CI system.

If you are using GitHub see the [GitHub Integration Guide](get-started/).

If you are using GitLab or another CI system, see the [GitLab and other CI Integration Guide](general/).
