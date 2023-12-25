# **kwargs are used to override the default parameters of a function. It is used to pass a dictionary of arguments.
# We create unlimited key word arguments.
def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(add=3, multiply=5)
