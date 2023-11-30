# Debugging

Sometimes you need to get under-the-hood to diagnose why a linter is failing on a particular file or to more easily reproduce an issue you are seeing with a tool.

### Analyzing Linter Failures

When a linter fails, `trunk` will generate a linter failure report that contains all the information needed to understand what went wrong and why. `prettier`, for example, will fail on improperly formatted HTML; let's see what that looks like:

```shell
trunk/hello_world.html:0:0
 0:0  failure  prettier error (details: .trunk/out/lYa9w.yaml)  prettier
```

This tells us that `prettier` failed when `trunk` ran it on `trunk/hello_world.html` and that we can find a full report of the invocation in `.trunk/out/lYa9w.yaml`. This report will include:

1. the command that was run,
2. the environment (e.g. `cwd`, environment variables),
3. the invocation's `stdout`, `stderr`, and exit code, and
4. repro instructions.

All of this combined is generally sufficient to fix either the file or tool to get useful results out of the linter.

```yaml
title: "prettier error"
report:
  - command: |
      /home/horton/.cache/trunk/linters/prettier/2.3.2-368f87d0e434ae207c0a3622371f91cc/node_modules/.bin/prettier --stdin-filepath trunk/hello_world.html
    environment:
      HOME: /home/horton
      PATH: /home/horton/.cache/trunk/linters/node/16.14.2/bin:/home/horton/.cache/trunk/linters/prettier/2.3.2-368f87d0e434ae207c0a3622371f91cc/node_modules/.bin
    run_from: /tmp/trunk-Bi6hWP
    rerun:
      env -i -C /tmp/trunk-Bi6hWP HOME=/home/horton
      PATH=/home/horton/.cache/trunk/linters/node/16.14.2/bin:/home/horton/.cache/trunk/linters/prettier/2.3.2-368f87d0e434ae207c0a3622371f91cc/node_modules/.bin
      /home/horton/.cache/trunk/linters/prettier/2.3.2-368f87d0e434ae207c0a3622371f91cc/node_modules/.bin/prettier
      --stdin-filepath trunk/hello_world.html
    exit_code: 2
    stdout: (none)
    stderr: |
      [error] trunk/hello_world.html: SyntaxError: Unexpected closing tag "head". It may happen when the tag has already been closed by another tag. For more info see https://www.w3.org/TR/html5/syntax.html#closing-elements-that-have-implied-end-tags (3:2)
      [error]   1 | <html>
      [error]   2 |  head>
      [error] > 3 |  </head>
      [error]     |  ^^^^^^^
      [error]   4 |  <body>
      [error]   5 |    <h1>Hello World<h1>
      [error]   6 |  </body>
```

### Debugging Linter Failures in CI

If linter failures occur while Trunk Check is running in CI, you'll see something like this:

<figure><img src="../../.gitbook/assets/Screenshot 2023-10-16 at 5.09.29 PM.png" alt=""><figcaption></figcaption></figure>

To debug these, you'll need get the linter failure report(s) from the Github Actions output. Click on "Details" to see a screen like this:

<figure><img src="../../.gitbook/assets/Screenshot 2023-10-16 at 5.10.39 PM.png" alt=""><figcaption></figcaption></figure>



Then click on "View more details on trunk-io"

<figure><img src="../../.gitbook/assets/Screenshot 2023-10-16 at 5.11.57 PM.png" alt=""><figcaption></figcaption></figure>

You'll then see your check run summary. Click "\<your repo name>/pull\_request" to see the CI logs, and scroll all the way to the bottom.

<figure><img src="../../.gitbook/assets/Screenshot 2023-10-16 at 5.12.23 PM.png" alt=""><figcaption></figcaption></figure>

You'll then see a list of the failures that occurred, as well as all of the linter failure reports in collapsibles. You can then follow the instructions in [Analyzing Linter Failures](https://docs.trunk.io/check/debugging#analyzing-linter-failures) to resolve the problem.

### Actions

When `trunk check` is run, a dynamic set of check actions are generated and executed in parallel. An engineer developing custom integrations may find it helpful to examine in detail exactly what `trunk check` does and sees when it runs a given tool. The output of the `check` run will include an `ACTIONS` section with a execution report for each action that was run as well as cache hit information.

For example, to run a report on all actions taken on hello.py:

```bash
trunk check --verbose hello.py
```
