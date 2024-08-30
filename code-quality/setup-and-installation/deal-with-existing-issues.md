# Deal with Existing Issues

After initializing Trunk, you can begin to scan for issues in your repo. You can decide to fix them up front, fix them incrementally as you code, or ignore irrelevant suggestions. This page walks through the process of fixing existing issues.

If you **only want to prevent new issues** from new code changes, skip to [prevent-new-issues.md](prevent-new-issues.md "mention").

### Check for Existing Issues

After initializing Trunk Code Quality, you can run linters and formatters to look for existing issues. You can run Trunk on **all files** in your repo with this command. This will output all issues detected by every linter enabled in your project.

```bash
trunk check --all
```

{% hint style="info" %}
#### Trunk is Git aware

When you run `trunk check` without specifying `--all`, it will **only run on files you've modified according to git**. Remember to [specify a base branch](initialize-trunk.md#initializing-trunk) if you're using something other than `main` or `master`.
{% endhint %}

### Fixing Existing Issues

There are different approaches to dealing with existing issues, such as running `format` and applying automatic fixes, ignoring irrelevant issues, and sampling linters/files. This section walks you through the process to make fixing issues easier.

{% hint style="info" %}
#### Hold-the-line

You don't need to fix all issues upfront. Trunk lets you fix linter errors incrementally with hold-the-line.

Lean more about [#hold-the-line-1](deal-with-existing-issues.md#hold-the-line-1 "mention")
{% endhint %}

#### Running Formatters and Applying Fixes

Some issues can be fixed automatically. You can apply fixes by running the following command.

```bash
trunk check --all --fix
```

#### Overwhelmed by Existing Issues?

You can also focus on the issues revealed by 1 linter at a time.

```bash
trunk check --all --filter=<linter>
```

If that still produces too many issues, you can sample your files, such as 1/5 files.

```bash
trunk check --all --filter=<linter> --sample=5
```

You can drill down further and run only one single file.

```bash
trunk check --all --filter=<linter> --sample=5 <dir/filename>
```

If you're still overwhelmed by the results, you can fix them incrementally as you change files. See the [hold-the-line](deal-with-existing-issues.md#hold-the-line) section.

#### Disabling Linters

Some recommended linters could be unnecessary for your project. You can disable and enable linters with these commands:

```bash
trunk check enable <linter>
trunk check disable <linter>
```

#### Ignore Issues

If there are warnings that don't apply to your project, you can ignore them by line, by file, and ignore a class of warnings in each linter's config files.

To tell Trunk Code Quality to ignore a line in your source code with a special comment like this:

```cpp
struct FooBar {
  // trunk-ignore(clang-tidy)
  void *ptr = NULL;
};
```

The comment should contain the name of the linter you want to ignore the following line, in this case `clang-tidy` For more complex ignore commands, see [Ignoring Issues](../linters/ignoring-issues-and-files.md).

Sometimes you may want to ignore entire files or groups of files, such as generated code. To ignore them, use the `ignore` key to your `.trunk/trunk.yaml` file:

```yaml
lint:
  ignore:
    - linters: [ALL]
      paths:
        # Ignore generated files
        - src/generated/**
```

You can also ignore an entire class of warnings, you can do this in the config file of your linter, either at the project root or in `.trunk/configs`

For example, these are the ignores for Markdownlint in `.trunk/configs/.markdownlint.yaml`:

```yaml
# Prettier friendly markdownlint config (all formatting rules disabled)
extends: markdownlint/style/prettier
MD024: false
MD033: false
MD034: false
```

### Hold-the-line

You don't need to fix all the issues. Trunk Code Quality has the ability to _**Hold The Line**_, which means it only lints your git diffs; only what you changed on your branch gets linted. The pre-existing issues can be managed later.

This allows you to clean up as you go, preventing new issues and letting your team leave each file with better code quality than before.

When you've fixed the existing issues you want to fix, you can skip to [prevent-new-issues.md](prevent-new-issues.md "mention") directly.

