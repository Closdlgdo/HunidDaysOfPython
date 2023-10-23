country = input()
visits = int(input())
list_of_cities = eval(input())

travel_log = [
    {
        "country": "France",
        "visits": 1,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 2,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# We create a function that will add a new country to the list of countries.
def add_new_country(country, visits, cities):
    """This function adds a new country to the travel log"""
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times")
print(f"My favorite city was {travel_log[2]['cities'][1]}")
