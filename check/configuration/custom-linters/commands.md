# Commands

Once Trunk has figured out which linters it will run on which files, Trunk expands the template 
provided in the `run` field to determine the arguments it will invoke the linter with. Here's 
what that looks like for `detekt`, one of our Kotlin linters:

```yaml
lint:
  definitions:
    - name: detekt
      # ...
      commands:
        - output: sarif
          run:
            detekt-cli --build-upon-default-config --config .detekt.yaml --input ${target} --report
            sarif:${tmpfile}
```

This command template contains all the information Trunk needs to execute `detekt` in a way 
where Trunk will be able to understand `detekt`'s output.


## Trunk Variables

Note that some of the fields in this command template contain `${}` tokens: these tokens are why 
`command` is a template and are replaced at execution time with the value of that variable 
within the context of the lint action being executed.

| Variable          | Description                                                                   |
| ----------------- | ----------------------------------------------------------------------------- |
| `${workspace}`    | Path to the root of the repository                                            |
| `${target}`       | Path to the file to check, relative to `${workspace}`                         |
| `${linter}`       | Path to the directory the linter was downloaded to                            |
| `${runtime}`      | Path to the directory the runtime (e.g. `node`) was downloaded to             |
| `${upstream-ref}` | Upstream git commit that is being used to calculate new/existing/fixed issues |
| `${plugin}`       | Path to the root of the plugin's repository                                   |

