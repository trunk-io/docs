---
description: >-
  Trunk Actions can also produce notifications to display in your terminal or in
  the VSCode extension!
---

# Notifications

### Defining actions that produce notifications

Typically, whatever actions write to stdout is stored in the log file and perhaps shown to the user. However, actions can also produce structured output if `output_type` is set on the Action Definition to be `notification_v1`.

In this case, the action should print yaml to output with the following structure:

```yaml
notifications:
  - id: action-id
    # Display-related fields
    title: My action
    message: some text about the notification
    rendered: A rendered message string for color terminals
    icon: https://uri/to/icon
    commands:
      - title: A button title
        run: a run command
        run_from: directory to run from
    priority: high # Can be one of low, high (default low)
```

Some notes:

1. The ID can be whatever you want it to, but generally should be made to match the action ID.
2. You may emit multiple notifications per action.
3. `icon` and `commands` are used to control notifications display in VSCode.
4. High priority notifications are immediately shown to the user in terminal. Low priority notifications are only shown every 24 hours (These are configurable).

### Deleting notifications

Actions can also clear their own notifications. in this case, make the output looks like this:

```yaml
notifications_to_delete: [action-id]
```

If actions produce a notification that is reflective of a current state or something actionable for the user to do, they may clear the notification once that state changes/when the user takes the requested action.

### An example

We illustrate the cycle of actions managing their own notifications with the following example.

Consider the built-in action for `trunk upgrade` - a command that upgrades trunk and a repo's enabled linters to their most recent versions. We'd like to notify the user of new upgrades once a day. Thus our `trunk-upgrade-available` action definition looks like this:

```yaml
id: trunk-upgrade-available
output_type: notification_v1
run: trunk upgrade --notify
triggers:
  - schedule: 1h
  - files: [.trunk/trunk.yaml]
```

`trunk upgrade --notify` produces a notification that looks like this:

```yaml
notifications:
  - commands:
      - run: trunk upgrade
        title: Upgrade Trunk
    id: trunk-upgrade
    message: "Upgrades available\n\n  Trunk version 0.17.0-beta\n  10 linter updates\n\nRun trunk upgrade to upgrade all\n or trunk upgrade trunk to just upgrade trunk"
    priority: low
    rendered: "\x1b[1m\x1b[90m\nUpgrades available\x1b[0m\n\x1b[90m\n\x1b[0m• \x1b[90mTrunk version\x1b[0m \x1b[92m0.17.0-beta\x1b[0m\x1b[90m\n\x1b[0m• \x1b[92m11 linter\x1b[0m \x1b[90mupdates\n\x1b[0m\n\x1b[90mRun\x1b[0m\x1b[96m trunk upgrade\x1b[0m\x1b[90m to upgrade all\x1b[0m\x1b[90m\n or\x1b[0m\x1b[96m trunk upgrade trunk\x1b[0m\x1b[90m to just upgrade trunk\x1b[0m\x1b[90m\n\x1b[0m"
```

If there are no upgrades available, `trunk upgrade --notify` will produce:

```yaml
notifications_to_delete: [trunk-upgrade-available]
```

So in this scenario, the `trunk-upgrade-available` action runs in the background periodically and produces a notification. The user takes action by running `trunk upgrade`. Since `trunk upgrade` modifies `.trunk/trunk.yaml`, this will again trigger the `trunk-upgrade-available` action (due to the file trigger). Since there is nothing else to upgrade, `trunk upgrade --notify` will produce output telling Trunk to delete its notification. Now, the user is no longer shown a notification about available upgrades!
