# Linter Definition

Simply defining a linter does not enable it. Trunk needs to know when to auto-enable
the linter for certain projects (ex: all python projects) or if certain files are
already present (ex: `.eslintrc`).


## Auto Enabling

The `direct_configs` property contains a list of config files that the underlying linter uses.
The `suggest_if` property determines when `trunk check` should suggest this linter. If
`suggest_if` is set to `config_present`, then trunk will search for the listed config files. If 
found, the linter will be enabled automatically when the user does `trunk init` or `trunk update`.

For example: in the following yaml, the **flake8** linter sets `suggest_if` to `config_preset`
and sets `direct_configs` to `[.flake8]`. If any `*.flake8` files are found, then trunk check
will automatically enable flake8.

**Flake8** linter definition. [full source](https://github.com/trunk-io/plugins/blob/main/linters/flake8/plugin.yaml)

```yaml
version: 0.1
tools:
  definitions:
    - name: flake8
      runtime: python
      package: flake8
      shims: [flake8]
      known_good_version: 4.0.1
lint:
  definitions:
    - name: flake8
      files: [python]
      tools: [flake8]
      direct_configs: [.flake8]
      suggest_if: config_present
      affects_cache:
        - setup.cfg
        - tox.ini
        # In case the user installs https://pypi.org/project/Flake8-pyproject/
        - pyproject.toml
      issue_url_format: https://flake8.pycqa.org/en/latest/user/error-codes.html
      known_good_version: 4.0.1
      version_command:
        parse_regex: ${semver}
        run: flake8 --version

```

The **suggest_if** field can be one of the following:

* `config_present` will auto-enable a linter if Trunk sees any `direct_config` for it .
* `files_present` will auto-enable a linter if Trunk sees any file type that it operates on.
* `never` will never auto-enable this linter.

Trunk curates the values of `suggest_if` for all linters in the [plugins](https://github.com/trunk-io/plugins) repo.


## Manually enabling and disabling

Setting the `lint.definitions[*].enabled` property to true will force the linter to be enabled.
Setting the `lint.definitions[*].disabled` property to true will force the linter to never
be enabled, even if the `enabled` property is true, and will never suggest this linter, even
if `suggest_if` says it should.

For additional information on the properties of Linters, see 
the [Linter Definition Reference](linter-definition.md). 

