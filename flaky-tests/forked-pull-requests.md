---
description: >-
  Upload test results and check quarantined tests on pull requests opened from
  forked repositories, where workflow runs cannot read repository secrets.
---

# Forked Pull Requests

Repositories that accept pull requests from forks — most commonly open-source projects on GitHub — face a CI limitation: **workflow runs triggered from a fork do not have access to the upstream repository's secrets.** In those runs, `secrets.TRUNK_API_TOKEN` is empty, the [Trunk Analytics CLI](uploader.md) cannot authenticate, and the upload fails.

To support these workflows, Trunk provides a **public repo identifier** that you embed directly in your workflow YAML. The Trunk backend uses it to route requests to your repository without an API token. This lets fork PRs upload test results and check the quarantine list, the same as PRs opened from a branch on the upstream repo.

{% hint style="info" %}
The public repo identifier is **not a secret**. It is a per-repo routing value that is safe to commit to a public workflow file. Authorization comes from the per-repo opt-in described below, not from the value itself.
{% endhint %}

### When to use this

Enable the public repo identifier **only for workflows that run on forked pull requests**. Every other run — PRs from branches on the upstream repo, pushes to your default branch, scheduled jobs — should continue to authenticate with `TRUNK_API_TOKEN`, which has full access and higher rate limits.

The identifier authorizes a limited set of operations:

* Uploading test results from the [Trunk Analytics CLI](uploader.md).
* Fetching the quarantine configuration via `/v1/metrics/getQuarantineConfig` so the CLI can apply [Quarantining](quarantining.md) to fork PRs.

It does not authorize Merge Queue endpoints or any other Trunk APIs. Those continue to require an API token.

### Enable the identifier

1. In the Trunk app, go to **Settings → Repositories →** _**your repo**_ **→ Flaky Tests**.
2. In the **Forked PR uploads** card, toggle **Enable forked PR uploads** to **On**.
3. A short identifier is shown on the card — for example `abcd1234`. Copy it.

Toggling the setting **Off** at any time causes Trunk to immediately reject every request that uses the identifier, even though the value itself does not change. Use this if you need to stop accepting fork-PR uploads — for example, while migrating tools.

### Add the identifier to your workflow

In your GitHub Actions workflow, pass `public-repo-id` as a non-secret input alongside (not instead of) your existing `token`:

```yaml
- name: Upload test results
  if: always()
  uses: trunk-io/analytics-uploader@v1
  with:
    org-url-slug: <TRUNK_ORG_SLUG>
    junit-paths: ./target/junit-*.xml
    token: ${{ secrets.TRUNK_API_TOKEN }}
    public-repo-id: abcd1234
```

The action prefers the token when it is available. On runs from a branch in the upstream repo, `secrets.TRUNK_API_TOKEN` is populated and the upload uses it as before. On runs triggered from a fork, the token is empty and the action falls back to `public-repo-id` automatically. No conditional logic is required in your workflow.

To verify the fallback is working, open a pull request from a fork. The upload step should complete successfully, and the run should appear on the **Flaky Tests** dashboard for the upstream repository within a few minutes.

If you call the [Trunk Analytics CLI](uploader.md) directly instead of through the action, pass `--public-repo-id` alongside `--token`. The CLI applies the same fallback rule.

### Authorization model

Each request that arrives with an `X-Trunk-Public-Repo-Id` header is gated by the per-repo toggle:

| Toggle state | Result |
| ------------ | ------ |
| **On**       | The request is accepted and processed the same as a token-authenticated request for that repo. |
| **Off**      | The request is rejected with `401 Unauthorized`. |

Because authorization is gated by the toggle rather than by the secrecy of the value, the identifier is safe to commit to a public workflow file. Anyone reading the YAML can see it; that is expected.

### Troubleshooting

| Symptom | Likely cause |
| ------- | ------------ |
| Every fork-PR upload returns `401`. | The toggle is off, the identifier was copied incorrectly, or neither `token` nor `public-repo-id` is being passed. |
| Some fork-PR uploads return `401`, others succeed. | A subset of your workflow files is not passing `public-repo-id` through. Search your `.github/workflows` for `public-repo-id`. |
| Uploads succeed but results show up under the wrong repo. | The identifier corresponds to a different repository than you expect. Re-open the **Forked PR uploads** card on the correct repo and copy the value shown there. |
