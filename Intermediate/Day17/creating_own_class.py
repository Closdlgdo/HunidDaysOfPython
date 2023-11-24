# we will be creating our own custom classes.
# class ClassName: Also, the class name should be written in Pascal case.
# Pascal case is: CarlosDelgado, HelloWorld, MyNewClass.

class User:
    def __init__(self):
        # This is where we initialize or create the starting values of the attributes.
        # The init function wil be called when we create a new object from this class.
        print("New User Created!")


user_1 = User()  # user_1 is an object of the User class
user_1.id = "001"  # this is an attribute of the user_1 object
user_1.username = "Carlos"  # this is an attribute of the user_1 object

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Theano"
print(user_2.username)


# An attribute is a variable that can be associated with an object almost as if
# we created a new variable, except we attach it to an object.
# A constructor/initializer is a special method that is called when we create a new object.
# To set (variables, counters, switches, etc.) to their starting values at the beginning of a program
# or subprogram.

# The way to create the constructor is:
# def __init__(self): this is used to initialize the attributes.
