# Files and Caching

## Applicable filetypes

To determine which linters to run on which files (i.e. compute the set of lint actions), Trunk requires that every linter define the set of filetypes it applies to in `lint.files`, then reference those files from `lint.definitions[*].files`.

We have a number of pre-defined filetypes (e.g. `c++-header`, `gemspec`, `rust`; see our [plugins repo](https://github.com/trunk-io/plugins/blob/main/linters/plugin.yaml) for an up-to-date list), but you can also define your own filetypes. Here's how we define the `python` filetype:

```yaml
lint:
  files:
    - name: python
      extensions:
        - py
        - py2
        - py3
      shebangs:
        - python
        - python3
```

This tells Trunk that files matching either of the following criteria should be considered `python` files:

* the extension is any of `.py`, `.py2`, or `.py3` (e.g. `lib.py`)
* the shebang is any of `python` or `python3` (e.g. `#!/usr/bin/env python3`)

The **flake8** linter definition uses python files, so it references the filetype above in its definition.

```yaml
lint:
  definitions:
    - name: flake8
      files: [python]
      commands:
        ...
      affects_cache:
        - setup.cfg
        - tox.ini
        # In case the user uses https://pypi.org/project/Flake8-pyproject/
        - pyproject.toml
```

## Caching

Trunk Code Quality automatically caches results from previous runs of linters to speed up development. To do this Trunk needs to know which files could potentially affect the cache, besides the source code files themselves.

### Enabling caching

If a linter wishes Trunk to cache the results it should set `cache_results` to true.

## Files which affect caching

The `lint.definitions[*].affects_cache` property is a list of files which could affect the cache. General these are files which would change the configuration of the linter, and therefore invalidate the current cached results. For example, the **flake8** tool tells trunk to invalidate the cache whenever the `setup.cfg`, `tox.ini`, or `pyproject.toml` files are changed.

```yaml
lint:
  definitions:
    - name: flake8
      files: [python]
      commands:
        ...
      affects_cache:
        - setup.cfg
        - tox.ini
        # In case the user uses https://pypi.org/project/Flake8-pyproject/
        - pyproject.toml
```

### Idempotency

Trunk Code Quality also needs to know if the linter command itself is idempotent, meaning the command will return the exact same results given the exact same inputs. Most linters are, however semgrep, for example, fetches rules from the internet so the output could be different each time.

Setting the `linter.definitions[*].commands.idempotent` property to true will tell trunk to only cache the result for a duration of `cache_ttl`, which is set to 24hrs by default.
