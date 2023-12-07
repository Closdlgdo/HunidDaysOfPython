with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="w") as file:
    file.write("New text.")

with open("new_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="a") as file:
    content = file.read()
    print(content)
# file.close()  # always remember to close the file after using it because it continues to run in the background.
