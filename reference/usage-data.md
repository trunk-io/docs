# Usage Data

Trunk sends certain metrics to our analytics system and we want you to better understand what is being sent and why it's important for our ability to continue to improve the product and provide our users with a better experience over time.

## Why we collect usage data?

Our product team is constantly working on feature enhancement and new areas to invest in. Usage data allows us to best understand the ergonomics and performance of our existing tools. For example, if we add a new subcommand to the command line interface - how often is it actually used? Additionally usage data is gathered in order to track usage and compliance against with our free and paid product offerings.

To give a concrete example, we track the client version and operating systems of our users in order to understand backwards compatibility requirements and understand the time it takes our user base to upgrade onto our latest releases.

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

Yes. You can disable usage telemetry by setting the environment variable TRUNK\_MIXPANEL to "off."
