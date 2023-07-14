# User YAML

## Per-User Customization

`trunk` can also be managed by the `.trunk/user.yaml` file in your repository. This file is optional, but it allows individual developers to customize how they want `trunk` to run on their machines.

Simply configure `.trunk/user.yaml` as you would for `.trunk/trunk.yaml`. Now you can add additional linters, enable [actions](../actions/overview.md), or specify [default command options](../reference/trunk-yaml.md#cli), without impacting the way other developers run `trunk`.

Be mindful that `.trunk/user.yaml` takes precedence over `.trunk/trunk.yaml`, so substantial modifications could violate hermeticity.

## Identity Config

Trunk also saves a user config in `$HOME/.cache/trunk/user.yaml`. This is initially auto-generated, but some fields can be user-configured.

### Disable upgrade notifications

Trunk will periodically tell you to upgrade to a newer version if one is available. If you prefer not to see these notifications, edit (or add) the section of your `.trunk/trunk.yaml` to include the following lines:

```yaml
actions:
  disabled:
    - trunk-upgrade-available
```
