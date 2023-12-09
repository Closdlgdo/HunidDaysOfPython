# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas as pd

data = pd.read_csv("weather_data.csv")
data_dict = data.to_dict()

temp_list = data["temp"].to_list()
# # let's find the average temperature
# print(sum(temp_list) / len(temp_list))
#
# # This too will find the average temperature using a standard panda method
# print(data["temp"].mean())
#
# # This will find the max temperature
# print(data["temp"].max())

# # Get data in columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday.condition)

# Let's find the temp for monday and convert it to fahrenheit
monday_temp = int(monday.temp)
monday_temp_fahrenheit = monday_temp * 1.8 + 32
print(monday_temp_fahrenheit)
