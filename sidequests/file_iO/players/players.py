names = input("Enter your favorite player's name, team and number seperated by a comma: ")

with open("players.csv",
          "a") as file:  # When we use the "a" function, we are appending (adding to the list) to the file instead
    # of writing over it.
    file.write(f"{names}\n")  # we then indent this line into the with scope.
