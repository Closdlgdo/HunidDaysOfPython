# we will implement a program that asks the user to input what house they are in Harry Potter
name = input("What is your name? ")

# if name == "Harry":
#     print("You are in Gryffindor")
# elif name == "Ron":
#     print("You are in Gryffindor")
# elif name == "Hermione":
#     print("You are in Gryffindor")
# elif name == "Draco":
#     print("You are in Slytherin")
# else:
#     print("Who?")

# let's tighten the code up a bit

# if name == "Harry" or name == "Ron" or name == "Hermione":
#     print("You are in Gryffindor")
# elif name == "Draco":
#     print("You are in Slytherin")
# else:
#     print("Who?")

# let's try and make the code simpler.

# match name:
#     case "Harry":
#         print("You are in Gryffindor")
#     case "Hermione":
#         print("You are in Gryffindor")
#     case "Ron":
#         print("You are in Gryffindor")
#     case "Draco":
#         print("You are in Slytherin")
#     case _:
#         print("Who?")

# and now simplest so far

match name:
    case "Harry" | "Ron" | "Hermione":
        print("You are in Gryffindor")
    case "Draco":
        print("You are in Slytherin")
    case _:
        print("Who?")
