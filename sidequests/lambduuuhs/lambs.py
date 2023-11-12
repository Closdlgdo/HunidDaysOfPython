# Lambda Expression: Think of a lambda expression as a quick, throwaway function. It's a way to define a function without
# formally using the def keyword. It's like a mini-function that you create on the fly for a specific purpose.
# Syntax: The syntax of a lambda expression is lambda arguments: expression. In the provided code, lambda x: x["name"]
# is a lambda expression that takes an argument x and returns x["name"].
# Anonymous Function: The term "anonymous" means that the function doesn't have a formal name like functions defined with
# def. In this case, it's used right where it's needed without assigning it a name.
# Use Case: lambda is often used for short, simple operations, like in this example where it's used to specify the
# sorting key. Instead of defining a separate function using def, a lambda expression is used for brevity.

# These two functions are the same:

def sq_this(x):  # this function has a name.
    return x * x


lambda x: x * x  # this function does not have a name.


# This is how it looks without an argument

def get_hundo():
    return 10 * 10


lambda: 10 * 10

######################################################################################

# This is how we would call a lambda function:

(lambda x: x * x)(10)
(lambda: 10 * 10)()


######################################################################################
def add(x, y):
    return x + y


print(add(1, 2))

print((lambda x, y: x + y)(1, 2))
