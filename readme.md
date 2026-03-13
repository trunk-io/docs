# Trunk.io documentation ([docs.trunk.io][docs])

[![docs](https://img.shields.io/badge/-docs-darkgreen?logo=readthedocs&logoColor=ffffff)][docs]
[![slack](https://img.shields.io/badge/-community-611f69?logo=slack)][slack]
[![vscode](https://img.shields.io/visual-studio-marketplace/i/trunk.io?color=0078d7&label=vscode&logo=visualstudiocode)][vscode]

This repository is the official repo for [docs.trunk.io][docs]. If you see any mistakes or any improvements that can be made, we'd love your contributions!

## Local Development

This repo is synced with [GitBook](https://www.gitbook.com/) via Git Sync. Content pushed to `main` is automatically published to [docs.trunk.io][docs]. To preview changes before publishing:

### Setup

1. Push your feature branch to GitHub:
   ```bash
   git push -u origin your-branch-name
   ```
2. In the GitBook editor, create a **Change Request** linked to your branch.
3. GitBook will render your branch content in a preview, separate from the published docs.

### Workflow

```
Edit locally → git push → GitBook auto-syncs branch → Preview in GitBook editor
                                                        ↓
                                              Review & iterate
                                                        ↓
                                              Merge PR on GitHub → publishes to docs.trunk.io
```

- Every push to your branch updates the GitBook preview automatically
- Edits made in the GitBook web editor push commits back to your branch
- Nothing goes live on docs.trunk.io until the branch merges to `main`

## Contributing

If you see any mistakes or any improvements that can be made, we'd love your contributions! Just fork the repo and open a PR with your changes. While you're browsing [docs.trunk.io][docs], you can get to the GitHub source for that page via the `...` menu → `Edit on GitHub`:

![Screenshot 2023-11-29 at 11 37 32 AM](https://github.com/trunk-io/docs/assets/3904462/ce706890-84c3-44c7-9e5f-9bc85aaca99f)

## Feedback, Advice, and Help

Come chat with us in our [Slack Community][slack] ❤️

[slack]: https://slack.trunk.io
[docs]: https://docs.trunk.io
[vscode]: https://marketplace.visualstudio.com/items?itemName=Trunk.io
