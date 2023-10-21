my_dict = {
    "Carlos": "Dock10",
    "Mike": "Dock10",
    "Zack": "Dock11"
}

print(my_dict["Mike"])
# Adding new items to the dictionary
my_dict["Juan"] = "Dock2"
print(my_dict)

# Creating an empty dictionary
empty_dict = {}

# Wipe out the dictionary
# my_dict = {}
# print(my_dict)

# Edit the dictionary
my_dict["Mike"] = "Dock12"
print(my_dict)

# Looping through the dictionary
for key, value in my_dict.items():
    print(key, value)
