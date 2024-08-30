# Python Assignment: Summer Class -- Lesson 09

### Instructions:
1. Write comments to explain your code.
2. Use loops effectively to solve the problems.
3. Ensure your code is well-organized and easy to understand.

### Assignment:

1. **While Loop:**
   - Write a `while` loop that prints the numbers from 1 to 15.
   - Add a condition inside the loop to skip the number 10 using the `continue` statement.
   - When the loop reaches the number 15, use the `break` statement to exit the loop.
   - Print `"Loop ended"` after the loop exits.

2. **For Loop with Lists:**
   - Create a list called `colors` with the following items: `"Red"`, `"Green"`, `"Blue"`, `"Yellow"`, `"Purple"`.
   - Write a `for` loop to print each color in the list.
   - Inside the loop, use an `if` statement to skip the color `"Blue"` and continue to the next iteration.
   - Print `"Finished printing colors"` after the loop ends.

3. **For Loop with Strings:**
   - Write a `for` loop that iterates over the string `"Python"` and prints each character on a new line.
   - After the loop, print `"End of string"`.

4. **For Loop with Range:**
   - Use a `for` loop with the `range()` function to print the numbers from 10 to 50 (inclusive) in steps of 10.
   - Print `"Range loop completed"` after the loop ends.

5. **Nested Loops:**
   - Create two lists: `fruits = ["Apple", "Banana", "Cherry"]` and `colors = ["Red", "Yellow", "Green"]`.
   - Use nested `for` loops to print each combination of fruit and color, in the format `"Fruit - Color"`.
   - If the fruit is `"Banana"` and the color is `"Yellow"`, print `"Banana is yellow!"` and use `break` to exit the inner loop.

### Example Code Snippet:

```python
# While Loop
x = 1
while x <= 15:
    if x == 10:
        x += 1
        continue
    print(x)
    x += 1
    if x > 15:
        break
print("Loop ended")

# For Loop with Lists
colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
for color in colors:
    if color == "Blue":
        continue
    print(color)
print("Finished printing colors")

# For Loop with Strings
for char in "Python":
    print(char)
print("End of string")

# For Loop with Range
for num in range(10, 51, 10):
    print(num)
print("Range loop completed")

# Nested Loops
fruits = ["Apple", "Banana", "Cherry"]
colors = ["Red", "Yellow", "Green"]
for fruit in fruits:
    for color in colors:
        print(f"{fruit} - {color}")
        if fruit == "Banana" and color == "Yellow":
            print("Banana is yellow!")
            break
