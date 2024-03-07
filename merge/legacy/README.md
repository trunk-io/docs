---
description: Older version of Merge.
---

# Legacy Merge

{% hint style="info" %}
This documentation is for the older version of Merge. Use if it you initially set up your Merge config **before November 16, 2023**. If you setup Merge later, then use the [new merge docs](https://github.com/trunk-io/gitbook/blob/main/merge/README.md). If your Merge console has a _**graph**_ tab, then you should use the new merge docs instead.

**To migrate to the new Merge**, all you have to do is **delete and then recreate your queue**. It is recommend that you **pause** your queue and ensure it is empty before doing this so that no PRs get dropped. Also, if you are using the cli, be sure to add `service:graph` in your `.trunk/trunk.yaml` inside the `merge` section.
{% endhint %}

Trunk Merge is a service that enables your repository to adhere to The “Not Rocket Science Rule Of Software Engineering”: **Automatically maintain a repository of code that always passes all the tests.**

## How It Works

Trunk Merge adds an additional test pass before merging pull requests. For example, a typical developer workflow for authoring a feature and merging the code to a repository might look like this:

1. Create a feature branch from the main branch
2. Author a Change
3. Open a Pull Request
4. Tests are Run
5. Code Review
6. When tests & code review pass, Author merges request

In a repository with many contributors, the state of the main branch will have advanced significantly after step 1. Because of this, the results of the tests run in step 4 are out of date. Merge solves for this by adding another test pass to ensure no broken code lands on your main branch. A developer workflow with Merge integrated might look like this:

1. Create a feature branch from the main branch
2. Author a Change
3. Open a Pull Request
4. Tests are Run
5. Code Review
6. When tests & code review pass, Author submits pull request to Merge
7. Tests are run on a branch consisting of head of main + the pull request changes
8. If the tests pass, the pull request is merged automatically

## Demo

Watch this 5 minute demo to see how it works in practice

{% embed url="https://youtu.be/0iC_fK6arXI" %}
