---
description: Custom Linters should output one of several output formats.
---

# Output Types

Trunk supports several different generic output types. If your linter doesn't conform well to any of these specifications, you can also write a [custom parser](custom-parsers.md).

#### SARIF

`output: sarif` linters produce diagnostics in the [Static Analysis Results Interchange Format](https://docs.oasis-open.org/sarif/sarif/v2.0/sarif-v2.0.html):

```json
{
  "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
  "version": "2.1.0",
  "runs": [
    {
      "results": [
        {
          "level": "warning",
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": {
                  "uri": "/dev/shm/sandbox/detekt_test_repo/example.kt"
                },
                "region": {
                  "startColumn": 12,
                  "startLine": 18
                }
              }
            }
          ],
          "message": {
            "text": "A class should always override hashCode when overriding equals and the other way around."
          },
          "ruleId": "detekt.potential-bugs.EqualsWithHashCodeExist"
        }
      ],
      "tool": {
        "driver": {
          "downloadUri": "https://github.com/detekt/detekt/releases/download/v1.19.0/detekt",
          "fullName": "detekt",
          "guid": "022ca8c2-f6a2-4c95-b107-bb72c43263f3",
          "informationUri": "https://detekt.github.io/detekt",
          "language": "en",
          "name": "detekt",
          "organization": "detekt",
          "semanticVersion": "1.19.0",
          "version": "1.19.0"
        }
      }
    }
  ]
}
```

#### LSP JSON

`output: lsp_json` linters output issues as [Language Server Protocol](https://microsoft.github.io/language-server-protocol/specification#diagnostic) JSON.

```json
[
  {
    "message": "Not formatted correctly. Missing owner",
    "code": "missing-owner",
    "severity": "Error",
    "range": {
      "start": {
        "line": 12,
        "character": 8
      },
      "end": {
        "line": 12,
        "character": 12
      }
    }
  },
  {
    "message": "TODO is assigned to someone not listed in this project",
    "code": "unknown-user",
    "severity": "Warning",
    "range": {
      "start": {
        "line": 37,
        "character": 0
      },
      "end": {
        "line": 37,
        "character": 14
      }
    }
  }
]
```

#### Pass/Fail Linters

`output: pass_fail` linters find either:

* no issues in a file, indicated by exiting with `exit_code=0`, or
* a single file-level issue in a file, whose message is the linter's `stdout`, indicated by exiting\
  with `exit_code=1`.

> Note: Exiting with `exit_code=1` but writing nothing to `stdout` is considered to be a linter tool failure.
>
> Note: `pass_fail` linters are required to have `success_codes: [0, 1]`

#### Regex

`output: regex` linters produce output that can be parsed with custom regular expressions and named capture groups. The regular expression is specified in the `parse_regex` field.

`regex` supports capturing strings from a linter output for the following named capture groups:

* `path`: file path (required)
* `line`: line number
* `col`: column number
* `severity`: one of `allow`, `deny`, `disabled`, `error`, `info`, `warning`
* `code`: linter diagnostic code
* `message`: description

For example, the output

```
.trunk/trunk.yaml:7:81: [error] line too long (82 > 80 characters) (line-length)
```

can be parsed with the regular expression

```
((?P<path>.*):(?P<line>\d+):(?P<col>\d+): \[(?P<severity>.*)\] (?P<message>.*) \((?P<code>.*)\))
```

and would result in a `trunk` diagnostic that looks like this:

```
7:81  high    line too long (82 > 80 characters)      regex-linter/line-length
```

In the event that multiple capture groups of the same name are specified, the nonempty capture will be preferred. If there are multiple non-empty captures, a linter error will be thrown. Adjust your regular expression accordingly to match the specifics of your output.

> Note: For additional information on building custom regular expressions, see [re2](https://github.com/google/re2/wiki/Syntax). More complicated regex may require additional escape characters in yaml configuration.

#### Arcanist

You can also output JSON using the Arcanist format.

```json
[
  {
    "Char": 1,
    "Code": "missing_copyright",
    "Description": "Message about things\nMaybe contain multiple lines and web\nlinks\nhttps://website.com/notice-about-stuff\n",
    "Line": 1,
    "Name": "Incorrect (or missing) copyright notice",
    "OriginalText": "",
    "Path": "somefile.py"
  }
]
```

#### Formatters

`output: rewrite` linters write the formatted version of a file to `stdout`; this becomes an autofix which `trunk` can prompt you to apply (which is what `trunk check` does by default) or automatically apply for you (if you `trunk check --fix` or `trunk fmt`).

For example, if you wanted a linter to normalize your line endings, you could do this:

```yaml
lint:
  definitions:
    - name: no-carriage-returns
      files: [ALL]
      commands:
        - output: rewrite
          formatter: true
          command: sed s/\r// ${target}
          success_codes: [0]
```

Setting `formatter: true` will cause `trunk fmt` to run this linter.
