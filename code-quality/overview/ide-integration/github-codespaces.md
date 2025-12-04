# GitHub Codespaces

We provide support for running `trunk` in GitHub Codespaces.

[Github Codespaces](https://github.com/features/codespaces) are fully configured virtual containers for developing your GitHub repositories.

## Installing the Trunk feature

You can install the Trunk Launcher in your codespace by including the following line in your `devcontainer.json` file under `features`:

```json
    "features": {
      "ghcr.io/trunk-io/devcontainer-feature/trunk": "latest",
    },
```

The feature is defined [here](https://www.github.com/trunk-io/devcontainer-feature).

To have the launcher binary install the CLI tool and associated linters, you can add `trunk install` to `updateContentCommand` in `devcontainer.json`:

```json
"updateContentCommand": "trunk install",
```

Read the [GitHub docs](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds#configuring-time-consuming-tasks-to-be-included-in-the-prebuild) to learn more about `updateContentCommand` .

Note: You should only add `trunk install` if you have a Trunk-configured repository.

You can then [configure pre-builds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds) to run from GitHub workflows, ensuring the `trunk` CLI and needed linters are available and ready to go when you need to boot up your codespace.

## Installing the Trunk extension

If you are using the Trunk feature, we will automatically install the Trunk extension on your behalf.&#x20;

Note: We highly recommend turning off auto-save in your VSCode settings in your codespace (or set autosave to a longer timeout). Saving files triggers the extension to re-lint, which can quickly overload the extension for anything but the fastest linters. The auto-save setting is detailed [here](https://code.visualstudio.com/docs/editor/codebasics#_save-auto-save).

Otherwise, You can add `trunk` to your list of extensions in `devcontainer.json` -

```json
    "customizations": {
      "vscode": {
        "extensions": [..., "trunk.io"]
      }
    },
```

Then you're all set to run `trunk` in your Codespace!
