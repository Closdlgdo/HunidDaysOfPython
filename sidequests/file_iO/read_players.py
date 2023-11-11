with open("players.csv") as file:
    for line in file:
        players, team = line.rstrip().split(",")
        print(f"{players} plays/ed with {team}")
