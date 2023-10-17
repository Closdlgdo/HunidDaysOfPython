# Functions are a really handy way of taking a complex set of instructions and packaging them together inside a block
# of code that has a name given to it.
#
# def my_function():
#   Do this
#   Then Do that
#   Finally do this
# my_function()

# # Review:
# # Create a function called greet().
# def greet():
#     print("Hello")
#     print("Welcome")
#     print("To Python")
# # Write 3 print statements inside the function.
# # Call the greet() function and run your program.
#
#
# greet()
#
#
# The function with a return is when you put somthing in the parenthesis ().

# def my_function(something):
#   Do this with something
#   Then Do that
#   Finally do this
# my_function(123)  # When you put in a value here (argument), that same value gets put into the top parenthesis (parameter),
# after that, the value goes into the actual code to run.

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Welcome to Python {name}")


greet_with_name("Bambi")
