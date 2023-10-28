import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

# This gets printed out when we run "python3 say.py Carlos":
# Hello world!
# Goodbye world!
# Hello Carlos!
