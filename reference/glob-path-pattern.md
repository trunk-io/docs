# Glob Path Pattern

Path patterns in trunk configuration are always relative to the repo root. Every pattern may contain one or more path segments. Each path segment is separated by a `/`. A single `*` is treated as a segment level wildcard. It will match any substring in the segment (including the empty string) and excluding the directory separator `/`. The `*` wildcard may appear multiple times in a single path segment. A double `**` is even broader; it will match zero or more complete path segments and must appear exclusively in it's own segment (i.e. `**/foo` is legal syntax whereas `foo**/bar` is not).

```none
/hello_world
├── bar
│   ├── hello.cpp
│   ├── h.cpp
│   ├── h.zip
│   ├── zap
│   │    ├── hi.png
├── foo
│   ├── file.txt
```

Some examples:

* `bar` non-recursively matches every file in the directory `bar/`, including `bar/hello.cpp`, `bar/h.cpp`, and `bar/h.zip`, but not `bar/zap/hi.png`
* `foo/bar.txt` matches only a single file named `bar.txt` in the `foo` subdirectory
* `foo/*.txt` matches every file in the foo subdirectory that ends with `.txt`
* `bar/h*.c*` matches every files in the bar subdirectory that starts with an `h` and also contains the substring `.c`, including `bar/hello.cpp` and `bar/h.cpp`, but not `bar/h.zip`
* `bar/**` recursively matches every file in the directory `bar`, including `bar/hello.cp` as well as `bar/zap/hi.png`
