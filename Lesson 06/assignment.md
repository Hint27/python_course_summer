# Python Assignment: Summer Class -- Lesson 06

### Instructions:
1. Write comments to explain your code.
2. Use tuples and apply the methods and techniques you have learned.
3. Demonstrate your understanding of unpacking tuples and accessing elements.

### Assignment:

1. **Create a Tuple:**
   - Create a tuple called `my_favorites` that contains:
     - Your favorite fruit (as a string)
     - Your age (as a number)
     - A boolean value representing if you like pizza (`True` or `False`)
   - Print the tuple.
   - Use the `tuple()` constructor to create a tuple called `my_numbers` with 3 different numbers.

2. **Access and Slice Tuples:**
   - Access and print the first and last item in `my_favorites`.
   - Slice and print the first two items of `my_favorites`.
   - Slice and print everything except the first item of `my_favorites`.

3. **Check Existence in Tuples:**
   - Check if the fruit you added to `my_favorites` exists in the tuple and print the result.
   - Check if the number 42 exists in `my_numbers` and print the result.

4. **Tuple Methods:**
   - Create a tuple called `my_tuple` with some repeated elements (e.g., `(5, 10, 5, 20, 5)`).
   - Use the `count()` method to count how many times an element appears in `my_tuple` and print the result.
   - Use the `index()` method to find the position of an element in `my_tuple` and print the result.

5. **Unpacking Tuples:**
   - Create a tuple called `food_items` with at least 5 different food items.
   - Unpack the first item into one variable, and unpack the remaining items into another variable.
   - Print both the first item and the remaining items.
   - Also, unpack the first and last items, and store the middle items in a separate variable.

### Example Code Snippet:

```python
# Create a Tuple
my_favorites = ('Apple', 12, True)
print(my_favorites)

my_numbers = tuple((10, 20, 30))
print(my_numbers)

# Access and Slice Tuples
print(my_favorites[0])  # First item
print(my_favorites[-1])  # Last item
print(my_favorites[:2])  # First two items
print(my_favorites[1:])  # Everything except the first item

# Check Existence in Tuples
print('Apple' in my_favorites)
print(42 in my_numbers)

# Tuple Methods
my_tuple = (5, 10, 5, 20, 5)
print(my_tuple.count(5))  # Count occurrences of 5
print(my_tuple.index(10))  # Find the index of 10

# Unpacking Tuples
food_items = ('Pizza', 'Burger', 'Salad', 'Pasta', 'Sushi')

# Unpack first item and the remaining items
(first_food, *remaining_food) = food_items
print(first_food)
print(remaining_food)

# Unpack first, middle, and last items
(first_food, *middle_food, last_food) = food_items
print(first_food)
print(middle_food)
print(last_food)
