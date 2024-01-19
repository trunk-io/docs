# Runtimes

Trunk makes it easy for you to run tools (such as linters and actions) because, under the hood, Trunk actually downloads everything a given tool depends on, and then executes said tool in the context of its dependencies. In other words, you can run tools like `golangci-lint` and `rubocop` without wasting hours figuring out how to install the right Go and Ruby versions on your machine, because Trunk will install a `go` and `ruby` runtime for those tools to depend on.

Importantly, just like how Trunk by design requires you to version your tools, i.e. specify which version of `golangci-lint` and `rubocop` is enabled in your repository at a given commit, Trunk also versions your runtimes. This means that you can stop asking questions like "wait, which version of Go are you using?" and "how do I choose a Ruby version to install on this new Jenkins runner?"; instead, all you have to do is look at the `runtimes` section in your `.trunk/trunk.yaml`, and you know which version of which runtime Trunk will use for a tool at any given moment:

```
runtimes:
  enabled:
    - go@1.18.3
    - node@16.14.2
    - python@3.10.3
    - ruby@3.1.0
```

## How does this work?

Runtimes are defined by a combination of configuration and native code inside Trunk itself. Let's walk through an example, `prettier`:

```yaml
lint:
  definitions:
    - name: prettier
      runtime: node
      package: prettier
      commands:
        - run: prettier -w ${target}
          ...
```

Since Prettier uses the `node` runtime, let's also look at that definition; specifically, the `runtime_environment` and `linter_environment`:

```yaml
runtimes:
  definitions:
    - type: node
      linter_environment:
        - name: PATH
          list:
            - ${linter}/node_modules/.bin
      runtime_environment:
        - name: HOME
          value: ${home}
        - name: PATH
          list:
            - ${runtime}/bin
```

Now we have all the config fields we need to understand what Trunk does in this example.

### Installing `prettier`

Before Trunk can run `prettier`, it needs to install `prettier`; this is done using the package manager associated with a given runtime, the mechanism for which is defined natively inside Trunk (i.e. Trunk has custom code for every runtime to manage how packages for said runtime are installed).

For most runtimes, this is as simple as executing the runtime's package manager in the context of the `runtime_environment`; in this example, that means doing `npm install ${package}` with environment variables `HOME=${home}` and `PATH=${runtime}/bin`.

### Running `prettier`

Once `prettier` is installed, we combine its runtime's `linter_environment` with any other environment variables that might be defined in a given `lint.definitions` entry (in this case there are none), and then use that as the environment when we execute the command for a given linter.
