# Logging and Troubleshooting

We provide a number of tools for inspecting the results of actions that run in the background and wouldn't otherwise surface their errors.

Every action execution is logged. We consider an action execution to have failed if it has a non-zero exit code.

`trunk actions history <action_id>` gives a history of the recent runs of an action and whether it succeeded. You can control how many recent runs to show with the `--count` flag (ie. `trunk actions history trunk-upgrade-available --count=10`). When available, a full stacktrace is written to a file and made available.

Failed action executions will also produce a notification so that background failures are periodically surfaced to the user.

You can inspect also inspect action logs at `.trunk/out/actions/<action_id>/`.

We recommend running actions manually when you develop them in order to verify that they work correctly.

### Output Level

In order to see a more verbose output when running trunk actions, particularly from git-hooks, you can add the following to your `trunk.yaml`:

```yaml
actions:
  output_level: <hidden/short/verbose>
```
