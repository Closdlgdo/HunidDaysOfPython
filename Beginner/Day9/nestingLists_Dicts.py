# We can nest multiple lists inside a single dictionary.
# { key:[list], key2:{Dict}, }, this gives us more flexibility when we are trying to store more complex piece of data.
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# Nesting lists and dictionaries inside a Dictionary with Key:Value pair.

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 1},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 2},
    "Spain": {"cities_visited": ["Madrid", "Barcelona", "Seville"], "total_visits": 2},
}

print(capitals)
print(travel_log)

# We can nest dictionaries and lists inside lists.

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 1,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 2,
    },
    {
        "country": "Spain",
        "cities_visited": ["Madrid", "Barcelona", "Seville"],
        "total_visits": 2,
    },
]
