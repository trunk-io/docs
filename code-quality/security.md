---
description: The properties of code access and security of using Trunk Code Quality
---

# Security

At Trunk, we prioritize the security and privacy of your source code. Our primary commitment is that we do not clone or store your entire codebase. Here's a detailed breakdown of how we handle your code:

### CLI

Whether invoked directly by developers on their local machines, triggered automatically by git hooks during commits or pushes, or run in CI, it's the same tool operating in different contexts. In all these scenarios:

* Your code is processed entirely locally; by default, we never transmit, store, or share your source code on our servers.
* All linting, formatting, and analysis occur within your own environment, ensuring your code never leaves your control.
* Limited usage telemetry data is collected. This data never includes your source code, and it is possible to opt-out. For more details on telemetry, please refer to our[ telemetry documentation](https://docs.trunk.io/cli/configuration/telemetry).
* See below for the properties of setting up uploads to the Trunk web application.

### VS Code Extension

The Trunk VS Code extension has the same privacy properties as the Trunk CLI. Under the hood, all code-checking by the VS Code extension is completed via the Trunk CLI, which drives the VS Code extension.

### Web App ([app.trunk.io](https://app.trunk.io/?intent=code+quality))

The Trunk Code Quality web app is powered via running nightly scans in your repo’s own CI system which uploads results to the Trunk backend. This feature is optional, but it enables you to audit the issues in your repo and prioritize fixes. Here's how it works:

* Whole-repo scans are performed nightly in your CI environment
* Results are uploaded to Trunk’s backend, using an API token specific to your organization
* Five-line code snippets around each issue Trunk Code Quality detects are uploaded along with the actual issues for better viewing in the Trunk Code Quality web app
* This process ensures that only necessary, limited data is shared, without transmitting or storing your full source code
* You have full control over when and how often these scans and uploads occur

For more information on setting up and configuring result uploads, including how to obtain and use the Trunk access token, please refer to our [upload documentation](https://docs.trunk.io/code-quality/setup-and-installation/github-integration).

\
