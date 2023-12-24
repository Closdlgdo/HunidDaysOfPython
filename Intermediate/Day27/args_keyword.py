# *args - A list of non-keyword arguments to pass to a function. This is a tuple.
# Limited arguments.
# def add(n1, n2):
#     return n1 + n2
# add(n1=5, n2=3)
# This only allows you to pass two arguments.

# Unlimited arguments.
# You dont have to use the word args but you do need the asterisk.
# def add(*args):
#     for n in args:
#         print(n)
#
#
# add(1, 2, 3, 4, 5)

def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 3, 4, 234, 23, 55, 7))
