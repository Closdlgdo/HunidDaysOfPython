player_s = []

with open("players.csv") as file:
    for line in file:
        players, team = line.rstrip().split(",")  # This line splits each line of the file into two parts using the
        # split(",") method.
        player = {"name": players, "team": team}  # This creates a dictionary named player with keys "name" and "team"
        # and assigns the values from the previous line.
        player_s.append(player)


def get_team(player):
    return player["team"]


# ^^^^^^^^ This defines a function get_player that takes a player dictionary as an argument and returns the value associated
# with the key "name". This function will be used as the key function for sorting the players.

for player in sorted(player_s, key=get_team):  # This iterates through the sorted player_s list based on the "name"
    # key using the get_player function.
    print(f"{player['name']} plays for the {player['team']}.")

# We do this if we want to sort by the team and not the player.
