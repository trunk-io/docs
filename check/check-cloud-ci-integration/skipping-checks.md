# Skipping Checks

## Bypass `trunk check` on a Pull Request

Sometimes you need to bypass a failing `trunk check` job on an individual pull request. To bypass the failing pull request add `/trunk skip-check` as a comment or in the description of the pull request before Trunk Check runs (if it has already run, restart it).



If you are using the Trunk GitHub action, then you will need to ensure the job has the following configuration:

`permissions:`\
&#x20; `pull-requests: read`

> Note:`trunk check` will still run in this case and report issues, but the job will always return a passing exit code.
