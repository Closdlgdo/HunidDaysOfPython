# we will be creating our own custom classes.
# class ClassName: Also, the class name should be written in Pascal case.
# Pascal case is: CarlosDelgado, HelloWorld, MyNewClass.

class User:
    def __init__(self, user_id, username):
        # This is where we initialize or create the starting values of the attributes.
        # The init function wil be called when we create a new object from this class.
        self.id = user_id
        self.username = username
        self.followers = 0  # These two are called default attributes.
        self.following = 0

    def follow(self, user):  # When a user decides to follow another user.
        user.followers += 1  # Their follower account goes up by one.
        self.following += 1  # Our following account goes up by one.


user_1 = User("001", "Carlos")  # user_1 is an object of the User class
# user_1.id = "001"  # this is an attribute of the user_1 object
# user_1.username = "Carlos"  # this is an attribute of the user_1 object
user_2 = User("002", "Theano")

user_1.follow(user_2)  # user_1(object) will follow(method) user_2
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Theano"
# print(user_2.username)


# An attribute is a variable that can be associated with an object almost as if
# we created a new variable, except we attach it to an object.
# A constructor/initializer is a special method that is called when we create a new object.
# To set (variables, counters, switches, etc.) to their starting values at the beginning of a program
# or subprogram.

# The way to create the constructor is:
# def __init__(self): this is used to initialize the attributes.
# The way to create an attribute is:
# def __init__(self, parameter):
#     self.parameter = parameter
