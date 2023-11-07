# a for loop is used to iterate over a list of objects.

# for obj in [0, 1, 2]:
#     print("Carlos")

# list comprehension version of the above code
[print("Carlos") for i in [0, 1, 2, ]]


# to make the top code usable with higher values, we need to add a new function called "range"
# this function allows us to give a starting point and a stop point.
# for obj in range(3):
#     print("delgado")

# list comprehension version of the above code
[print("delgado") for a in range(3)]

# another way to print this in the simplest way is:
# print("Churro\n" * 3, end="")

# list comprehension version of the above code
[print("Churro") for c in range(3)]
