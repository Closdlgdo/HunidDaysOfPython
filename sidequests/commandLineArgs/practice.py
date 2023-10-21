# sys is a module in python. argv is a variable in sys.
# argv is argument vector. It is a list. describing the list of all words that the user typed in the prompt before enter
# was selected.
# This is useful to influence the behavior of your program based of their input.
import sys

# let's be a bit more defensive with the code and give a refined exception.
if len(sys.argv) < 2:
    print("Too few arguments!")
elif len(sys.argv) > 2:
    print("Too many arguments!")
else:
    print(f"Hello, my name is", sys.argv[1])
# this way we don't have to give an exception, we can use the conditionals that could express that.

# This is what I would input into the terminal to run the program:
# python3 practice.py Carlos
# It prints out "Hello, my name is Carlos"
# If we want to type out our full name, we can wrap our name in quotes. This is called a string and seen as one argument.
# python3 practice.py "Carlos Delgado"
# It prints out "Hello, my name is Carlos Delgado"
