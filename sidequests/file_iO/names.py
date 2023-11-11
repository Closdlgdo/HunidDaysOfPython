# names = []
#
# for _ in range(3):
#     names.append(input("Please enter your name: "))
#
# for name in sorted(names):
#     print(f"Hello, {name}!")
#
# # Every time we rerun the program, the names do not get saved. They will simply disappear and will
# # be replaced with the new names. If a program required the names to be saved, then this would not work out.

# names = input("Please enter your name: ")
#
# file = open("names.txt", "w")  # we write two arguments in the function. One is the name of the file we want to use,
# # and the other is what we want to do to the file. "w" means write into the file. If the file doesn't exist, it will create
# # a new one.
# file.write(names)
# file.close()
# # Instead of printing out the name that has just been inputted, we will save it to a file by using the open() function.
# # Allows us to read from or write to a file.
# # This certain code will not save all the names when the program is re-run over and over since there is no list to save in,
# # and we are not appending to the file. The "w" writes over the previous contents of the file if not properly appended.

names = input("Please enter your name: ")

with open("names.txt",
          "a") as file:  # When we use the "a" function, we are appending (adding to the list) to the file instead
    # of writing over it.
    file.write(f"{names}\n")  # we then indent this line into the with scope.
# file.close(), to make it more pythonic, we can introduce the "with" statement.

# with open("names.txt", "a") (Call the function in question) as file (specify the name of the variable that should be assigned
# the return value of open)
