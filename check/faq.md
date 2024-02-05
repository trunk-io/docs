---
description: Frequently Asked Questions
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# FAQ

<details>

<summary>What linters should I be using?</summary>

The best set of linters depends on your particular needs and which tech stack you are using (C/C++, Javascript, Rust, Python, etc). By default Trunk Check will detect your project type and select a recommended set of linters for that type, ESLint for a Javascript project or `clang-tidy` for C++ projects. There are plenty more linters you can use, however. You can see all possible (built in) linters with

```sh
trunk check list
```

and enable a new linter with

```sh
trunk check enable cool_new_linter
```

See more about our [supported linters here](https://docs.trunk.io/check/supported-linters).

</details>

<details>

<summary>Why aren't issues showing up anymore?</summary>

If you aren’t seeing any issues the likely cause is that your local repo is clean. By default Trunk Check only processes new changes to your codebase (read about [hold-the-line](https://docs.trunk.io/check/under-the-hood)). To scan older changes try running:

```sh
trunk check --samples=5 
```

to look at a sampling of each linter's issues for 5 random files

```sh
trunk check --all
```

to scan all files, whether they've changed or not. [More on CLI options](https://docs.trunk.io/check/command-line).

</details>

<details>

<summary>There are too many issues showing up</summary>

One reason for seeing too many issues is that you may have multiple linters configured which are all printing output. Try running just one linter at a time with the `--filter=some_linter` option.

Another reason may be that linters are running on files they should skip, such as generated code from other tools. [These docs explain how to configure linters to ignore certain files.](https://docs.trunk.io/check/configuration#ignoring-files)

Linters are usually configured to be very aggressive and flag many potential bugs and security risks. Sometimes you may want to tell a linter “Trust me, I know what I’m doing”. If that is the case you can configure [a linter to ignore certain issues](https://docs.trunk.io/check/ignoring-issues).

A final possible reason for excess issues is that one of your linters is misconfigured. For example, when using ESlint on a TypeScript project it will flag code that is perfectly fine for TypeScript, but incorrect for JavaScript. In this case make sure that your `.eslintrc` file is correctly set up to handle TypeScript. Also make sure the `extends` section lists the `typescript` defaults after the `eslint:recommended` ones, since ESLint uses _last one wins_ priority.

[More on the CLI options](https://docs.trunk.io/check/command-line).

</details>

<details>

<summary>My linters are failing or not running as expected</summary>

When your linters aren’t working the way you expect, first check their configuration. Trunk’s [list of supported linters](https://docs.trunk.io/check/supported-linters#linter-specific-configuration) provides some specific tips for certain linters. You can see the full default configuration of every linter in [Trunk’s public plugin repo](https://github.com/trunk-io/plugins/tree/main).

You can also try running `trunk check --verbose` to see what’s going on under the hood. If that still doesn’t work then please reach out to us on [our community Slack](https://trunkcommunity.slack.com/ssb/redirect) with the output of `trunk check --verbose`.

</details>

<details>

<summary>What is the difference between a Linter and a Formatter?</summary>

A **linter** is a tool that looks for potential code errors such as security vulnerabilities, code spell, anti-patterns, and other things that might be a problem at runtime. _Linters generally report warnings and errors but do not modify code_. A **formatter** is a tool that reformats code to fit a particular style (indentation, sorting imports, semicolons, etc). _Formatters always modify code._ In general, even though your setup may use many different linters we recommend using only _one formatter per filetype_.

Some tools like ESLint can serve as both a linter and formatter for Javascript code. If Prettier is also enabled then code could be reformatted twice, creating conflicts. In this case we recommend using ESLint just for linting and use Prettier for code formatting. [Further advice for ESLint with prettier](https://docs.trunk.io/check/supported-linters#eslint).

Ruff and Black are another example of a linter/formatter pair that can collide with each other if not configured properly. If you enable Ruff but don’t already have a ruff config, Trunk Check will generate a `ruff.toml` file for you automatically. This [ruff.toml](https://github.com/trunk-io/plugins/blob/main/linters/ruff/ruff.toml) is _formatter friendly_, meaning that it will silence formatting related warnings and allow Black to take care of them more quickly and easily. This is another example of tuning your linters with linter configs.

</details>

<details>

<summary>What is Hold-the-line (HTL)?</summary>

**Hold The Line** (HTL) is the principle that Trunk Check will _only run on new changes_ in your codebase, rather than every file in the whole repo. This allows you to use Check to improve your codebase **incrementally** rather than having to address all of the issues at once. HTL also runs checks much faster than scanning the entire codebase would.

HTL works even within files! Check only processes changed lines in a file, not the entire file. More [on how Hold the Line works](https://docs.trunk.io/check/under-the-hood).

If you specifically want to work on older files you can do that by running `trunk check` directly on that file

```
trunk check foo.file
```

or

```
trunk check --all
```

to run on all files. [More on CLI options](https://docs.trunk.io/check/command-line#options).

</details>

<details>

<summary>What does it mean when Trunk Check wants to format an image in my repo?</summary>

Sometimes Trunk Check says there is some `Incorrect formatting` in your images. Check usually enables a program called [Oxipng](https://github.com/shssoichiro/oxipng) which can _optimize_ images to make them smaller (without losing any data). The error message just means that Oxipng wants to optimize those images. You can do that with `trunk fmt` or `trunk fmt filename.png`. You can also disable Oxipng with `trunk check disable oxipng`.

</details>

<details>

<summary>Why does Trunk take up so much disk space</summary>

Trunk Check uses hermetically versioned tools, which means it downloads a separate copy of the tools and runtime for each tool version. Over time, as tools are upgraded, this can leave a lot of unnecessary files in the cache directory. Trunk is working on a way to automatically remove unneeded files from the cache. In the meantime you can safely clear your cache with

```
trunk cache clean --all
```

then run `trunk install` again in your repos.

</details>

<details>

<summary>How to transition to running more linters with Trunk</summary>

Trunk supports over 90 different linters, and we are always adding more! Some linters are easier to configure than others, and we enable many of them out-of-the-box. You can read more about specific linter setup [here](https://docs.trunk.io/check/supported-linters). Trunk is intended to be the one-stop-shop for running all of your linters.

To see a list of currently available linters run

```
trunk check list
```

</details>

<details>

<summary>Upgrading Trunk</summary>

Trunk automatically keeps your tools up to date. To check for recent updates you can run `trunk upgrade` to get the latest tools and fixes. You can read more about how this works [here](https://docs.trunk.io/cli/upgrade).

When upgrading from Trunk CLI versions 1.14.2 or older, you will have to rerun `trunk upgrade`in order to get all available fixes.

</details>

<details>

<summary>Runtime &#x26; Download Versioning</summary>

Some of the tools that Trunk installs use direct downloads and others use runtime installs. For example, most Javascript tools run using the NodeJS runtime. Runtimes themselves are provided through Trunk as versioned direct downloads.

You can use a different version of a runtime by changing its version in the enabled section of your `.trunk/trunk.yaml` file in the `runtimes` section.

```
runtimes:
  enabled:
    - node@18.12.1
    - python@3.10.8
```

If you want to pin the version of a runtime that a particular tool uses, you can do that with an `!` after the version number in your `trunk.yaml`.

```
lint:
  enabled:
    - pylint@2.17.5!
```

[More on pinning versions](https://docs.trunk.io/cli/upgrade#pinning-versions)

However, some versions are not supported in Trunk check by default. If you need to specify an unsupported version, for example to use a particular python version that has been deprecated, you would need to override the `downloads` section as necessary. Check out the definition for [python downloads here](https://github.com/trunk-io/plugins/blob/main/runtimes/python/plugin.yaml). In general we advise against using unsupported runtimes.

[More on how runtimes work](https://docs.trunk.io/runtimes)

</details>

<details>

<summary>How do I Make a Linter Work with a Different Filetype?</summary>

Every linter defines a set of file types that it wants to work with in a section of the YAML called `files`. To change this you need to override the files section of that linter’s definition. [More linter application file types](https://docs.trunk.io/check/custom-linters#applicable-filetypes).

Suppose you are using the **foo-linter** which normally runs on `foo` files. The config might look like this:

```yaml
lint:
  files:
    - name: foo
      extensions: [foo]
  definitions:
    - name: foo-linter
      files: [foo]
      commands:
        - name: lint
          output: pass_fail
          run: echo “foo”
          success_codes: [0, 1]
```

To add support for `bar` files add this to your `trunk.yaml` file. The first part defines the `bar` file type, and the second says that `foo-linter` uses both `foo` and `bar` files.

```yaml
lint:
  files:
    - name: bar
      extensions: [bar]
...
      
  definitions:
    - name: foo-linter
        files:
          - foo
          - bar
```

</details>
