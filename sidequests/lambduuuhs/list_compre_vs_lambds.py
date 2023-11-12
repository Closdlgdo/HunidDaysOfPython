# A list comprehension is a concise way to create lists in Python. It combines a for loop and an expression, allowing
# you to generate a list by applying an operation to each item in an existing iterable (like a list, tuple, or string).
# For example, we create a traditional for loop:
squares = []
for num in range(5):
    squares.append(num ** 2)
print(squares)

# List comprehension is much more concise:
squares = [num ** 2 for num in range(5)]
print(squares)


##########################################################################

# A lambda function is a small, anonymous function defined using the lambda keyword. It's handy for short operations
# where a full function definition might seem overly formal.

# Using a traditional function
def double(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))

print(doubled_numbers)

# Using a lambda function with map:

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)
