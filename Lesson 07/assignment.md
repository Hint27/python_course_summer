# Python Assignment: Summer Class

### Instructions:
1. Write comments to explain your code.
2. Use dictionaries and apply the methods and techniques you have learned.
3. Create and manipulate dictionaries, including nested dictionaries.

### Assignment:

1. **Create a Car Dictionary:**
   - Create a dictionary called `car` with the following key-value pairs:
     - `"brand"`: the name of a car brand
     - `"model"`: the car model
     - `"year"`: the year the car was made
     - `"electric"`: a boolean indicating if the car is electric or not
   - Print the dictionary.

2. **Access and Modify Dictionary Items:**
   - Access and print the value associated with the `"brand"` key.
   - Use the `get()` method to print the value of the `"model"` key.
   - Change the value of the `"year"` key to a more recent year.
   - Add a new key-value pair to the dictionary: `"color"` with your favorite color.

3. **Dictionary Methods:**
   - Create a dictionary called `person` with at least 3 key-value pairs (e.g., `"name"`, `"age"`, `"city"`).
   - Print the keys, values, and items of the dictionary using the appropriate methods.
   - Check if the key `"name"` exists in the `person` dictionary, and print the result.

4. **Updating and Removing Items:**
   - Update the `person` dictionary by adding a new key-value pair: `"hobby"` with your favorite hobby.
   - Use the `pop()` method to remove one of the key-value pairs and store the removed value in a variable.
   - Print the updated dictionary and the value that was removed.

5. **Copying and Clearing Dictionaries:**
   - Make a copy of the `car` dictionary and store it in a new variable `car_copy`.
   - Clear all the items in the original `car` dictionary.
   - Print both the `car` and `car_copy` dictionaries to verify that `car_copy` still holds the original data.

6. **Nested Dictionaries:**
   - Create a nested dictionary called `classroom` that contains at least 3 student dictionaries. Each student dictionary should have keys `"name"`, `"age"`, and `"grade"`.
   - Print the entire `classroom` dictionary.
   - Access and print the `"name"` of the second student in the classroom.
   - Update the `"grade"` of the third student and print the updated student information.

### Correction:

```python
# Create a Car Dictionary
car = {
    "brand": "Tesla",
    "model": "Model S",
    "year": 2020,
    "electric": True
}
print(car)

# Access and Modify Dictionary Items
print(car["brand"])
print(car.get("model"))

car["year"] = 2022
car["color"] = "Red"
print(car)

# Dictionary Methods
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person.keys())
print(person.values())
print(person.items())

print("name" in person)

# Updating and Removing Items
person["hobby"] = "Reading"
removed_value = person.pop("age")
print(person)
print(removed_value)

# Copying and Clearing Dictionaries
car_copy = car.copy()
car.clear()

print(car)
print(car_copy)

# Nested Dictionaries
classroom = {
    "student1": {"name": "John", "age": 12, "grade": "A"},
    "student2": {"name": "Mary", "age": 11, "grade": "B"},
    "student3": {"name": "Eli", "age": 13, "grade": "A-"}
}
print(classroom)
print(classroom["student2"]["name"])

# Update third student's grade
classroom["student3"]["grade"] = "A+"
print(classroom["student3"])
