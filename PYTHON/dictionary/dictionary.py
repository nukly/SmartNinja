box = {"height": 20, "width": 45, "length": 30}

# print(box["height"] or


print(box.get("height"))

# add item to dictionary

box["weight"] = 1
print(box.keys())
print(box.values())
print(box.get("width"))
print(box)

# remove item from dictionary
box.pop("height")
print(box)

# list in dictionary and dictionary in list

some_dict = {"cars": ["bmw", "vw", "tesla"], "city": "Vienna"}

some_list = [25, "Ninja", {"city": "Vienna"}]


# If you want to group data of the same kind, you'd use a list. Example: a list of European cities:

eu_cities = ["Vienna", "Malaga", "Budapest", "Cologne", "Zagreb"]

# But if you'd like to group data of different kinds, you'd use a dictionary:

jordan = {"first_name": "Michael", "last_name": "Jordan", "age": 56, "games_played": 1072, "total_points": 32292}