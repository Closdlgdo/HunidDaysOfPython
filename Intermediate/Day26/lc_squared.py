# We will be writing a list comprehension to create a new list called squared_numbers. This new
# list should contain every number in the list numbers but each number should be squared.
# Example:
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# The result should be [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)
