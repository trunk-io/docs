# Per User Overrides

## Per-User Customization

Trunk can also be managed by the `.trunk/user.yaml` file in your repository. This file is optional, but it allows individual developers to customize how they want `trunk` to run on their machines.

Simply configure `.trunk/user.yaml` as you would for `.trunk/trunk.yaml`. Now you can add additional linters, enable [actions](../getting-started/actions/), or specify [default command options](./#cli), without impacting the way other developers run `trunk`.

Be mindful that `.trunk/user.yaml` takes precedence over `.trunk/trunk.yaml`, so substantial modifications could violate hermeticity.

## Identity Config

Trunk also saves a user config in `$HOME/.cache/trunk/user.yaml`. This is auto-generated in order to manage [anonymous usage data](telemetry.md) and persist login sessions.
