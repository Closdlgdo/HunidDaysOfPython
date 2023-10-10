# # starting with loops. My dogs are barking
# print("Woof")
# print("Woof")
# print("Woof")
#
# # While loops time. It goes from line 7 to line 8 to line 9. You need to add line 10 to stop the loop.
# i = 0
# while i < 3:
#     print("Woof")
#     i += 1  # i = i + 1
#
# i = 1
# while i <= 3:
#     print("Woof")
#     i += 1  # i = i + 1
#
# a = 3
# while a != 0:
#     print("Woof")
#     a -= 1  # i = i - 1

# if we want to purposely induce an infinite loop, we can use this:
# while True:
#     en = int(input("How old is your pet? "))
#     if en < 0:
#         continue  # this is telling the code to continue the same loop until the user gives a proper input.
#     else:
#         break  # this will break us out of the loop if the input is not less than 0.
#
# # we can also use this without an if, else statement:
# while True:
#     en = int(input("How old is your pet? "))
#     if en > 0:
#         break
# for _ in range(en):
#     print("Woof")
#

# This code defines a function called main which calls two other functions: get_number and woof.
# The get_number function is expected to return a number, and that number is passed as an argument to the woof function.
def main():
    number = get_number()
    woof(number)


# This code defines a function called get_number that repeatedly asks the user for input until they enter a number
# greater than 0. It then returns that number.
def get_number():
    while True:
        en = int(input("What is en? "))
        if en > 0:
            break
    return en


# This code defines a function called woof that takes an argument n. It then prints the word "Woof" n times.
def woof(n):
    for _ in range(n):
        print("Woof")


main()
# Now we have the ability to take user input and print out the quantity they wanted.
