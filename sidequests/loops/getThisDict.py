# Dict: In Python, a dict refers to a dictionary, which is a built-in data structure used to store a collection of key-value pairs.
# It is also known as an associative array or hash map in other programming languages.
#
# In a dictionary, the keys are unique and immutable (such as strings, numbers, or tuples), and they are used to access
# the corresponding values. The values can be of any data type (e.g., strings, numbers, lists, or even other dictionaries).
#
# Dictionaries are unordered, meaning that the elements are not stored in any particular order. They are mutable, which
# allows for adding, removing, and modifying key-value pairs. Dictionaries are commonly used to represent structured data
# or to efficiently look up values based on their keys.

# students = ["Harry", "Ron", "Hermione", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# the dictionary version of this top lists is:
# keys on the left and values on the right.
students = {
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Hermione": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Draco"])

# loop time. It will only iterate over the keys.
for student in students:
    print(student)  # It will only iterate over the keys.
    print(student, students[student], sep=", ")  # It will call the full list.
