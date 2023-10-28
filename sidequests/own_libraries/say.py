import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

# This gets printed out when we run "python3 say.py Carlos":
# Hello world!
# Goodbye world!
# Hello Carlos!

# now when the program is ran with the same command to the terminal, this prints out:
# Hello Carlos!
# Why? Because it is going to ignore the call to main() because it is wrapped in that conditional statement.
# To use the other function created in sayings.py, we need to import that function. from sayings import goodbye
