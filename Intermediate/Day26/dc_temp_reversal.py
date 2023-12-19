# We are going to create a dictionary called from another dictionary.
weather_c = eval(input())

weather_f = {key: ((9 * value) / 5) + 32 for (key, value) in weather_c.items()}
print(weather_f)
