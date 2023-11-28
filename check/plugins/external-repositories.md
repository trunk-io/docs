# Creating Organization Configs

To standardize Trunk configuration across an organization, you can create and publish a public plugins repository. This repo can define new linter definitions, specify enabled linters and actions, and even [export linter configs](exported-configs.md).

Once you've created your plugin repository, you can source it in other repositories to adopt shared configuration across your organization. For an example of how we do this in our own org, check out our [configs repo](https://github.com/trunk-io/configs).

Note that in order to keep linters and tools up to date in your plugin configs repo, you'll need to run `trunk upgrade --apply-to=plugin.yaml` to apply [upgrades](../cli/upgrade.md#plugin-repos-and-user.yaml). After making a public GitHub release with your plugin changes, other dependent repos will pick up these changes automatically when running `trunk upgrade`.

### Get started

Let's walk through how to create a simple linter that warns about TODOs in your codebase.

We'll start by creating a new Git repository:

```bash
PLUGIN_PATH=~/my-first-trunk-plugin
mkdir "${PLUGIN_PATH}" && cd "${PLUGIN_PATH}"
git init
```

And then create a linter that can find TODOs in your codebase using `grep` and `sed`:

```bash
cat >plugin.yaml <<EOF
version: 0.1
lint:
  definitions:
    - name: todo-finder
      files: [ALL]
      commands:
        - output: parsable
          run: grep --with-filename --line-number --ignore-case todo ${target}
          success_codes: [0, 1]
          read_output_from: stdout
          parser:
            run: "sed -E 's/(.*):([0-9]+):(.*)/\\1:\\2:0: [error] Found todo in \"\\3\" (found-todo)/'"
EOF
```

Now we can turn this linter on in a repository where we have `trunk` set up:

```bash
trunk plugins add my-first-plugin "${PLUGIN_PATH}"
trunk check enable todo-finder
```

And now, to demonstrate how this works, let's `trunk check` some files where we know we have TODOs:

```bash
trunk check $(git grep -li todo | head -n 10)
```

which will show you something like this:

```
.eslintrc.yaml:19:0
  19:0  high  Found todo in "  # TODO(chris): Figure out why this causes a massive slowdown ... .trunk/dev-out/O1F.txt  local.todo-finder/found-todo
 101:0  high  Found todo in "  node/no-unpublished-import: off # TODO: do we want this?"                                local.todo-finder/found-todo
```

### Organizing your code

In the example we gave above, we put the linter's source code in `plugin.yaml`, which is fine for an example, but not really great for anything more than that. We can take the `sed` command from the plugin we created earlier and push that into the shell script:

```bash
#!/bin/bash
sed -E 's/(.*):([0-9]+):(.*)/\1:\2:0: [error] Found todo in \"\3\" (found-todo)/'"
```

> Tip: Remember to run `chmod u+x todo-finder-parser.sh` so that `trunk` can run it!

and also point the definition of `todo-finder` at it:

```bash
version: 0.1
lint:
  definitions:
    - name: todo-finder
      files: [ALL]
      commands:
        - output: parsable
          run: grep --with-filename --line-number --ignore-case todo ${target}
          success_codes: [0, 1]
          read_output_from: stdout
          parser:
            run: ${plugin}/todo-finder-parser.sh
```

We can also go another step and push the entire linter definition into a shell script:

```bash
#!/bin/bash
grep --with-filename --line-number --ignore-case todo "${1}" | \
  sed -E 's/(.*):([0-9]+):(.*)/\1:\2:0: [error] Found todo in \"\3\" (found-todo)/'"
```

```yaml
version: 0.1
lint:
  definitions:
    - name: todo-finder
      files: [ALL]
      commands:
        - output: parsable
          run: ${plugin}/todo-finder.sh
          success_codes: [0]
```

See our documentation on [custom linters](../custom-linters.md) and [custom parsers](../custom-parsers.md) for more on what you can do, such as writing your parser in Javascript or Python!

### Publishing your plugin

To share your plugin with the world, all you have to do is tag a release and push it to GitHub, Gitlab, or some other repository hosting service:

```bash
git add .
git commit "Create a TODO finder"
git tag -a v0.0.0 --message "Initial TODO finder release"
git remote add origin ${repo_url}
git push origin main v0.0.0
```

Now that it's available on the Internet, everyone else can just use your plugin by running:

```bash
trunk plugins add --id=their-first-plugin ${repo_url} v0.0.0
```
