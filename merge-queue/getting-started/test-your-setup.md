# Test your setup

### Prerequisites

After completing configuration, verify your setup:

* [ ] `trunk-io` bot is added to push restrictions for your protected branch
* [ ] No branch protection rules apply to `trunk-temp/*` or `trunk-merge/*` branches
* [ ] If using Draft PR mode: Required status checks are configured in GitHub branch protection
* [ ] If using Push-triggered mode:
  * [ ] CI workflows trigger on `trunk-merge/**` branches
  * [ ] `merge.required_statuses` is defined in `trunk.yaml`

#### **Test your configuration**

1. Create a test pull request
2. Comment `/trunk merge` on the pull request
3. Check the [Trunk Dashboard](https://app.trunk.io/) to monitor your pull request status
4. The pull request should appear in the queue as "Queued" until all checks complete
5. Click on the pull request in the dashboard to see detailed status of what it's waiting for
6. You'll also see status updates in the comments on your pull request

**Expected behavior:** Your pull request should progress through testing and merge automatically once all required checks pass.

### Next Steps

🎉 **Congratulations!** Your Merge Queue is working. You're ready to use it with your team.

#### Start using Merge Queue

→ [**Submit and cancel pull requests**](../using-the-queue/reference.md) - Learn how to use the queue day-to-day

#### Optimize your queue

Ready to make it even better? Explore these optimizations

→ [**Predictive Testing**](../optimizations/predictive-testing.md) - Prevent queue collapse and increase throughput

→ [**Batching**](../optimizations/batching.md) - Merge multiple PRs together for faster processing

→ [**Priority merging**](../optimizations/priority-merging.md) - Fast-track urgent PRs

→ [**Anti-flake protection**](../optimizations/anti-flake-protection.md) - Handle flaky tests automatically

#### Configure integrations

→ [**Slack integration**](../administration/integration-for-slack.md) - Get notifications in Slack

→ [**Metrics and monitoring**](../administration/metrics.md) - Track your queue's performance



_Having trouble?_ See our [Troubleshooting guide](../reference/troubleshooting.md) for common installation issues.
