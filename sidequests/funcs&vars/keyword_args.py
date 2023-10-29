# we want to increment the number by a given value.
def increment(number, by):
    return number + by


# # result = increment(5, 10)  # we can simplify this code by removing the variable.
# print(increment(5, 10))  # this is to print out in the terminal.
# # we replace result with the call to increment function.
# # it first calls the increment function and then returns the result and temporarily store the result in the variable we
# # cannot see. then it passes that variable as an argument to the print function.

################################

# to make the code simpler, we can use *keyword arguments* in our print function.
print(increment(number=5, by=10))
