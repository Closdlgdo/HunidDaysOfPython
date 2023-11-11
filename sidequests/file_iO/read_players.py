player_s = []

with open("players.csv") as file:
    for line in file:
        players, team = line.rstrip().split(",")
        player_s.append(f"{players} plays/ed with {team}")

for player in sorted(player_s):
    print(player)
