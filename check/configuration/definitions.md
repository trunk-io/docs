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
* definitions
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

