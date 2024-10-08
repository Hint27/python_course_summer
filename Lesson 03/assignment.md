# Python Assignment: Summer Class -- Lesson 03

### Instructions:
1. Add comments to explain your code.
2. Create and use variables for different data types (numbers and strings).
3. Use at least two string methods in your code, including `strip()`.
4. Use string indexing to extract specific characters from a string.

### Assignment:

1. **Create a Greeting Program:**
   - Create a variable called `name` and assign it your name as a string.
   - Create a variable called `age` and assign it your age as a number.
   - Use string concatenation or formatting to print a message that says, `"Hello, my name is [name] and I am [age] years old."`
   - Use at least two string methods (e.g., `.upper()`, `.strip()`, `.capitalize()`).
   - Use string indexing to print the first and last letters of your name.

2. **Favorite Food Program:**
   - Create a variable called `favorite_food` and assign it your favorite food as a string.
   - Print a sentence that says, `"My favorite food is [favorite_food]."`
   - Use the `strip()` method to remove any leading or trailing spaces from your favorite food string, then print the result.
   - Use string indexing to print the first and last letters of the `favorite_food` string.

### Example Code Snippet:

```python
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
