bucket
======

CLI for auto "bucket"ing files by moving to proper directory filtered by type of file.


Install
=======

```
pip install -U git+https://github.com/nagasuga/bucket.git
```


Usage
=====

Go to a git project and execute `bucket` in terminal

```
$ bucket [-h] [--settings SETTINGS] [-p] [-v] filename [filename ...]

CLI for auto "bucket"ing files by moving to proper directory filtered by type of file.

positional arguments:
  filename             files to be moved to correct buckets

optional arguments:
  -h, --help           show this help message and exit
  --settings SETTINGS  settings file for the bucketing of files in JSON format
  -p                   Create intermediate directories as required. If this option is not specified, the full path prefix of each operand must already exist
  -v                   Verbose mode to print more information
```


TODO
====

* support complex rules like "extension is txt and source dir is ~/Downloads
