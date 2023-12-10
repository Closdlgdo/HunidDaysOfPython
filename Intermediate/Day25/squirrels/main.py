# Create a CSV that's called squirrel_count that has a small table
# which just contains the fur color, so there's only three fur colors,
# and they are logged under the primary fur color column.
# And it can either basically be gray, cinnamon
# which is red, or black.
# There's only three possible values in that column. Now,
# what you're going to do is you are going to figure out how many gray squirrels
# there are in total,
# how many cinnamon ones and how many black ones based on that primary fur color
# column.

import pandas

data = pandas.read_csv("2018_Squirrel_Data.csv")
gray = data[data["Primary Fur Color"] == "Gray"]
print(len(gray))

cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
print(len(cinnamon))

black = data[data["Primary Fur Color"] == "Black"]
print(len(black))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray), len(cinnamon), len(black)]
}

data = pandas.DataFrame(data_dict)

data.to_csv("squirrel_count.csv", index=False)
