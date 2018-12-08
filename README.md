# ppconfig
Configuration helper

PyPI package: [ppconfig](https://pypi.python.org/pypi/ppconfig)

If you spot any problems or have any improvement ideas then feel free to open
an issue and I will be glad to look into it for you.

## Installation
A recommended way of installing the tool is pip install.

### pip install
The tool is available in PyPI and can be installed using pip:
```
$ pip install --user ppconfig
```

## Configuration
By default, configuration files are searched for in `~/.config/` (this can be overridden by class argument `config_dir` or [environment variable XDG_CONFIG_HOME](https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html)). If the config directory does not exist then it will be automatically created.

## Usage
Let's say we have `~/.config/app_name` with the following contents:
```
[default]
var1 = First Data

[section_name]
var2 = Some other random data
```

To read both variables from this file:
```
from ppconfig import Config

config = Config(config_file='app_name')

var1 = config.get('var1')
var2 = config.get('var2', section='section_name')
```