# Under the Hood

`trunk check` does a lot of cool stuff under the hood so that you have a good experience with it.

## Holding the Line

Linters usually operate only on source code and have no awareness of your commit history, which makes introducing a linter into an existing codebase a nightmarish exercise. Sure, this new linter may be flagging all sorts of potential existing bugs in your code, but you've got features to ship and you know your code works as is, so clearly those potential bugs aren't showstoppers. Trunk's ability to [hold-the-line](../check/overview.md#hold-the-line) suppresses pre-existing issues, which means only new issues are flagged. We achieve this by checking both your mainline and in-progress code and comparing the results and source code to determine which issues you actually care about.

## Caching and Reproducibility

Constantly re-running linters on all source code, the default mode of operation for most linters, is very time-consuming and gets frustrating fast when you know that you've only modified a few functions in these files, but the linters are re-linting all these other hundreds of files that you haven't modified. `trunk check` caches results so that you don't have to wait for linter work that's already been done, which is a surprisingly difficult thing to do:

- We need to guarantee that results are _reproducible_, which we achieve by sandboxing linter runs, similar to how Google's [Bazel](https://bazel.build/) project sandboxes compiler actions.
- We need to intelligently invalidate/ignore cache entries: if `fileA` is modified and check results for `fileB` depend on the contents of `fileA`, then check results for `fileB` from prior to `fileA`'s modification cannot be reused. We solve this by keying cache entries on the linter configuration, the actual linter target file, and all dependencies of said target file.

## Discarding Invalidated Results

Over the course of a `trunk check` run, changes made to the filesystem outside of Trunk may render linter results outdated or otherwise incorrect. For example, switching branches or merging from one's main branch might invalidate analysis in progress. Trunk will recognize these conditions, such as modified, missing, or read-only files requiring modification, and simply discard them from the results. The summary will include a notice of these discards along with their reason, and the client will exit with a non-zero status code to indicate the incomplete result.

## Why does trunk only work in a git repo?

`trunk` uses git to detect your changes so we only check the code you've changed. Additionally we use it to accurately detect errors _caused_ by your changes, even if the errors aren't on lines you changed. You'll read more about [hold-the-line](../check/overview.md#hold-the-lineld-the-line) later in the docs.
