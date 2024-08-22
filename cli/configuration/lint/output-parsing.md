# Output Parsing

If you have a command or utility that you want to run pretty much as-is, but Trunk doesn't natively understand how to parse it, you can inject your own custom parser to translate its output into a format that Trunk does understand!

For example, let's say that we want to use `grep` as a linter, but we want to add more context to the matches. We could define a custom linter like so:

```yaml
lint:
  definitions:
    - name: todo-finder
      files: [ALL]
      commands:
        - output: regex
          # matches the parser run output
          parse_regex: "((?P<path>.*):(?P<line>\\d+):(?P<col>\\d+): 
              \\[(?P<severity>.*)\\] (?P<message>.*) \\((?P<code>.*)\\))" 
          run: grep --with-filename --line-number --ignore-case todo ${target}
          success_codes: [0, 1]
          read_output_from: stdout
          parser:
            run:
              "sed -E 's/(.*):([0-9]+):(.*)/\\1:\\2:0: 
                 [error] Found todo in \"\\3\" (found-todo)/'"
```

The execution model that `trunk` follows for a parser is that it will:

* execute the linter's `run` field, asserting that either:
  * the linter's exit code is in `success_codes`, or
  * the linter's exit code is not in `error_codes`;
* execute `parser.run`,
  * with the `read_output_from` of the linter execution fed to `parser.run` as `stdin`,
  * assert that the exit code of the parser is 0, and then
* use `output` to determine how it should parse the parser's `stdout`.

Note that you can also set `parser.runtime` to [`node`](output-parsing.md#node) or [`python`](output-parsing.md#python) so that you can write your parser in Javascript or Python instead, if you so prefer! You can find plenty examples of python parsers in our [plugins repo](https://github.com/trunk-io/plugins).

{% tabs %}
{% tab title="node" %}
#### Node

```yaml
lint:
  definitions:
    - name: todo-finder-node
      files: [ALL]
      commands:
        - output: parsable
          # parse_regex matches the parser run output
          parse_regex: "((?P<path>.*):(?P<line>\\d+):(?P<col>\\d+): 
              \\[(?P<severity>.*)\\] (?P<message>.*) \\((?P<code>.*)\\))" 
          run: grep --with-filename --line-number --ignore-case todo ${target}
          success_codes: [0, 1]
          read_output_from: stdout
          parser:
            runtime: node
            run: ${workspace}/todo-finder-parser.js
```

```javascript
#!/usr/bin/env node
'use strict';
let readline = require('readline');
let rl = readline.createInterface({ input: process.stdin });

rl.on('line', function(line){
  let match = line.match(/(.*):([0-9]+):(.*)/);

  if (match) {
    let [_, path, line_number, line_contents] = match;
    console.log(`${path}:${line_number}:0: [error]`
            +` Found todo in "${line_contents}" (found-todo)`);
  }
```

Remember to run `chmod u+x todo-finder-parser.js` so that `trunk` can run it!
{% endtab %}

{% tab title="python" %}
#### Python

```yaml
lint:
  definitions:
    - name: todo-finder-python
      files: [ALL]
      commands:
        - output: parsable
          # parse_regex matches the parser run output
          parse_regex: "((?P<path>.*):(?P<line>\\d+):(?P<col>\\d+): 
              \\[(?P<severity>.*)\\] (?P<message>.*) \\((?P<code>.*)\\))" 
          run: grep --with-filename --line-number --ignore-case todo ${target}
          success_codes: [0, 1]
          read_output_from: stdout
          parser:
            runtime: python
            run: ${workspace}/todo-finder-parser.js
```

```python
#!/usr/bin/env python
import re, sys

for line in sys.stdin.readlines():
  match = re.match("(.*):([0-9]+):(.*)", line)
  if match:
    path, line_number, line_contents = match.groups()
    print(f"{path}:{line_number}:0: [error] "
           "Found todo in \"{line_contents}\" (found-todo)")

```

Remember to run `chmod u+x todo-finder-parser.py` so that `trunk` can run it!
{% endtab %}
{% endtabs %}
