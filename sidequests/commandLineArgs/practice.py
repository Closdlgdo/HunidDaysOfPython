# sys is a module in python. argv is a variable in sys.
# argv is argument vector. It is a list. describing the list of all words that the user typed in the prompt before enter
# was selected.
# This is useful to influence the behavior of your program based of their input.
import sys

# let's be a bit more defensive with the code and give a refined exception.
if len(sys.argv) < 2:
    sys.exit("Too few arguments!")  # When sys.exit is called, the program is immediately terminated, and any further
    # code that follows it will not be executed. It can be used to forcefully exit the program in specific situations
    # or to handle exceptional cases where you want to stop the execution of the program.
# to not limit how many arguments we can give to the program, we to iterate over every name at the prompt.
for arg in sys.argv[1:]:
    print(f"Hello, my name is", arg)
# a slice is a way to extract a portion of a sequence, such as a string, list, or tuple. It allows you to select a range
# of elements from the sequence based on their indices.
#
# The syntax for a slice is sequence[start:end:step], where start is the index of the starting element, end is the index
# of the ending element (exclusive), and step is the interval between elements.

# This is what I would input into the terminal to run the program:
# python3 practice.py Carlos
# It prints out "Hello, my name is Carlos"
# If we want to type out our full name, we can wrap our name in quotes. This is called a string and seen as one argument.
# python3 practice.py "Carlos Delgado"
# It prints out "Hello, my name is Carlos Delgado"
