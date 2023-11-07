# We will be learning about list comprehensions in python.
# What is a list comprehension? List comprehension in Python is a way to create a new list from an existing one, but
# with some modifications. It’s like a shortcut for creating lists.
list1 = [1, 2, 3, 4, 5]

print([i for i in list1])

# filtering to make sure all numbers are positive numbers. Any integer 3 we will multiply by 5 so that its 15.
print([i * 5 if i == 3 else i for i in list1])

# The Operation is left of the for loop. The if else statement is typically to the left of the for loop.
print([i for i in list1 if i > 2])

print([i * 5 for i in list1 if i == 3])  # the if statement to the right of the for loop takes on a different behaviour
# than that of the if statement to the left of the for loop.

print([i * 3 if i == 3 else i for i in list1 if i > 1])
# the if statement to the right of the for loop is basically a filter for the for loop
# (the else statement is not allowed there).
# Once the for loop goes through the if statement to the right of it, then the if-else statement to the left of the for
# loop proceeds to compute.
