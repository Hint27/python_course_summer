# There are 6 major types of data type in python
# 1. Numeric: Integer - int, Float - float, Complex - complex
# 2. Text: String - str
# 3. Sequence: List - list, Tuple - tuple, Range - range
# 4. Mapping: dictionary - dict
# 5. Set: set - set
# 6. Boolean: bool - bool

# Type function
bootcamp = "Hint"

print(type(bootcamp))

# Integer
x = 23

print(x, type(x))

# float
# DOCString: Are more multi-line comment.
"""
Float are essentially numbers with decimal point
"""
y = 20.34

print(y, type(y))

# Complex
"""
Complex numbers are written with a "j" as the imaginary part
"""

z = 34j

print(type(z))

# String
name = "John"
my_favourite = "I Love Python"

print(type(name))
# concatenation = "adding of text and or variable"
print(my_favourite + ' The type of this is ', type(my_favourite))

essay = """I am Umar.
        I am a Python developer.
        I am 25 years old."""

print(essay)

# String Indexing
name2 = "Williams"

print('\n')
print(name2)
print("This is the first character of the name2 variable " + name2[0])

print("negative indexing start from the back:", name2[-1])

print(name2[1:4])

print(name2[-2])

# String methods
name3 = " Phillip Timothy "

print(len(name3))
print(name3.upper())
print(name3.lower())
print(name3.strip())
print(name3.replace('thy', 'py'))