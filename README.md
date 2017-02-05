[![Build Status](^https://travis-ci.org/DEV3L/python-files-by-date.png^)](https://travis-ci.org/DEV3L/python-files-by-date)
[![Coverage Status](https://coveralls.io/repos/github/DEV3L/python-files-by-date/badge.svg)](https://coveralls.io/github/DEV3L/python-files-by-date)

# python-files-by-date

A Python program that takes files within an input directory and copies them to an output directory into subdirectories in [YYYYMM] format based upon the file create date.

Continuously deployed to PyPi via Snap-CI. 
[https://pypi.python.org/pypi/files-by-date/](PyPi : files-by-date)


## Installation

pip install files-by-date


## Usage

`usage: files-by-date [-h] [-f FORCE_OVERWRITE] input_dir target_dir

Files-By-Date v1.1: A Python program that takes files within an input
directory and copies them to a target directory, sorted into [YYYYMM] format
subdirectories based upon the file create date.

positional arguments:
  input_dir           input directory
  target_dir          target output directory

optional arguments:
  -h, --help          show this help message and exit
  -f FORCE_OVERWRITE  Force overwrite of files in target directory`


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


## License

MIT
