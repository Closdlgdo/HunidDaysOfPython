# Global Scope works outside the function.

x = 10


def global_scope():
    for i in range():
        print(x * 2)


print(x)  # this print function is in the global scope because it is not indented within the function.


# Local Scope works within the function.

def global_scope():
    for i in range():
        print(x * 2)  # this print function is in the local scope because it is indented within the function.

# Scopes are also a concept with functions, not only variables.
