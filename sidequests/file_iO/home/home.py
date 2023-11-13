import csv

name = input("Enter your name: ")
home = input("Enter your home street: ")

with open("home.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
