def increment(number, by=10):  # we can create the by parameter as an option.
    return number + by


print(increment(5, 5))  # we can create the by parameter as an option and when we pass it to the
# print function, it will be used as the default value. If we don't pass a by function in the print function,
# then it will use the default value given in the constructor (by=10).
