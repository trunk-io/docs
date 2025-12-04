# Run Linters

The main commands when running `trunk` from the command line are:

```bash
trunk check       # runs the universal linter on all applicable files
trunk fmt         # runs all the enabled formatters and auto-applies changes
```

You can always find this list using `trunk check --help`.

{% hint style="info" %}
Trunk is git-aware. When you run `trunk check` it will **only run on files you've modified according to git**. To run on a sampling in your repo, run: `trunk check --sample 5`
{% endhint %}

### check

`trunk check` runs linters & formatters on your changed files, prompting you to apply fixes. Without additional args, `trunk check` will run all applicable linters on all files changed in the current branch.

### fmt

Run all applicable formatters as configured in `trunk.yaml`. `trunk fmt` is short-hand for running\
`trunk check` with a `--fix --filter` set to all formatters enabled in your repository.

## Options

<table><thead><tr><th width="238">options</th><th></th></tr></thead><tbody><tr><td><code>--all</code></td><td>Run on all the files in the repository. Useful if trying to assess a new linter in the system, or to find and fix pre-existing issues</td></tr><tr><td><code>--fix</code></td><td>Auto-apply all suggested fixes</td></tr><tr><td><code>--no-fix</code></td><td>Surface, but do not prompt for autofixes</td></tr><tr><td><code>--filter</code></td><td>List of comma-separated linters to run. Specify <code>--filter=-linter</code> to disable a linter.</td></tr><tr><td><code>--sample=N</code></td><td>Run check on a <a href="run-linters.md#sample">sampling</a> of all files in the repo</td></tr><tr><td><code>--help</code></td><td>Output help information</td></tr></tbody></table>

### Recipes

| Check                                                        | Command                                      |
| ------------------------------------------------------------ | -------------------------------------------- |
| all files                                                    | `trunk check --all --no-fix`                 |
| a specific file                                              | `trunk check some/file.py`                   |
| all applicable files with flake8                             | `trunk check --all --no-fix --filter=flake8` |
| a selection of five files in the repo                        | `trunk check --sample 5`                     |
| a selection of five files in the repo with a specific linter | `trunk check --sample 5 --filter=flake8`     |
| format the whole repo                                        | `trunk fmt --all`                            |
| format a specific file                                       | `trunk fmt some/file.py`                     |
| format all python code with `black`                          | `trunk fmt --all --filter=black`             |

