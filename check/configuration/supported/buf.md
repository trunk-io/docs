---
description: buf is a linter for Protobuf
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# buf

**buf** is a linter for Protobuf.

You can enable the buf plugin with

```shell
trunk check enable buf
```

## Settings


buf uses the same config files as the
upstream [buf](https://github.com/bufbuild/buf#readme) project, so you can continue to use any
existing configuration files (ex: `buf.yaml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/buf) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
