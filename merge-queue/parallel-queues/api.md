---
description: Upload custom list of impacted targets
---

# API

Impacted Targets should be computed for every PR. The list of impacted targets should be computed by comparing two different SHAs: the **head of the target branch**, and the **merge commit of the pr**.&#x20;

{% hint style="info" %}
Our [reference implementation](https://github.com/trunk-io/bazel-action/tree/main/src/scripts) may be useful in guiding your implementation.
{% endhint %}

**POST** the list of impacted targets here:`https://api.trunk.io:443/v1/setImpactedTargets`.&#x20;

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

`impactedTargets` allows specifying either an array of strings representing the impacted targets from the PR or the string "ALL" (note that this is explicitly not in an array and is just the string "ALL"). Specifying "ALL" is the equivalent of saying that everything that comes into the graph after this PR should be based on this one, which is useful when your PR contains changes that affect the whole repo (such as editing `trunk.yaml` or a GitHub workflow).

**Handling Forked Pull Requests**\
The HTTP POST must contain the `x-api-token` to prove that it is a valid request from a workflow your org controls. _Workflows which come from forked PRs most likely will not have access to the Trunk org token_ required for the HTTP POST above. In this case you should provide the **run ID** of the workflow as the  `x-forked-workflow-run-id` header in place of the `x-api-token`. This ID can be  obtained from [the GitHub context](https://docs.github.com/en/actions/learn-github-actions/contexts#github-context) as `${{ github.run_id }}`. Trunk Merge will verify that the ID belongs to a currently running workflow originating from a forked PR with a SHA that matches the one provided in the request and allow it through.

{% hint style="info" %}
We do not recommend using an event trigger like `pull_request_target.` This would allow workflows from forked PRs to get secrets, which is a security risk and would open your repo to attackers making forks, adding malicious code, and then running it against your repo to exfiltrate information. (see[ Keeping your GitHub Actions and workflows secure](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/)).
{% endhint %}
