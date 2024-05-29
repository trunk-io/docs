---
description: >-
  Merge Queue's create predictive branches to verify that the future state of
  your protected branch will remain green when the contents of the queue merge
  into it.
---

# How does it work?

**How does a merge queue work?**

1. Instead of merging your pull requests directly through GitHub, engineers submit their pull requests to the merge queues service. A pull request can be submitted to the queue before passing CI or code review is complete. Once the pre-requisites for the queue have been met - the pull request will formally enter the queue.
2. Trunk Merge will test your pull request against the changes ahead of it in the queue so that the changes are tested against the predicted view of the branch, assuming everything ahead of it merges successfully. This process is called [**predictive testing** ](predictive-testing.md)and is illustrated in the video below.
3. When all the required tests are passing, Trunk will merge your pull request into the protected branch automatically.
4. If your pull requests fails testing - it will either be retested or removed from the queue for further inspection by the author.

{% embed url="https://share.vidyard.com/watch/31gaLwGNSYTn2ec2BSQjkn" %}
predictive testing // test pull requests ahead of you in the queue with your changes
{% endembed %}

\
**What happens under the hood when I submit a pull request to the queue?**

1. Trunk Merge will wait until all the normal gating tests for a pull request are passing. By default, this is the list of required status checks and code review requirements you have configured for pull requests to pass before they can be merged onto `main`
2. Once the pre-requisites are met, Trunk Merge will create a temporary branch with the naming convention `trunk-merge/***`. This branch will be based on the head of `main` and will include the changes in your pull request and the changes from pull requests ahead of your pull request in the queue. This is the predictive branch described above and is used to guarantee the correctness of your system.&#x20;
3. The same tests that are required for your pull request will now be run on this predictive branch. When those tests pass - your original pull request will be merged into `main`.&#x20;

