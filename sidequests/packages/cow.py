# A module that is implemented in a folder. A third party library.
# We can use the website pypi.
# cowsay is a package in python that allows us to have a cow to say something on the screen.
# pip is the package installer for Python. It is used to install, upgrade, or remove Python packages from the
# Python Package Index (PyPI), as well as other package indexes.
import sys

import cowsay

if len(sys.argv) == 2:
    cowsay.tux("Hello, " + sys.argv[1])
