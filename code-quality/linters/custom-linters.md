# Custom Linters

Trunk Code Quality allows you to define custom linters. If a linter is not within the [list of supported linters](supported/) or you have a bespoke solution, you can define a custom linter.

### Defining a Custom Linter

You can define linters right in your `.trunk/trunk.yaml` file in your repo. These definitions have the same configurable parameters as in our [public plugins repo](https://github.com/trunk-io/plugins/blob/main/CONTRIBUTING.md) or [your own plugins repo](../../references/cli/configuration/plugins/external-repositories.md).

#### Pass-Fail Linter Script Example

For example, you can define a simple [pass-fail linter](custom-linters.md#pass-fail-linter-script-example) that runs a custom script file. The linter passes or fails based on the status code returned.

```yaml
version: 0.1
cli:
  version: 1.22.1
lint:
  enabled:
    - SampleLinter
  definitions:
    - name: SampleLinter
      files: [javascript, typescript]
      commands:
        - name: lint
          run: sh ${workspace}/.trunk/myscript.sh ${target}
          output: pass_fail
          success_codes: [0, 1]
```

#### Inline Grep Command Example

You can also define simple linters inline using tools like `grep`. This linter will grep against your custom regex pattern, format the output using sed, and then parse the output into pattern groups using a [regex output](../../references/cli/configuration/lint/output.md#regex) for Trunk Code Quality to report.

```yaml
# This file controls the behavior of Trunk: https://docs.trunk.io/cli
# To learn more about the format of this file, see https://docs.trunk.io/cli/configuration
version: 0.1
cli:
  version: 1.22.1
lint:
  enabled:
    - SampleGrepLinter
  definitions:
    - name: SampleGrepLinter
      files: [ALL]
      commands:
        - name: lint
          run: bash -c "grep -o -E '<YOUR_PATTERN>' --line-number --with-filename ${target}"
          success_codes: [0, 1]
          read_output_from: stdout
          parser:
            run: 'sed -E "s/([^:]*):([0-9]+):(.*)/\1:\2:0: [error] Found \3 in line (numeric-\3)/"'
          output: regex
          parse_regex: "(?P<path>.*):(?P<line>-?\\d+):(?P<col>-?\\d+): \\[(?P<severity>[^\\]]*)\\] (?P<message>[^\\(]*) \\((?P<code>[^\\)]*)\\)"
```

To see the configurable fields available [Linter Definition Reference](../../references/cli/configuration/lint/definitions.md).

### Contributing a New Linter

The [Trunk Code Quality plugins repo](https://github.com/trunk-io/plugins/blob/main/CONTRIBUTING.md) is public and welcomes contributions. Feel free to open a PR if the new custom linter you defined could be useful to others. You can reach out to us [on Slack](https://slack.trunk.io/) if you need a hand.
