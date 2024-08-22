# Ignoring Issues and Files

## Ignoring parts of a file

Sometimes we want to deliberately tell a linter that, yes, I know what I'm doing, and yes, in any other situation I should _not_ do this, but in this specific case it's fine. Maybe there's a dummy private key you're using for a test stack, or fixing the lint issue will actually make your code less readable: whatever it is, you now need to figure out how to suppress a given lint issue.

Trunk provides a simple, standardized mechanism to do this, saving you from having to look up the linter-specific syntax for doing so:

```cpp
struct FooBar {
  // trunk-ignore(clang-tidy/modernize-use-nullptr): load-bearing NULL, see ISSUE-832
  void *ptr = NULL;
};
```

This tells Trunk that the `clang-tidy` linter found a `modernize-use-nullptr` issue on the highlighted line and that Trunk should suppress this linter issue.

Comments may be omitted:

```cpp
struct FooBar {
  // trunk-ignore(clang-tidy/modernize-use-nullptr)
  void *ptr = NULL;
};
```

You can also omit the name of the check to simply tell Trunk that all issues from a given linter on a specific line should be suppressed:

```cpp
struct FooBar {
  // trunk-ignore(clang-tidy)
  void *ptr = NULL;
};
```

`trunk-ignore` directives can also be placed at the end of the line on which they're suppressing lint issues:

```cpp
struct FooBar {
  void *ptr1 = NULL;  // trunk-ignore(clang-tidy/modernize-use-nullptr)
  void *ptr2 = NULL;  // trunk-ignore(clang-tidy)
};
```

If you need to suppress issues from multiple linters, `trunk-ignore` supports that too:

```cpp
struct FooBar {
  // trunk-ignore(clang-tidy): ISSUE-914 explains why the `void *` type is needed
  // trunk-ignore(gitleaks,my-custom-linter/do-not-hardcode-passwords): see ISSUE-915
  void *super_secret_password = (void *)("915dr~S$Pzqod~oR*CrQ$/SQ@hbtQBked:CL@z!y]");
};
```

`trunk-ignore` directives can also apply to other `trunk-ignore`s if need be:

```ts
// trunk-ignore(eslint/max-line-length)
// trunk-ignore(eslint/@typescript-eslint/no-unsafe-member-access,eslint/@typescript-eslint/no-unsafe-assignment)
const version = parsedConfig.version;
```

### Ignoring all issues/formatting in a file

You can also ignore all issues or formatting in a file:

```cpp
// trunk-ignore-all(clang-tidy)
struct FooBar {
  void *ptr1 = NULL;
  void *ptr2 = NULL;
};
```

{% hint style="info" %}
`trunk-ignore-all` is not required to be the first line of a file, because we recognize that other constructs (shebangs, front matter, docstrings) may need to take precedence.
{% endhint %}

### Ignoring all issues in a code block

Alternatively, you can ignore all matching issues in a code block:

```cpp
struct FooBar {
  // trunk-ignore-begin(clang-tidy)
  void *ptr1 = NULL;
  void *ptr2 = NULL;
  // trunk-ignore-end(clang-tidy)
};
```

### Tracking unused ignores

Trunk will alert you if your `trunk-ignore` directives are unused. This can happen due to user error or even innocuously over time, for example, if your internal APIs change or if a linter's output changes.

```
app/parse.ts:18:3
 18:3  note  trunk-ignore(eslint/@typescript-eslint/no-unsafe-member-access)   trunk/ignore-does-nothing
             is not suppressing a lint issue
```

Hold the Line will continue to only surface ignore issues that you have introduced, and these issues will have a `note` [severity](configure-linters.md#blocking-thresholds), indicating they are non-blocking by default.

If you need to, you can ignore issues from unused `trunk-ignore` directives, using `trunk-ignore(trunk)`:

```
// trunk-ignore(trunk): This error will resurface after our API migration.
// trunk-ignore(eslint/@typescript-eslint/no-unsafe-member-access)
```

### Specification

The syntax of a trunk-ignore directive is as follows:

```
<trunk-ignore>      ::= <trunk-ignore-type> "(" <check-ids> ")" <optional-comment>
<trunk-ignore-type> ::= "trunk-ignore" | "trunk-ignore-begin" | "trunk-ignore-end" | "trunk-ignore-all"
<check-ids>         ::= <check-id> <optional-check-id>
<optional-check-id> ::= "," <check-id>
<check-id>          ::= <linter-id> <optional-rule-id>
<optional-rule-id>  ::= "/" <rule-id>
<optional-comment>  ::= ": " <comment>
```

## Ignoring Multiple Files

Some files are never meant to be checked, such as generated code. To ignore them, use the `ignore` key to your `.trunk/trunk.yaml` file:

```yaml
lint:
  ignore:
    - linters: [ALL]
      paths:
        # Ignore generated files
        - src/generated/**
        # Except for files ending in .foo
        - !src/generated/**/*.foo # Test data
        - test/test_data
```

Every entry in `ignore` defines both a set of linters and a set of paths to ignore.

<table><thead><tr><th width="101">Key</th><th>Value</th></tr></thead><tbody><tr><td>linters</td><td>List of linters (i.e. <code>[black, eslint]</code>) or the special <code>[ALL]</code> tag</td></tr><tr><td>paths</td><td>List of <a href="broken-reference">glob paths</a>, relative to the root of the repo, to ignore. If a path begins with a <code>!</code> then it represents an inverse ignore. This means that any file matching that glob will not be ignored, even if matched by other globs.</td></tr></tbody></table>

{% hint style="info" %}
Trunk is `git`-aware, which means it ignores `gitignore'd` files by default.
{% endhint %}

### Known Issues

`trunk-ignore` does not currently support:

* suppressing findings on lines 0 or 1 using inline/block directives

If you need any of these to be supported, or you have another edge case, please reach out to us on the [Trunk community slack](https://slack.trunk.io).
