# Today we are learning about list comprehensions. A list comprehension is a way to create a new list with less syntax.
# Example:
# a_list = [1, 2, 3, 4, 5]
# new_list = []
# Without list comprehensions:
# new_list = []
# for item in a_list:
#     new_list.append(item)
# print(new_list)
# With list comprehensions:
# new_list = [item for item in a_list]
# print(new_list)

# Another example:
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# With list comprehensions:
# new_list = [n + 1 for n in numbers]
# print(new_list)

# Exercise:
name = "Carlos"
new_list = [letter for letter in name]
print(new_list)
