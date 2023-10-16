# Creating my own function
# STEP 1.
# name = input("What is your name? ")
# hello()
# print(name)

# STEP 2. Create/invent your own function
# def hello():
#     print("Hello!")
#
#
# name = input("What is your name? ")
# hello()
# print(name)

# Hello!
# carlos

# STEP 3. Add a parameter to the new function.
# def hello(to):
#     print("hello", to)  # the second argument to the function "hello"
#
#
# name = input("What is your name? ")
# hello(name)  # we insert the parameter and calling as input the name as argument to the new function. Name is basically
# a copy to the argument "to".

# hello carlos

# STEP 4. Let's use our new function to say hello to no one specific and give a default value.
# def hello(to="world"):
#     print("hello", to)
#
#
# hello()  # here, this will give the default value of "hello world" because it is before line 36.
# name = input("What is your name? ")
# hello(name)
#
# hello world
# What is your name? carlos
# hello carlos

# STEP 5. MAIN FUNCTIONS. This code defines a function called main that asks the user for their name using the
# input function and stores it in a variable called name. Then it calls another function called hello passing
# the name variable as an argument.
# the main code is at the top.
def main():
    name = input("What is your name? ")
    hello(name.title())


# This code defines a function named hello that takes an optional argument to with a default value of "world".
# It prints "hello" followed by the value of to.
def hello(to="world"):
    print(f"Hello {to}")


main()  # you have to call main in order to execute the function. If you don't, you will get an error.
