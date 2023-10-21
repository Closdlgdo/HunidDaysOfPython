# sys is a module in python. argv is a variable in sys.
# argv is argument vector. It is a list. describing the list of all words that the user typed in the prompt before enter
# was selected.
# This is useful to influence the behavior of your program based of their input.
import sys

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments.")
# This is what I would input into the terminal to run the program:
# python3 practice.py Carlos
# It prints out "Hello, my name is Carlos"
