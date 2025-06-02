# Licensing

### Introduction

Trunk Code Quality is a powerful metalinter that simplifies linting, formatting, and static analysis across your entire codebase. By integrating over 100 supported tools like ESLint, Prettier, Ruff, and more, it enables you to manage code quality with unified configuration and consistent reporting. Trunk Code Quality helps you install tools hermetically, run them efficiently, and integrate seamlessly with pull requests and CI pipelines.

### Licensing Overview

Trunk Code Quality is composed of a closed-source core complemented by open-source components that enhance extensibility and integration. Understanding the licensing terms for each part ensures compliance and optimal use.

#### Closed-Source Components

* Trunk CLI: The core command-line tool is closed-source but free to use under specific conditions.
* VS Code Extension: Integrates Trunk Code Quality directly into your development environment. Under the hood, all code-checking by the VS Code extension is completed via the Trunk CLI, which drives the VS Code extension.

#### Open-Source Components

* Plugin System and Configurations: An extensible plugin system that allows you to define, extend, and share linter configurations. These plugins are open-source under the MIT License, enabling you to modify them or create new ones to integrate additional tools or customize behavior.
* GitHub Action:  Scripts that automate Trunk Code Quality checks in your GitHub workflows. GitHub Actions require the source code to be visible for transparency and security. Our GitHub Action is open-source under the MIT License, allowing you to review, modify, and ensure it meets your needs.

By open-sourcing these components, we promote transparency, extensibility, and community collaboration. This approach encourages our community and customers to contribute to the ecosystem, enhancing Trunk Code Quality for everyone.

#### Free Usage

You can use the Trunk CLI and access core functionalities for free under the following conditions:

* Open-Source and Public Projects: Unlimited use in public repositories.
* Private Repositories
  * Free for teams with up to 5 active non-bot committers.
  * An active committer is a non-bot user who has committed in the last 30 days.

#### Paid Licensing

For private repositories with over 5 active committers, a paid license is required to comply with Trunk Code Quality’s licensing agreement. While all features remain accessible, payment is necessary to meet licensing obligations and support the continued development of the product.

Compliance and Support

* Licensing Compliance: Payment ensures your use of Trunk Code Quality aligns with the licensing terms for larger teams.
* Dedicated Support: Paid customers receive prioritized support to help with integration, troubleshooting, and maximizing the benefits of Trunk Code Quality.

#### How Billing Works

Trunk Code Quality offers two billing options for paid licenses:

**1. Team Plan - Monthly Self-Serve Billing**

* Per-Seat Model: Billing is based on the monthly active committers in your private repositories.
* User Count Calculation:
  * Counts non-bot users who have made commits in the last 30 days.
  * Calculated at the end of each billing period to adjust the next invoice.
* Integration with GitHub App: Install the Trunk GitHub App to allow us to measure active monthly users.
* Billing Cycle: Month-to-month billing with invoices reflecting the latest user count.

**2. Enterprise Plan - Annual Site License**

* Fixed User Count: Based on the number of active committers at the beginning of the licensing term.
* Organization-Wide License: Provides a license for all users in the organization during the entire term without the need to purchase additional licenses for new employees.
* Simplified Billing: One annual payment covers all users for the year.
* Discount: Incentives available with annual plans for logo usage, case study, and/or scale.&#x20;

**Choosing the Right Option**

* Team Plan: Appropriate for small teams that prefer flexibility and want to pay monthly with a credit card.
* Enterprise Plan: Best for organizations that prefer predictable costs, to avoid the administrative overhead of tracking monthly user counts, and wish to benefit from the discounted rate.

### FAQs

**What are the benefits of paying for Trunk Code Quality?**

Paying for Trunk Code Quality offers several important benefits:

* Licensing Compliance: For private repositories with 5 or more active committers, purchasing a license is required to comply with Trunk Code Quality’s licensing terms and continue using the product legally and effectively.
* Dedicated Support: Receive prioritized assistance to help integrate, troubleshoot, and maximize the product’s benefits in your production environment.
* Priority Feature Requests: Your requests for new features and plugin integrations receive high priority, allowing you to influence the product’s development to suit your needs better.
* Expert Consultation: Access advisory services from our team to optimize your code quality setup and linting processes.
* Onboarding Assistance: Receive support and best practices guidance during the integration of Trunk Code Quality into your workflows.

Importantly, all features are available regardless of licensing status; you do not unlock additional features by purchasing a license. However, buying a license ensures compliance with the licensing terms, supports the continued development of Trunk Code Quality, and provides access to the dedicated support and benefits listed above.

**Do you provide free Proofs of Concept (POCs)?**

Yes, we are happy to provide 2–4 week free POCs for teams that want to evaluate our product's capabilities with their team and as part of their CI. We also provide dedicated support and guidance throughout the POC period. Email us to get started at: [sales@trunk.io](mailto:sales@trunk.io).

**What happens if I exceed the free usage limits?**

If you exceed the free tier limits (e.g., more than 5 active committers in a private repository), you must obtain a paid license to continue using Trunk Code Quality in compliance with the licensing agreement.

**Is the Trunk CLI free to use?**

The Trunk CLI is free for public repositories and private repositories with fewer than 5 active committers. For private repositories with 5 or more active committers, a paid license is required to comply with the licensing agreement.

**Can I use Trunk Code Quality in CI/CD pipelines for free?**

Yes, you can integrate the Trunk CLI into your CI/CD pipelines for free if you’re within the free usage limits (public repositories or private repositories with fewer than 5 active committers). Exceeding these limits requires a paid license.

**Is support provided for free users?**

Yes, free users can seek help through our community Slack channel at [slack.trunk.io](https://slack.trunk.io) or participate in discussions on our [GitHub page](https://github.com/orgs/trunk-io/discussions). Our community members and developer relations engineers regularly participate in discussions and answer questions.

**Why are some components open-source while the core is closed-source?**

* Core Functionality: The Trunk CLI provides the core functionality and is closed-source to protect proprietary technology and ensure a consistent, reliable experience.
* Open-Source Components: The plugin system and GitHub Action are open-source to promote transparency, security, and community-driven extensibility. This allows you to customize integrations and contribute to the development of plugins and workflows.

**Do I need the Trunk CLI to use the open-source components?**

Yes, the open-source components are designed to work with the Trunk CLI. They enhance and extend the functionality provided by the core tool but are not standalone applications.

**How to Contribute to the Open-Source Components?**

* Plugin Development: You can develop new plugins or improve existing ones by visiting our public GitHub repository at [github.com/trunk-io/plugins](https://github.com/trunk-io/plugins).
* GitHub Action: Modify or fork our GitHub Action to better suit your CI workflows. The source code is available at [github.com/trunk-io/trunk-action](https://github.com/trunk-io/trunk-action).
* Community Engagement: Join our community Slack channel at [slack.trunk.io](https://slack.trunk.io) to collaborate with other users and our development team.

#### Contact Us

For licensing inquiries, to obtain a paid license, or to discuss which billing option is best for your organization, please contact [sales@trunk.io](mailto:sales@trunk.io). We’re here to help you ensure compliance and get the most out of Trunk Code Quality.
