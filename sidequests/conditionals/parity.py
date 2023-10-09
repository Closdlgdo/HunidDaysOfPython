# Modulo operator %. The remainder symbol

# is this number even or odd?
# x = int(input("What is x? "))
#
# if x % 2 == 0:
#     print("x is even")
# else:
#     print("x is odd")


# let's improve this by creating a new function
def main():
    x = int(input("What is x? "))
    if is_even(x):  # using a function as my boolean expression
        print("x is even")
    else:
        print("x is odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()


# let us improve the previous code.

def maine():
    x = int(input("What is x? "))
    if is_evene(x):  # using a function as my boolean expression
        print("x is even")
    else:
        print("x is odd")


def is_evene(n):
    # return True if n % 2 == 0 else False
    return n % 2 == 0  # this is the same as above


main()
