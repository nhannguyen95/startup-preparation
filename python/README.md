## Python location

`/usr/bin/python` is the executable for the python that comes with OSX.

`/usr/local/bin/python` is a location for user-installed version of Python (possibly from Homebrew or python.org).

These executables are the symlink to the original installed location somewhere else. To see the original location: `ls -l path_to_python`.

Usually:
- `/usr/bin/python` links to a Python version in `/System/Library/Frameworks/Python.framework`.
- `/usr/local/bin/python` links to a Python verion in `/Library/Frameworks/Python.framework` (python.org?) or `/usr/local/Cellar/python` (Homebrew?).
