# The Scope is defined as the area where a variable can be accessed.
message = "Hello"  # global scope variable is defined here.


def greet(name):
    message = "Hello"


print(name)  # print(message)
# NameError: name 'message' is not defined
# this is because the print function is not in the scope of the greet function.
