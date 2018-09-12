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

## Usage
```
from ppconfig import Config

config = Config('file_name')

var1 = config.get('var1')
var2 = config.get('var2', section='section_name')
```