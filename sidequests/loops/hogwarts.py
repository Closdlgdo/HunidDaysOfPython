# this is a list of length 3.
students = ["Harry", "Ron", "Hermione"]

# print(students[0])  # we are indexing inside the list to pick a certain item.
#
# # if you don't know what is in the list, you can do a for loop to iterate over the list.
#
# for student in students:  # call your variables
#     print(student)

# we can iterate over a list of objects using numbers. If I know the size of the list then we can use this code:

for i in range(len(students)):
    print(students[i])  # you can also use a variable inside the brackets.
    print(i + 1, students[i])  # taking two arguments through print. The +1 prints our names with numbers next to them
    # staring at 1 instead of 0.
