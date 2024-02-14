---
description: Trunk Check suppresses pre-existing issues so only new issues are flagged
---

# Hold the Line

## What is Hold the Line?

Linters usually operate only on source code and have no awareness of your commit history, which makes introducing a linter into an existing codebase a nightmarish exercise. Sure, this new linter may be flagging all sorts of potential existing bugs in your code, but you've got features to ship and you know your code works as is, so clearly those potential bugs aren't showstoppers.

Trunk Check has the ability to _**Hold The Line**_, which means it only lints your diffs; only the new code gets linted. The pre-existing issues can be managed later.&#x20;

## How does Hold the Line work?

_Hold the Line_ simplifies integrating a linter into your workflow by comparing the source code from your local working branch (your worktree) with the source code in your upstream (say, the github repo branch you are committing to). Trunk Check runs the linters twice, once for the upstream code and once for the work tree (although one or both is often cached to make it faster) and compares them to report only the issues found in new / changed code. _Hold the Line_ also works across configuration changes, such as changing the max line length in a linter, and adding/removing linters.

_Hold The Line_ **works at the line level** of your source code. For example, if a single line has multiple pre-existing issues and a new linter is added which reports the new issue, then Trunk Check will report just the new issue and not the previous ones.

_**Hold the Line**_** is built into Trunk Check itself.** This means existing linters that do not support line by line functionality will still work with _Hold the Line_. Also, when making a custom linter you do not need to do anything special to support _Hold the Line_. It just works!

## How can I disable or customize Hold the Line?

If you wish to run Trunk Check to _find issues in all of your code_, not just the newest changes, you can run with the `--all` option to scan all code.  We recommend you run it once with `--no-fix` to get an overview. You can also run it with `--filter` to only use certain linters.

```sh
trunk check --all --no-fix --filter=eslint
```

If you wish to run Trunk Check against all code changes since a particular release or timestamp of your codebase you can use the `--upstream` option to specify the upstream branch used to calculate new vs existing issues. See [Advanced Trunk Check Features](../advanced-setup/cli/cli-options.md#advanced-trunk-check-features) for more information.

