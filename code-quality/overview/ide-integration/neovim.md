# Neovim

{% hint style="info" %}
📘 The Trunk Code Quality Neovim Plugin is available for beta!

Try it out by following the instructions below.
{% endhint %}

### Prerequisites

The Neovim Plugin needs the following prerequisites:

| Tool   | Minimum Required Version |
| ------ | ------------------------ |
| CLI    | 1.17.0                   |
| Neovim | v0.9.2                   |

### Get started

Using the [lazy.nvim](https://github.com/folke/lazy.nvim#readme) plugin manager:

```lua
require("lazy").setup({
	{
		"trunk-io/neovim-trunk",
		lazy = false,
		-- optionally pin a version
		tag = "v0.1.3",
		-- these are optional config arguments (defaults shown)
		config = {
			-- trunkPath = "trunk",
			-- lspArgs = {},
			-- formatOnSave = true,
                        -- formatOnSaveTimeout = 10, -- seconds
			-- logLevel = "info"
		},
		main = "trunk",
		dependencies = {"nvim-telescope/telescope.nvim", "nvim-lua/plenary.nvim"}
	}
})
```

For other plugin managers and installation methods, see our [Neovim Plugin repo](https://github.com/trunk-io/neovim-trunk#installation).

### Features

The Neovim Plugin is designed to mirror the [VSCode extension](vscode.md). Supported features include:

* Provide inline diagnostics and auto-fixes
* Format files on save
* Run [Trunk Actions](../getting-started/actions/) notifications
* Display the linters that Trunk runs on a file

### Limitations

The Trunk Code Quality Neovim Plugin is in beta with limited support. If you encounter any issues, feel free to reach out on [Slack](https://slack.trunk.io).

For other notes and configuration, see the [Neovim Plugins repo](https://github.com/trunk-io/neovim-trunk#trunk-check-neovim-plugin).
