# Troubleshooting

#### Troubleshooting common issues

{% hint style="info" %}
Visit [Trunk Support](../../setup-and-administration/support.md) for additional assistance or to contact the support team.
{% endhint %}

If your test PR doesn't merge automatically:

* **Check the status comments for the PR in** the [Trunk Dashboard](https://app.trunk.io/) to see what it's waiting for
* **Stuck in "Queued"**: Usually means branch protection rules haven't passed (missing required status checks or code review) or there are merge conflicts. If the status looks correct but the PR still won't enter the queue, try [removing](/broken/pages/c7O7hgOoGwFcANCdzUMZ#manually-restarting-failed-prs) and re-adding by commenting `/trunk merge` again on the PR.
* **Fails when attempting to merge**: Check that squash merges are enabled for your repository in GitHub settings (`Settings > General > Allow squash merging`). Trunk Merge Queue requires squash merges to be enabled.
* **"Permission denied" errors**: Review the [Branch Protection](/broken/pages/zvDo6oVz6lP1OOz5wOUB#configure-branch-protection-rules) guide to ensure `trunk-temp/*` and `trunk-merge/*` branches aren't protected by wildcard rules like `*/*`.
* **Status checks not running**: Verify your CI is configured to run on draft PRs (or `trunk-merge/**` branches if using push-triggered mode). See the [Branch Protection](/broken/pages/zvDo6oVz6lP1OOz5wOUB#configure-branch-protection-rules) guide for details.

###

### Troubleshooting common issues

<details>

<summary>"Permission denied on trunk-merge/* branch"</summary>

**Cause:** Branch protection rules are applying to Trunk's temporary branches.

**Solution:** Follow the "Exclude Trunk's Temporary Branches" section above to ensure `trunk-temp/*` and `trunk-merge/*` are not protected.

</details>

<details>

<summary>Pull request stuck as "Queued" in the queue</summary>

**Cause:** Required status checks are not completing or not configured correctly.

**Solution:**

* Click on the pull request in the Trunk Dashboard to see which checks it's waiting for
* Verify those checks are running in your CI provider
* If using Push-triggered mode, ensure the check names in `trunk.yaml` exactly match your CI job names

</details>

<details>

<summary>Required status checks not running</summary>

**If using Draft PR mode:** Verify your CI workflows are triggered by pull requests (including draft pull requests).

**If using Push-triggered mode:**

* Verify your CI workflows trigger on pushes to `trunk-merge/**` branches
* Check that the workflows actually ran in your CI provider's interface
* Ensure the `trunk-io` bot has permission to push to create these branches

</details>
