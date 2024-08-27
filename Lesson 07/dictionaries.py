# Dictionary: Key-Value Pairs, Unordered, mutable, No Duplicate entries.
dictionary = {
    "wheels": 4,
    "doors": 4,
    "car_name": "Mercedes",
    "sound": "Vroom!!!",
    "engine_type": "V8",
    "engine_type": "v12"
}

# mylist = [
#     4, 4, "Mercedes", "Vroom!!!", "V8"
# ]

print(type(dictionary))
print(dictionary)

# Access Item
car_name = dictionary["car_name"]
print(car_name)
print(dictionary.get("sound"))

print(len(dictionary))

# constructor function
dictionary2 = dict(name="Mark", age=23, gender="male")

print(dictionary2)

# Methods
print(dictionary2.keys())
print(dictionary2.values())
print(dictionary2.items())

# Check if key exist
print("name" in dictionary2)

# Change or Update dictionary
dictionary2["name"] = "John"
print(dictionary2)
dictionary3 = {"color": "black", "height": "Tall"}
dictionary2.update(dictionary3)
print(dictionary2)

# Removing of Items
popped = dictionary2.pop("height")
print(popped)
print(dictionary2)

#using del keyword
del dictionary2["color"]
print(dictionary2)

dictionary2.update({"intelligent": True})
print(dictionary2)
poppedItem = dictionary2.popitem()
print(poppedItem)
print(dictionary2)

print(dictionary3)
dictionary3.clear()
print(dictionary3)

# Copy Dictionary
print("Bad Practice")
dictionary4 = dictionary3 # making reference to dictionary3
print(dictionary4)
dictionary3["class"] = "SS1"
print(dictionary3)
print(dictionary4)

#good practice
print("Good Practice")

dicionary4 = dictionary3.copy()
print(dictionary4)
dictionary3.update({"lousy": False})

# using constructor function to make a copy
dictionary5 = dict(dictionary4)
print(dictionary5)

# Nested Dictionary
print("\n\n\n\n")
member1 = {
    "name": "Ebuka",
    "class": "JS2"
}
member2 = {
    "name": "David",
    "class": "Uni"
}
member3 = {
    "name": "Israel",
    "class": "JS1"
}

group = {
    "member1": member1,
    "member2": member2,
    "member3": member3
}

print(group)

# Print the name of the last member in the group
print(group["member2"]["name"])

# Here we stop.