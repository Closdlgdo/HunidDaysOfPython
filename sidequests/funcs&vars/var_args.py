# we will create a new function that takes a variable number of arguments.
def multiply(*numbers):  # we replace the two numbers with a single parameter using a plural name and a *.
    # return x * y
    print(numbers)  # this will print the tuple of numbers.
    # a tuple is similar to a list, but it is immutable which means that it cannot be modified.
    # they are like a list in the sense that iterate over them using loops.
    for number in numbers:
        print(number)


multiply(7, 3, 2, 6)
# print(multiply(2, 3, 4, 5))  # this won't work because we have only 2 arguments in the function.
