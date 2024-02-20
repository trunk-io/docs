# Lint Config Definition


The full linter definition is comprehensive. Most linters will not use every
configuration property, but they are listed here as reference.


## files

Every linter must define the set of filetypes it applies to in the `lint.files` section.

New filetypes are defined with the name and extensions properties. 
They may also include the comments properties to describe what style of
comments are used in these files.

This is how the C++ source filetype is defined.

```yaml
lint:
  files:
    - name: c++-source
      extensions:
        - C
        - cc
        - cpp
        - cxx
      comments:
        - slashes-block
        - slashes-inline
```

* runtimes
* linters __Is this a duplicate of definitions below?__

## definitions

Individual linters are defined in the `lint.definitions` section. See Linter Definitions


* enabled
* disabled
* ignore
* threshold
* landing_mode
* do_not_recommend_linters __should we exclude this one?__
* compile_commands
* bazel
* downloads
* environments
* triggers
* comment_formats
* exported configs
* shared_configs
* default_max_file_size __should we hide this?__
* extra_compilation_flags
* compile_command_roots
* hold_the_line_mode

# Individual Linter Definitions

`name` is the name of the linter. This property will be used to refer to the linter in other parts of the config, for example, in the list of enabled linters.

`type` is the type of output the linter produces.

`command`

`success_codes` is the list of success codes that indicates linter generated data and should be processed. Some linters return 0 for nothing to lint and 1 when there are issues.

`error_codes` is the list of error codes this linter will return when it hit an internal failure and couldn't generate results.

`direct_configs`
__If you have one of these config files, you're definitely using this linter__


`affects_cache`: the list of files that affect the cache results of this linter

`good_without_config`: boolean, indicates whether this linter is recommended without the user tuning its configuration. Prefer `suggest_if`.

`files` is a list of file types listed in the `lint.files` section that this 
linter applies to.


`include_lfs`: boolean, exclude this filetype if it is tracked using LFS.

`std_in`: boolean, Should the command be fed the file on standard input?

`cache_results` : boolean, indicates whether or not to support caching for this linter.

`disable_upstream` :boolean, indicates whether or not we support comparing against the upstream version of this file.  **should we expose this?**

`symlinks`: a list of symlinks to be created when using sandboxing.


`environment`: a list of runtime variables used when running the linter


`is_recommended`: boolean, indicating whether init should try to enable this linter. Prefer `suggest_if`

`run_linter_from`: indicates whether to set current working directory to WORKSPACE root, or the target files folder when run. Prefer `run_from` at the command level.

`include_scanner_type`: which include scanner to use, if any.

`formatter`: boolean. Indicates whether this is a formatter and should be included in `trunk fmt`


`allow_empty_files`: boolean. Indicates to skip linting empty files for this linter.

`runtime`: RuntimeType, Which runtime, if any, to require to be setup for this linter.

`package`: string, What primary package to install, if using a package manager runtime

`extra_packages`: list of strings, Extra packages to install, versions are optional


`download`: string, download url. You must provide either runtime + packages or download, not both. Using runtimes is preferred.

`issue_url_format`: string, a format string that accepts issue codes for links to issues docs.


`run_from_root_target`: string, Walk up to find this file to detect the run from directory. Prefer `run_from` at the command level.

`bool hold_the_line`, optional boolean, whether hold-the-line will be done for this linter or not.

ReadOutputFrom read_output_from = 35;
// Tell parser where to expect output from for reading (stdout, stderr, tmp file)


// ex. [tflint, --init]
repeated string prepare_command = 36;




























