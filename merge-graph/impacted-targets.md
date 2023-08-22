# Impacted Targets

## What are Impacted Targets?&#x20;

Impacted targets are metadata about a pull request that defines the logical changes made by a pull request. They're a list of strings: for example, PR 123 writing changes to the user service may generate the following list of impacted targets: `[backend, user-service, integration-tests]`. Anytime two PRs have an overlap in the list of impacted target strings, Trunk Merge will ensure those PRs pass tests when based off of one another.

## Generating Impacted Targets

The repo using the Merge Graph is required to generate impacted targets for every pull request. Some build systems (e.g. Bazel, Buck, Gradle, Turborepo, ...) define targets, which can be uploaded to the MergeGraph. Alternatively, a glob-based pattern approach could be used, where filepaths map to a target (e.g. files in `src/backend` upload the `backend` target.)

We offer out of the box CI solutions for uploading impacted targets based on the flavor of your repo (see below). If none of the solutions work, please let us know at our [Slack](https://slack.trunk.io); we are happy to help build out something for your use case. Alternatively, we are accepting contributions to our [open-sourced repository](https://github.com/trunk-io/merge-action).

### Custom Impacted Targets

Impacted Targets should be computed for every PR. The list of impacted targets should be computed by comparing two different shas: the **head of the target branch**, and the **merge commit of the pr**.

<figure><img src="../.gitbook/assets/02 Branch-1 kopiera.png" alt=""><figcaption><p>From <a href="https://www.atlassian.com/git/tutorials/using-branches/git-merge">https://www.atlassian.com/git/tutorials/using-branches/git-merge</a>. In this diagram, we want to compare the merge commit and the main tip.</p></figcaption></figure>

{% hint style="info" %}
Our [reference implementation](https://github.com/trunk-io/merge-action/blob/main/src/scripts/compute\_impacted\_targets.sh) may be useful in guiding your implementation.
{% endhint %}

After they are computed, upload them to our services. Our HTTP POST endpoint can be found at `https://api.trunk.io:443/v1/setImpactedTargets`. We expect the following headers/body:

```ssml
HEADERS:
	Content-Type: application/json,
	x-api-token: <repo API token>

BODY: {
	repo: {
		host: "github.com",
		owner: "trunk-io",
		name: "merge-action",
	},
	pr: {
		number: <pr number>,
		sha: <pr sha>,
	},
	targetBranch: <merge instance branch, e.g.. main>,
	impactedTargets: ["a", "b", "c"]
      }
```

### Impacted Targets Generation: Bazel + GitHub Actions

1. Grab your repository's API token from [app.trunk.io](../merge/graph/app.trunk.io), in the settings > repo-name page.
2. Store the repository's API token as a GitHub action secret.
3. Use the `trunk-io/merge-action` action, as defined [here](https://github.com/trunk-io/merge-action#usage).
