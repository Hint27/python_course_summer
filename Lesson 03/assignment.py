# This is a greeting program
name = "  Alex  "  # Name variable with extra spaces
age = 12  # Age variable (number)

# Print greeting message using the variables
print("Hello, my name is " + name.strip() + " and I am " + str(age) + " years old.")  # Using strip to remove extra spaces

# Use string methods to modify the name
print(name.upper())  # Make the name uppercase
print(name.capitalize())  # Capitalize the name

# Use string indexing to get the first and last letter of the name
print("First letter of name:", name.strip()[0])
print("Last letter of name:", name.strip()[-1])

# Favorite food program
favorite_food = " pizza "  # Assign favorite food with extra spaces
print("My favorite food is " + favorite_food.strip() + ".")

# Use string indexing to get the first and last letter of the favorite food
print("First letter of favorite food:", favorite_food.strip()[0])
print("Last letter of favorite food:", favorite_food.strip()[-1])