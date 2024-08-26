# Python Assignment: Summer Class

### Instructions:
1. Write comments to explain your code.
2. Use lists and apply different list methods you have learned.
3. Mimic resetting a list by clearing and re-adding items.

### Assignment:

1. **Favorite Fruits List:**
   - Create a list called `favorite_fruits` with at least 5 different fruits.
   - Use the following methods on your list:
     - `append()` to add a new fruit to the list.
     - `insert()` to add a fruit at the second position.
     - `remove()` to remove a fruit from the list.
     - `pop()` to remove the last fruit from the list and store it in a variable.
   - Print the final list and the fruit that was removed with `pop()`.

2. **Number List Operations:**
   - Create a list called `numbers` with 5 different numbers.
   - Perform the following operations:
     - Use `sort()` to sort the list in ascending order and print the result.
     - Use `reverse()` to reverse the order of the list and print the result.
     - Use `len()` to print the length of the list.
     - Use `sum()` to calculate the sum of the numbers in the list and print the result.

3. **Mimic List Reset:**
   - Create a list called `reset_list` with 4 random items (they can be numbers, strings, or a mix).
   - Use the `clear()` method to remove all items from the list and print the empty list.
   - Mimic resetting the list by adding new items to it using the `append()` method.
   - Print the "reset" list with the new items.

### Example Code Snippet:

```python
# Favorite Fruits List
favorite_fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]

# Modify the list with different methods
favorite_fruits.append("Pineapple")
favorite_fruits.insert(1, "Strawberry")
favorite_fruits.remove("Orange")
last_fruit = favorite_fruits.pop()

# Print the results
print(f"Updated fruits list: {favorite_fruits}")
print(f"Last fruit removed: {last_fruit}")

# Number List Operations
numbers = [4, 7, 1, 9, 3]

numbers.sort()  # Sort the list
print(f"Sorted numbers: {numbers}")

numbers.reverse()  # Reverse the list
print(f"Reversed numbers: {numbers}")

print(f"Length of the list: {len(numbers)}")
print(f"Sum of the numbers: {sum(numbers)}")

# Mimic List Reset
reset_list = ["Book", 42, "Laptop", 19.99]
print(f"Original list: {reset_list}")

reset_list.clear()  # Clear the list
print(f"List after clear(): {reset_list}")

# Mimic reset by adding new items
reset_list.append("Phone")
reset_list.append("Tablet")
reset_list.append(99)
reset_list.append("Notebook")

print(f"Reset list: {reset_list}")
