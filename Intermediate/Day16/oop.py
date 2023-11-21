# What is Object Oriented Programming?
# Object Oriented Programming (OOP) is a programming paradigm that uses objects and classes in programming.
# The idea is to create real-world entities that have attributes (data) and behaviors (functions).
# An object is an instance of a class. A class can have many objects. A class can have many methods.
# A class can have many attributes. A class is basically a blueprint for an object.
# A method is a function that is defined inside a class.
# An object is an instance of a class.
# An attribute is a property of an object.
from turtle import Turtle, Screen

pedro = Turtle()
print(pedro)
pedro.shape("turtle")
pedro.color("DarkSeaGreen4")
pedro.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
