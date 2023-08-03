# Prevent Duplicate Runtimes

If you would like to avoid having two copies of a specific runtime; For example, the system-managed version, and the Trunk-managed version, then you can always format your `trunk.yaml` file accordingly.&#x20;

```yaml
runtimes: 
  enabled: 
    - go@x.y.z

# or
runtimes: 
  definitions: 
    - type: go
      system_version: allowed
```

