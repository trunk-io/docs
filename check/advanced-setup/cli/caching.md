# Caching

Trunk hermetically manages all the tools that it runs. To do this, it will download and install them into its cache folder only when needed. On Linux and macOS you may find the cache folder at `$HOME/.cache/trunk`.

### Viewing your repo's cache

If you need to debug your repo's cache, you can find its location by running the cache command.

```
trunk cache
```

### Cleaning cache

Trunk will automatically clean up downloads that have not been used in a while, such as old versions of tools and linters.

If you want to manually prune files in your cache directory that are no longer needed, you can run this command:

```
trunk cache prune
```

If you need to clean your entire cache manually, you can use the command:

```sh
trunk cache clean --all
```

Remember to rerun the install command to reinstall the necessary tools and linters.

```
trunk install
```
