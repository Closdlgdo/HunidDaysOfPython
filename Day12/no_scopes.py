# Global Scope works outside the function.

x = 10


def global_scope():
    for i in range():
        print(x * 2)


print(x)  # this print function is in the global scope because it is not indented within the function.


# Local Scope works within the function.

def global_scope():
    for i in range():
        print(x * 2)  # this print function is in the local scope because it is indented within the function.

# Scopes are also a concept with functions, not only variables.
# There is no such concept of Block scope in Python.
game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]  # if you create a variable within the function then it is only available
    # within that function
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
