---
description: Trunk Check suppresses pre-existing issues so only new issues are flagged
---

# Hold the Line

Linters usually operate only on source code and have no awareness of your commit history, which makes introducing a linter into an existing codebase a nightmarish exercise. Sure, this new linter may be flagging all sorts of potential existing bugs in your code, but you've got features to ship and you know your code works as is, so clearly those potential bugs aren't showstoppers.&#x20;

Trunk Checks ability to [hold-the-line](../#hold-the-line) suppresses pre-existing issues, which means only new issues are flagged. We achieve this by checking both your mainline and in-progress code and comparing the results and source code to determine which issues you actually care about.

How it works
