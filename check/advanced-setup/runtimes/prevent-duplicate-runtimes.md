---
description: Configuration to avoid duplicate runtimes
---

# Prevent Duplicate Runtimes

If you would like to avoid having two copies of a specific runtime; For example, the system-managed version, and the Trunk-managed version, then you can always format your `trunk.yaml` file accordingly.

```yaml
runtimes: 
  enabled: 
    - go@x.y.z

# or
runtimes:
  enabled:
    - go@>=x.y.z
  definitions: 
    - type: go
      system_version: allowed
```

If you choose to use a system-managed version, you will also need to specify a runtime version constraint in your enabled section, e.g. `python@>=3.0.0`.
