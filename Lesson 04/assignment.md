# Python Assignment: Summer Class

### Instructions:
1. Write comments to explain your code.
2. Use variables and apply the string methods and formatting techniques you have learned.
3. Use f-strings to format your output.

### Assignment:

1. **Message Formatting Program:**
   - Create variables `name`, `age`, and `favorite_quote`.
   - The `name` should be left-aligned using `ljust()`, the `age` should be centered using `center()`, and the `favorite_quote` should be right-aligned using `rjust()`. Use a width of at least 20 characters for each field.
   - Print the formatted message using f-strings.
   - Add an escape character (e.g., `\n` or `\t`) to format the output into separate lines or indented sections.
  
2. **Stripping Extra Spaces Program:**
   - Create a variable `message` that has extra spaces on both sides.
   - Use `lstrip()` to remove leading spaces and print the result.
   - Use `rstrip()` to remove trailing spaces and print the result.
   - Finally, use `strip()` to remove all spaces from both sides and print the result.

3. **Centering a Title:**
   - Create a variable `title` and set it to the name of your favorite book, movie, or hobby.
   - Print the title centered within a string of `*` symbols, making the total width 30 characters using the `center()` method.

### Example Code Snippet:

```python
# Message Formatting Program
name = "Alex"
age = 12
favorite_quote = "The sky is the limit."

# Format and align the fields
print(f"Name: {name.ljust(20)} | Age: {str(age).center(20)} | Quote: {favorite_quote.rjust(20)}")

# Add escape characters for better formatting
print(f"\nFormatted Output:\nName:\t{name.ljust(20)}\nAge:\t{str(age).center(20)}\nQuote:\t{favorite_quote.rjust(20)}")

# Stripping Extra Spaces Program
message = "   Hello, Python!   "
print(f"\nOriginal message: '{message}'")
print(f"After lstrip: '{message.lstrip()}'")
print(f"After rstrip: '{message.rstrip()}'")
print(f"After strip: '{message.strip()}'")

# Centering a Title
title = "Python Programming"
print(f"\n{title.center(30, '*')}")