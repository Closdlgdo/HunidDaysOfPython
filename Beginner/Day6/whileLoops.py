# For loops look like this:
# for item in list_of_items:
#    do something to each item.
# for number in range(start, stop): we use every number in the range to do something
#    print(number)

# While loops look like this:
# while condition is true:
#    do something repeatedly.

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
