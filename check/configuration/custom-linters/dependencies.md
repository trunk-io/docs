
# Tool Download and Installation


## Hermetic Installs

You can use the `tools` section to specify trunk configured binaries that the linter uses to run.
The `tools` key should specify a list of tool names. We have two kinds of tool dependencies - 
they are described in turn below. 
See the [Tools Configuration](../../advanced-setup/tools/configuration.md) page for more details
on how to set up your tools.

Using tools is the preferred way of defining and versioning a linter, as it also allows repo 
users to conveniently run the linter binary outside of the `trunk check` context.

## Eponymous Tool Dependencies

Here is an example of where the tool matches the linter name:

```yaml
tools:
  definitions:
    - name: pylint
      runtime: python
      package: pylint
      shims: [pylint]
      known_good_version: 2.11.1
lint:
  definitions:
    - name: pylint
      files: [python]
      commands:
        - name: lint
          # Custom parser type defined in the trunk cli to handle pylint's JSON output.
          output: pylint
          run: pylint --exit-zero --output ${tmpfile} --output-format json ${target}
          success_codes: [0]
          read_output_from: tmp_file
          batch: true
          cache_results: true
      tools: [pylint]
      suggest_if: config_present
      direct_configs:
        - pylintrc
        - .pylintrc
      affects_cache:
        - pyproject.toml
        - setup.cfg
      issue_url_format: http://pylint-messages.wikidot.com/messages:{}
      known_good_version: 2.11.1
      version_command:
        parse_regex: pylint ${semver}
        run: pylint --version
```

In this case, the tool name (`pylint`) matches that of the linter, making it an _eponymous tool_. Eponymous tools need to be defined separately from the linter but implicitly enabled with the linter's version. You may explicitly enable the eponymous tool if you wish, but note that its version needs to be synced to that of the linter.

## Additional Tool Dependencies

You can also have a scenario where a linter depends on a tool that is not identically named - an 
_additional tool dependency_. We give an example below:

```yaml
tools:
  definitions:
    - name: terragrunt
      known_good_version: 0.45.8
      download: terragrunt
      shims:
        - name: terragrunt
          target: terragrunt
lint:
  definitions:
    - name: terragrunt
      tools: [terragrunt, terraform]
      known_good_version: 0.45.8
      files: [hcl]
      suggest_if: never
      environment:
        - name: PATH
          list: ["${linter}"]
      commands:
        - name: format
          output: rewrite
          run: terragrunt hclfmt ${target}
          success_codes: [0]
          sandbox_type: copy_targets
          in_place: true
          formatter: true
          batch: true
      version_command:
        parse_regex: terragrunt v${semver}
        run: terragrunt -version
```

In this scenario, `terraform` is an additional tool dependency - `terragrunt` requires it to be 
in `$PATH`. If the tool is an additional dependency, it must be enabled explicitly and versioned 
independently of the linter - that is, it must be listed in the `tools.enabled` section.


## Download via package manager

If your linter can be downloaded via `gem install`, `go get`, `npm install`, or `pip install`, you can specify a `runtime` and the `package` key:

```yaml
lint:
  definitions:
    - name: fizz-buzz
      files: [javascript]
      # npm install fizz-buzz
      runtime: node
      package: fizz-buzz
```

This will now create a hermetic directory in `~/.cache/trunk/linters/fizz-buzz` and `npm install fizz-buzz` there. You can refer to different versions of your package in `trunk.yaml` as normal, via `fizz-buzz@1.2.3`.

> Note: Such downloads will use the _hermetic_ version of the specified runtime that `trunk` installs, not the one >you've installed on your machine.
