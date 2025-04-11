# Pending Failure Depth

By default, a PR that fails testing will be evicted from the queue. The **Pending Failure Depth** feature allows a failed PR to remain in the queue for pull requests behind it to finish testing before this eviction occurs. The number of PRs that the queue will wait for is the _Pending Failure Depth._ This depth is configurable and reflects the number of pull requests behind this one that should complete testing before eviction is assessed. \
\
Let's take the example queue below:\
\
`main` <- **A** <- **B** <- **C**\
\
If _pending failure depth_ is set to 2 and **A** fails, Trunk Merge Queue will wait until both **B** and **C** complete testing before retrying or kicking **A** out of the queue.\
\
**Why does this matter?**\
Since trunk merge performs predictive testing when the queue above is tested it is actually testing the code like this:\
\
`main` <- <mark style="color:red;">**A**</mark> <- **B**+a <- **C**+ba\
\
The code in A is actually being tested when both **B** and **C** are being tested. We can take advantage of this feature of [predictive testing](predictive-testing.md) to give pull request **A** a second and third chance to pass tests.\
\
That means that if pull request **A** fails because of a flaky test it doesn't have to be immediately rejected and can leverage the test coverage it receives during the testing of **B** and **C**. By combining pending failure depth with optimistic merging - we can create a merge queue better [protected from flaky failures](anti-flake-protection.md).&#x20;
