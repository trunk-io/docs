---
description: Trunk Code Quality usage data tracking
---

# Telemetry

Trunk sends basic usage metrics from our local tools ([CLI](../advanced-setup/cli/) & [VS Code Extension](../ide-integration/vs-code.md)) to our analytics system to help us understand our usage and improve our tools over time.  We do not send your code or codebase to our backend.

## Why we collect usage data

Our product team constantly works on feature enhancement and new areas to invest in. Usage data allows us best to understand the ergonomics and performance of our tools. For example, if we add a new subcommand to the command line interface - how often is it used? Additionally, usage data is gathered to track usage and compliance against our free and paid product offerings.

To give concrete examples: we track our users' client version and operating system to understand backward compatibility requirements, and the time it takes our user base to upgrade to our latest releases.

## Example usage data

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "anonymous_id": &#x3C;GUID>,
  "command":  "check --all",
  "launcher_version": "1.2.3",
  "os": "macOS",
  "release": 1.4.1,
  "source": "client",
  "time": &#x3C;UTC_TIMESTAMP>,
  "exit_code": 0,
  "duration_ms": 232,
  "repository":&#x3C;REPO_IDENTIFIER>
}
</code></pre>

## Can I disable usage data?

Yes. You can disable usage telemetry by setting the following environment variable:

```bash
TRUNK_TELEMETRY=off
```
