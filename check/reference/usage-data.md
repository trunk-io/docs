# Telemetry

Trunk sends certain metrics to our analytics system to help us understand our usage and improve our tools over time.&#x20;

## Why we collect usage data

Our product team constantly works on feature enhancement and new areas to invest in. Usage data allows us best to understand the ergonomics and performance of our tools. For example, if we add a new subcommand to the command line interface - how often is it used? Additionally, usage data is gathered to track usage and compliance against our free and paid product offerings.

To give a concrete example, we track the client version and operating systems of our users to understand backward compatibility requirements, and the time it takes our user base to upgrade to our latest releases.

## Example usage data

```json
{
          "anonymous_id": <GUID>,
          "command":  "check --all",
          "launcher_version": "1.2.3",
          "os": "macOS",
          "release": 1.4.1,
          "source": "client",
          "time": <UTC_TIMESTAMP>,
          "exit_code": 0,
          "duration_ms": 232,
          "repository":<REPO_IDENTIFIER>
}
```

## Can I disable usage data?

Yes. You can disable usage telemetry by setting the environment variable `TRUNK_TELEMETRY=off`.
