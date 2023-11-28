import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.png', 30)

# Create a list to store RGB tuples
rgb_tuples = []

# Iterate through the extracted colors and store RGB tuples in the list
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_tuples.append(new_color)

# Print the list of RGB tuples
print(rgb_tuples)

color_list = [(211, 158, 99), (216, 210, 121), (140, 89, 55), (133, 188, 161), (237, 81, 44), (136, 169, 195),
              (214, 133, 155), (70, 96, 123), (148, 214, 203), (69, 106, 97), (152, 160, 68), (240, 163, 185),
              (144, 211, 222), (57, 53, 39), (84, 160, 132), (98, 123, 175), (177, 187, 217), (39, 58, 44),
              (235, 173, 158), (194, 93, 115), (74, 151, 160), (79, 67, 40), (142, 89, 104), (41, 52, 72), (47, 62, 90),
              (43, 77, 64)]
