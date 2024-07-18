---
description: >-
  Flaky Tests provides summary analytics about tests running on Pull
  Requests.
---

# GitHub Pull Request Comments

## Overview

Flaky Tests can post comments on GitHub pull requests to provide a summary of your tests’ health and prompt you to further inquire from the Flaky Tests dashboard.

<figure><img src="../.gitbook/assets/test-analtyics-pr-comment-screenshot.png" alt=""><figcaption><p>Screenshot of Flaky Tests test report</p></figcaption></figure>

## Getting Started

If you have the [Trunk GitHub App installed](https://docs.trunk.io/administration/github-app-permissions) and are [uploading JUnit XML](frameworks/) test results on pull requests, expect to start seeing comments on your Pull Requests soon. If you prefer not to use the Trunk GitHub App you can still set up comments on your Pull Requests by providing Trunk with a GitHub access token.

### Set Up (without Trunk GitHub App install)

1. _\[Recommended]_ Create a dedicated CI user with access to the repositories in your GitHub Organization that Flaky Tests will comment on e.g., `trunk-analytics-user`.
2. On [github.com](https://github.com/), for `trunk-analytics-user` (or whichever user you wish you to use), generate a _"Personal access token"_ by navigating to **Settings** > **Developer settings** > **Personal access token** > **Fine-grained tokens** > **Generate new token**.
3. Name the new token something memorable. ex: `trunk-flaky-tests-token`.
4. The expiry time is up to you - however long you wish to try out Flaky Tests comments/how often you are willing to update the token. For a longer term solution, consider installing the Trunk GitHub App.
5. The resource owner should be the GitHub Organization or user that owns the appropriate repositories. ([see note about GitHub Org Ownership settings](github-pull-request-comments.md#github-org-ownership))
6. Select the repositories you wish to enable comments on.
7. _\[Important]_ **Permissions** - you must enable **Issues (Read and write)** and **Pull requests (Read and write)**. Note: It is expected that metadata permissions automatically change.
8. If everything looks good, scroll down to double check that your Overview for permissions looks something like the image below. If so, create the token.![](<../.gitbook/assets/Screenshot 2024-06-12 at 9.52.28 AM.png>)
9. Once the token is generated, go back to the Trunk App ([app.trunk.io](https://app.trunk.io/)) > click on your profile > **Settings** > **Manage** (under _Organization_) > scroll down to **Organization GitHub Token** and enter the copied token into the text field, then finally press Submit.

Expect to see comments on your Pull Requests in a couple of minutes!

## GitHub Org Ownership

If you wish to set the resource owner to be a GitHub Organization, you should double check that this is allowed by navigating to your **GitHub Organization** > **Settings** > **Personal access tokens** > **Settings**. Make sure under "_Fine-grained personal access tokens_", you have _"Allow access via fine-grained personal access tokens"_ selected.

Once the token is created, the Organization admin may need to approve the request for the token. This can be done by going to **Github Organization** > **Settings** > **Personal access tokens** > **Pending requests**. To confirm that the token was set, you should be able to see it under _"Active tokens"_.

![](https://lh7-us.googleusercontent.com/docsz/AD\_4nXdZoEScO82K-8SGNGRLczrcgDjl2orvJhAE1m3SmMYEXB8nA0mL23DGiWli-LOoXiNRix3cFF6OxhEm8m\_kzDe4AwLLrA\_Uqql-X6iRejCQycpxPzhuuYYJasDjbuJVDDI7kJ6bkcCdhziyCLLbh2uCBdI?key=oLba3DU2CoziRj7rJD\_TyA)

## Disable commenting

Pull Request comments are enabled by default. If you wish to disable the comments, you can do so by navigating to the Trunk App > click on your profile > **Settings** > **RepoName**. Scroll down to Test **Analytics** then toggle the **Summary Flaky Tests Reports** setting.&#x20;

## Troubleshooting

At any point, feel free to reach out to our team through slack at https://slack.trunk.io.\
