# Under the Hood

`trunk check` does a lot of cool stuff under the hood so that you have a good experience with it.

## Hold the Line

Linters usually operate only on source code and have no awareness of your commit history, which makes introducing a linter into an existing codebase a nightmarish exercise. Sure, this new linter may be flagging all sorts of potential existing bugs in your code, but you've got features to ship and you know your code works as is, so clearly those potential bugs aren't showstoppers. Trunk's ability to [hold-the-line](./#hold-the-line) suppresses pre-existing issues, which means only new issues are flagged. We achieve this by checking both your mainline and in-progress code and comparing the results and source code to determine which issues you actually care about.

## Caching and Reproducibility

Constantly re-running linters on all source code, the default mode of operation for most linters, is very time-consuming and gets frustrating fast when you know that you've only modified a few functions in these files, but the linters are re-linting all these other hundreds of files that you haven't modified. `trunk check` caches results so that you don't have to wait for linter work that's already been done, which is a surprisingly difficult thing to do:

* We need to guarantee that results are _reproducible_, which we achieve by sandboxing linter runs, similar to how Google's [Bazel](https://bazel.build/) project sandboxes compiler actions.
* We need to intelligently invalidate/ignore cache entries: if `fileA` is modified and check results for `fileB` depend on the contents of `fileA`, then check results for `fileB` from prior to `fileA`'s modification cannot be reused. We solve this by keying cache entries on the linter configuration, the actual linter target file, and all dependencies of said target file.

### Performance

Where possible `check` will cache the results of a job. A valid cache result must take into account all inputs into a job that can affect cache correctness. This includes all deps/includes of a file, its contents and any configuration files that drive the results of a job.

Caching is currently enabled for about half the linters/formatters. Since Trunk needs to know all the inputs to a linter for a file/directory in order to cache the results, we don't yet cache every linter, but we are building out the functionality to do so. You can see which linters are currently configured to be cached by running `trunk print-config` and seeing which linter configurations have `cache_results: true` set. That's also how you can enable/disable caching for any custom linters you integrate.

If you pass `--verbose` flag when running check you can see which results were pulled from cache.

<figure><img src="../.gitbook/assets/SCR-20230811-mtvw.png" alt=""><figcaption><p>trunk check --verbose output</p></figcaption></figure>

## Discarding Invalidated Results

Over the course of a `trunk check` run, changes made to the filesystem outside of Trunk may render linter results outdated or otherwise incorrect. For example, switching branches or merging from one's main branch might invalidate analysis in progress. Trunk will recognize these conditions, such as modified, missing, or read-only files requiring modification, and simply discard them from the results. The summary will include a notice of these discards along with their reason, and the client will exit with a non-zero status code to indicate the incomplete result.

## Why does trunk only work in a git repo?

Trunk uses git to detect your changes so we only check the code you've changed. Additionally we use it to accurately detect errors _caused_ by your changes, even if the errors aren't on lines you changed. Read more about [hold-the-line](under-the-hood.md#hold-the-line).

## CPU Utilization

By default `check` will run concurrent jobs using up to half the available cores on your machine. This default is intended to balance system utilization and check responsiveness. If `check` detects that it is running in a continuous integration environment or you pass the [`--ci`](usage/) flag, then it will instead use all cores on the machine. This behavior can be overwritten by manually calling `check` with the [`--jobs`](usage/#options) argument.

## Memory Utilization

`check` does not current support a mechanism to throttle back jobs based on the memory consumption of concurrently runs jobs. In order to throttle memory utilization you can lower the\
[`--jobs`](usage/#options) count to indirectly reduct system load.

## Daemon

`trunk check` runs a daemon which monitors relevant file changes and triggers jobs to precompute in the background while you work. The daemon is used both to support realtime background checking in supported extensions (e.g. VS Code) and to precompute check results for faster commits/pushes. Some native linters are more compute/memory intensive and `check` supports disabling background linting of those tools.\
\
By default linters run whenever a file is modified in the background. You can override this behavior by editing the [`run_when`](configuration/custom-linters/#run\_when) configuration for a tool.&#x20;
