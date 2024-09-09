---
title: Configuring minitest
description: minitest is a test runner and testing framework for Ruby
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

# minitest

minitest is a testing framework for Ruby.

### Enabling XML Output

**minitest** can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output by installing the `minitest` Ruby gem. 

```shell
gem install minitest
```
Then require and enable the **minitest** gem in your test code like this:

```ruby
# mixer.rb
require 'minitest/autorun'
require 'minitest/reporters'
Minitest::Reporters.use! Minitest::Reporters::JUnitReporter.new('ruby/minitest/results', write_files: true)

class ColorMixerTest < Minitest::Test
  def test_red_and_blue
    mixer = ColorMixer.new
    assert mixer.mix('red', 'blue') == 'purple'
  end
end
```
Run it with `bundle exec ruby ruby/minitest/mixer.rb` and it will produce output that looks like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<testsuites>
  <testsuite name="ColorMixerTest" filepath="ruby/minitest/mixer.rb" skipped="0" failures="0" errors="0" tests="3" assertions="3" time="1.7999904230237007e-05">
    <testcase name="test_red_and_yellow" 
      lineno="12" 
      classname="ColorMixerTest" 
      assertions="1" 
      time="1.0999967344105244e-05" 
      file="ruby/minitest/mixer.rb">
    </testcase>
  </testsuite>
</testsuites>

```


### Test Suite Naming

The output file can be configured where you require `minitest` and use the `JUnitReporter`. The first argument to the constructor sets the output file.

```ruby
Minitest::Reporters.use! Minitest::Reporters::JUnitReporter
  .new('ruby/minitest/results', write_files: true)
```


## Further Information
See an example of using minitest in a GitHub action [here](https://github.com/trunk-io/flake-factory/blob/main/.github/workflows/ruby-tests.yaml#L35).
