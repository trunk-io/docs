---
description: Flaky Tests provides summary analytics about tests running on Pull Requests
---

# Pull request comments

Flaky Tests can post comments on GitHub pull requests that summarize test results across CI jobs. These comments indicate which failures are flaky and include the test’s failure history and related context.

**Note:** Flaky Tests will only post a comment when there are failing tests.

<figure><picture><source srcset="../.gitbook/assets/github-comment-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/github-comment-light.png" alt=""></picture><figcaption></figcaption></figure>

Each GitHub comment includes a summary report showing all tests that passed, failed, flaked, were skipped, or were quarantined on the PR.

<figure><picture><source srcset="../.gitbook/assets/pr-test-summary (1).png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/pr-test-summary.png" alt=""></picture><figcaption></figcaption></figure>

Each test case includes the full stack trace when expanded, and the job run link takes you to the complete CI logs.

## Configuration

If you have the [Trunk GitHub App installed](https://docs.trunk.io/administration/github-app-permissions) and are [uploading JUnit XML](get-started/frameworks/) test results on pull requests, expect to start seeing comments on your Pull Requests soon. If you prefer not to use the Trunk GitHub App, you can still set up comments on your Pull Requests by providing Trunk with a GitHub access token.



<details>

<summary>Without Trunk GitHub App</summary>

It's recommended that the Trunk GitHub App be used to manage GitHub comments. If you need to generate comments without the Trunk GitHub app, you can do so with a service account and an API token.

1. Create a dedicated GitHub SVC account (Service Account) with access to the repositories in your GitHub Organization that Flaky Tests will comment on e.g., `trunk-analytics-user`.
2. On [github.com](https://github.com/), for `trunk-analytics-user` (or whichever user you wish to use), generate a [_Personal access token_](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) by navigating to **Settings** > **Developer settings** > **Personal access token** > **Fine-grained tokens** > **Generate new token**.
3. Name the new token something memorable. ex: `trunk-flaky-tests-token`.
4. The expiry time is up to you - however long you wish to try out Flaky Tests comments/how often you are willing to rotate the token. For a longer-term solution, consider installing the Trunk GitHub App.
5. The resource owner should be the GitHub Organization or user that owns the appropriate repositories. [See note on GitHub Org Ownership settings.](github-pull-request-comments.md#github-org-ownership)
6. Select the repositories you wish to enable comments on.
7. **Permissions** - you must enable **Issues (Read and write)** and **Pull requests (Read and write)**. Note: It is expected that metadata permissions automatically change.
8.  If everything looks good, scroll down to double check that your Overview for permissions looks something like the image below. If so, create the token.

    <figure><img src="../.gitbook/assets/Screenshot 2024-06-12 at 9.52.28 AM.png" alt=""><figcaption></figcaption></figure>
9. Once the token is generated, go back to the Trunk App ([app.trunk.io](https://app.trunk.io/login?intent=flaky%20tests)) > click on your profile > **Settings** > **Manage** (under _Organization_) > **Organization GitHub Token** and enter the copied token into the text field, then finally press **Submit**.

You should see comments posted by your service account on your next PR.

</details>

## Disable commenting

Pull Request comments are enabled by default. If you wish to disable the comments, you can do so by navigating to the Trunk App > click on your profile > **Settings** > **RepoName**. In the **Flaky Tests** heading, toggle the **Summary Flaky Tests Reports** setting.

## Troubleshooting

#### **GitHub Organization ownership**

If you wish to set the resource owner to be a GitHub Organization, you should double check that this is allowed by navigating to your **GitHub Organization** > **Settings** > **Personal access tokens** > **Settings**. Make sure under "_Fine-grained personal access tokens_", you have _"Allow access via fine-grained personal access tokens"_ selected.

Once the token is created, the Organization admin may need to approve the request for the token. This can be done by going to **Github Organization** > **Settings** > **Personal access tokens** > **Pending requests**. To confirm that the token was set, you should be able to see it under **Active tokens**.

At any point, feel free to reach out to our team [through Slack](https://slack.trunk.io).
