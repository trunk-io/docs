---
description: >-
  Impacted targets are metadata about a PR describing which parts of the
  codebase changed.
---

# Impacted Targets

## What are Impacted Targets?

Impacted targets are metadata about a pull request that defines the logical changes made by a pull request. They're a list of strings: for example, PR 123 which changes to the user service may have the following list of impacted targets: `[backend, user-service, integration-tests]`. Anytime two PRs have an overlap in the list of impacted target strings, Trunk Merge will ensure those PRs pass tests when based off of one another.

## Generating Impacted Targets

The repo using the Merge Queue is required to generate impacted targets for every pull request. Some build systems (e.g. [Bazel](merge-+-bazel.md), Buck, Gradle, Turborepo, ...) define targets, which can be uploaded to the Merge Queue. Alternatively, a glob-based pattern approach could be used, where filepaths map to a target (e.g. files in `src/backend` upload the `backend` target.)

We offer out of the box CI solutions for uploading impacted targets based on the flavor of your repo (see below). If none of the solutions work, please let us know at our [Slack](https://slack.trunk.io); we are happy to help build out something for your use case. Alternatively, we are accepting contributions to our [open-sourced repository](https://github.com/trunk-io/merge-action).

### Custom Impacted Targets

Impacted Targets should be computed for every PR. The list of impacted targets should be computed by comparing two different SHAs: the **head of the target branch**, and the **merge commit of the pr**.

<figure><img src="../../.gitbook/assets/02 Branch-1 kopiera.png" alt=""><figcaption><p>From <a href="https://www.atlassian.com/git/tutorials/using-branches/git-merge">https://www.atlassian.com/git/tutorials/using-branches/git-merge</a>. In this diagram, we want to compare the merge commit and the main tip.</p></figcaption></figure>

{% hint style="info" %}
Our [reference implementation](https://github.com/trunk-io/merge-action/blob/main/src/scripts/compute\_impacted\_targets.sh) may be useful in guiding your implementation.
{% endhint %}

After they are computed, upload them to our services. Our HTTP POST endpoint can be found at `https://api.trunk.io:443/v1/setImpactedTargets`. We expect the following headers/body:

```ssml
HEADERS:
	Content-Type: application/json,
	x-api-token: <organization API token>, <!-- only for non forked PRs -->
	x-forked-workflow-run-id: ${{github.run_id}}, <!-- only for forked PRs -->

BODY: {
	repo: {
		host: "github.com",
		owner: <repo owner>, <!--- For example, "trunk-io" --->
		name: <repo name>, <!--- For example, "merge-action" --->
	},
	pr: {
		number: <pr number>, <!-- For example, 5 -->
		sha: <pr sha>, <!-- For example, "07fc773f16c0353bc3820fed65d89afddb9f81c3" -->
	},
	targetBranch: <merge instance branch>, <!-- For example, "main" -->
	impactedTargets: ["target-1", "target-2", ...] OR "ALL" <!--- see notes on "ALL" below --->
      }
```

`impactedTargets` allows specifying either an array of strings representing the impacted targets from the PR or the string "ALL" (note that this is explicitly not in an array and is just the string "ALL"). Specifying "ALL" is the equivalent of saying that everything that comes into the graph after this PR should be based off of this one, which is useful when your PR contains changes that affect the whole repo (such as editing `trunk.yaml` or a GitHub workflow).

### Impacted Targets for Forked PRs

The HTTP POST must contain the `x-api-token` to prove that it is a valid request from a workflow your org controls. _Workflows which come from forked PRs most likely will not have access to the Trunk org token_ required for the HTTP POST above. In this case you should provide the **run ID** of the workflow as the  `x-forked-workflow-run-id` header in place of the `x-api-token`. This ID can be  obtained from [the GitHub context](https://docs.github.com/en/actions/learn-github-actions/contexts#github-context) as `${{ github.run_id }}`. Trunk Merge will verify that the ID belongs to a currently running workflow originating from a forked PR with a SHA that matches the one provided in the request and allow it through.

{% hint style="info" %}
We do not recommend using an event trigger like `pull_request_target.` This would allow workflows from forked PRs to get secrets, which is a security risk and would open your repo to attackers making forks, adding malicious code, and then running it against your repo to exfiltrate information. (see[ Keeping your GitHub Actions and workflows secure](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/)).
{% endhint %}

### Impacted Targets Generation: Bazel + GitHub Actions

For Bazel specific instructions, see [the Bazel guide](merge-+-bazel.md).&#x20;
