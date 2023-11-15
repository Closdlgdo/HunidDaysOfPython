# Modifying Global Scope

enemies = 1


def increase_enemies():  # this function creates a local scope
    enemies = 3
    print(f"enemies inside function: {enemies}")
    # This prints out whatever is within the scope, so the output would be 3.
    # It is bad practice to name your local and global scopes the same.


increase_enemies()
print(f"enemies outside function: {enemies}")
# Ths prints out whatever is outside the scope, so the output would be 1.
