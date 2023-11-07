# this is a list of length 3.
# students = ["Harry", "Ron", "Hermione"]
#
# # print(students[0])  # we are indexing inside the list to pick a certain item.
# #
# # # if you don't know what is in the list, you can do a for loop to iterate over the list.
# #
# # for student in students:  # call your variables
# #     print(student)
#
# # we can iterate over a list of objects using numbers. If I know the size of the list then we can use this code:
#
# for i in range(len(students)):
#     print(students[i])  # you can also use a variable inside the brackets.
#     print(i + 1, students[i])  # taking two arguments through print. The +1 prints our names with numbers next to them
#     # staring at 1 instead of 0.

# We can escalate this by getting more information about the students. We have a database with more datasets.
#     | name     | house      | patronus|
#   0 | Hermione | Gryffindor | Otter
#   1 | Harry    | Gryffindor | Stag
#   2 | Ron      | Gryffindor | Jack Russell Terrier
#   3 | Draco    | Slytherin  |
# We want to create a list of dictionaries.
students = [
    {
        "name": "Hermione", "house": "Gryffindor", "patronus": "Otter"
    },
    {
        "name": "Harry", "house": "Gryffindor", "patronus": "Stag"
    },
    {
        "name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"
    },
    {
        "name": "Draco", "house": "Slytherin", "patronus": None  # None represents the absence of a value.
    }

]

# for student in students:  # allows us to iterate over the students in the list.
# print(student["name"])
# print(student["name"], student["house"], sep=", ")
# print(student["name"], student["house"], student["patronus"], sep=", ")

# We can use a list comprehension as well to make our code more readable.
[print(student["name"], student["house"], student["patronus"], sep=", ") for student in students]
