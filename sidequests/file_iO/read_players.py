with open("players.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} plays/ed with {row[1]}")
