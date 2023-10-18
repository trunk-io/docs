# Performance

## Caching

Where possible `check` will cache the results of a job. A valid cache result must take into account all inputs into a job that can affect cache correctness. This includes all deps/includes of a file, its contents and any configuration files that drive the results of a job.  \
\
Caching is currently enabled for about half the linters/formatters. Since Trunk needs to know all the inputs to a linter for a file/directory in order to cache the results, we don't yet cache every linter, but we are building out the functionality to do so. You can see which linters are currently configured to be cached by running `trunk print-config` and seeing which linter configurations have `cache_results: true` set. That's also how you can enable/disable caching for any custom linters you integrate.

If you pass `--verbose` flag when running check you can see which results were pulled from cache.&#x20;

<figure><img src="../.gitbook/assets/SCR-20230811-mtvw.png" alt=""><figcaption><p>trunk check --verbose output</p></figcaption></figure>

## CPU Utilization

By default `check` will run concurrent jobs using up to half the available cores on your machine. This default is intended to balance system utilization and check responsiveness. If `check` detects that it is running in a continuous integration environment or you pass the [`--ci`](command-line.md) flag, then it will instead use all cores on the machine. This behavior can be overwritten by manually calling `check` with the [`--jobs`](command-line.md#options) argument.&#x20;

## Memory Utilization

`check` does not current support a mechanism to throttle back jobs based on the memory consumption of concurrently runs jobs. In order to throttle memory utilization you can lower the \
[`--jobs`](command-line.md#options) count to indirectly reduct system load.

## Daemon

`trunk check` runs a daemon which monitors relevant file changes and triggers jobs to precompute in the background while you work. The daemon is used both to support realtime background checking in supported extensions (e.g. VS Code) and to precompute check results for faster commits/pushes. Some native linters are more compute/memory intensive and `check` supports disabling background linting of those tools. \
\
By default linters run whenever a file is modified in the background. You can override this behavior by editing the [`run_when`](custom-linters.md#run\_when) configuration for a tool. \
