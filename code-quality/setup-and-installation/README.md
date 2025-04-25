# Setup & Installation

{% hint style="danger" %}
**Deprecation Warning**\
The Trunk Code Quality web app, Code Quality on PRs, and Code Quality Nightly will soon be deprecated. Follow the instructions on the [Linting in CI](prevent-new-issues/) page to migrate off these features.
{% endhint %}

Trunk Code Quality is easy to adopt for new and legacy projects alike. You can run Trunk Code Quality using your existing linter configurations, incrementally address existing problems, and prevent new issues from being committed to your repo.

You can start using Code Quality in your repos in 4 steps.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Step 1: Initialize Trunk</strong></td><td>Initialize Trunk in your repo to generate Trunk config files and get linter recommendations based on your project's files.</td><td></td><td><a href="initialize-trunk.md">initialize-trunk.md</a></td></tr><tr><td><strong>Step 2: Check for issues</strong></td><td>Check for existing issues in your project. You can address problems up front, use <strong>hold-the-line</strong> to fix them incrementally, and configure ignores for irrelevant issues.     </td><td></td><td><a href="deal-with-existing-issues.md">deal-with-existing-issues.md</a></td></tr><tr><td><strong>Step 3: Prevent New Issues</strong></td><td>Set up automated runs on commits, before pushes, and on PRs to prevent new issues from appearing in your repo.</td><td></td><td><a href="prevent-new-issues/">prevent-new-issues</a></td></tr><tr><td><strong>Step 4: Nightly Reports</strong></td><td>Code Standards evolve, and new vulnerabilities are discovered daily. Run regular Code Quality checks to discover issues in your repo.</td><td></td><td><a href="../ci-setup/github-integration.md">github-integration.md</a></td></tr></tbody></table>
