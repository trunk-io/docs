# GitHub Codespaces

We provide support for `trunk` in GitHub Codespaces.

[Github Codespaces](https://github.com/features/codespaces) are fully configured virtual containers for developing your GitHub repositories.

## Installing the Trunk Feature

You can install the trunk launcher in your codespace by including the following line in your `devcontainer.json` file under `features`:

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

From the [GitHub documentation](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds):

> You can use the onCreateCommand and updateContentCommand commands in your devcontainer.json to include time-consuming processes as part of the prebuild creation. For more information, see the Visual Studio Code documentation, "devcontainer.json reference."
>
> onCreateCommand is run only once, when the prebuild is created, whereas updateContentCommand is run at > creation of the prebuild and at subsequent updates to it. Incremental builds should be included in updateContentCommand since they represent the source of your project and need to be included for every prebuild update.

Note: You should only add `trunk install` if you have a trunk-configured repository.

You can then [configure pre-builds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/configuring-prebuilds) to run from GitHub workflows, ensuring the trunk CLI and needed linters are available and ready to go when you need to boot up your codespace.

## Installing the Trunk Extension

If you are using the trunk feature, we will automatically install the trunk extension on your behalf. Note: We highly recommend turning off auto-save in your VSCode settings in your codespace (or to a longer timeout). Saving files triggers the extension to re-lint, which can quickly overload the extension for anything but the fastest linters. The auto-save setting is detailed [here](https://code.visualstudio.com/docs/editor/codebasics#\_save-auto-save).

Otherwise, You can add `trunk` to your list of extensions in `devcontainer.json` -

```json
    "customizations": {
      "vscode": {
        "extensions": [..., "trunk.io"]
      }
    },
```

Then you're all set to use `trunk` in your Codespace!
