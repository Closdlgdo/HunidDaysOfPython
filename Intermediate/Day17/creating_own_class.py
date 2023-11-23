# we will be creating our own custom classes.
# class ClassName: Also, the class name should be written in Pascal case.
# Pascal case is: CarlosDelgado, HelloWorld, MyNewClass.

class User:
    pass


user_1 = User()  # user_1 is an object of the User class
user_1.id = "001"  # this is an attribute of the user_1 object
user_1.username = "Carlos"  # this is an attribute of the user_1 object

print(user_1.username)

# An attribute is a variable that can be associated with an object almost as if
# we created a new variable, except we attach it to an object.
# A constructor/initializer is a special method that is called when we create a new object.
# To set (variables, counters, switches, etc.) to their starting values at the beginning of a program
# or subprogram.

# The way to create the constructor is:
# def __init__(self): this is used to initialize the attributes.
