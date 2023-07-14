# Prevent Duplicate Runtimes

If you would like to avoid having two copies of a specific runtime; For example, the system-managed version, and the Trunk-managed version, then you can always format your `trunk.yaml` file accordingly. \[block:code] { "codes": \[ { "code": "runtimes:\n enabled:\n - go@x.y.z\n\nor\n\nruntimes:\n definitions:\n - type: go\n system\_version: allowed", "language": "yaml" } ] } \[/block]
