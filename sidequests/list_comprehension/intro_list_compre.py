# We will be learning about list comprehensions in python.
# What is a list comprehension? List comprehension in Python is a way to create a new list from an existing one, but
# with some modifications. It’s like a shortcut for creating lists.
nums = [1, 2, 3, 4, 5]
strings = ["a", "b", "c", "d", "e", "f"]

# result = [] # This is a traditional python for-loop
# for i in nums:
#     i *= 2
#     print("i: ", i)  # this will show us how the loop iterates through our list.
#     result.append(i)

# var = [i * 2 for i in nums] # Using a list comprehension allows us to shorten this for-loop into a single line.
#
# print(var)

# results = []
# for i in strings:
#     i = i.upper()  # Here we are iterating over our list and changing each element to uppercase.
#     results.append(i)
# results = [i.upper() for i in strings]
#
# print(results)
#
# # A key feature to list comprehensions is that they return lists.
# # We can also add conditional statements to our list comprehensions.
iterating = [i * 2 for i in [1, 2, 3, 4]]
print(iterating)
