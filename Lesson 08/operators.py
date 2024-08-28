#Assignment Operation (=)
v1 = True

# Arithmetic Operator
x = 4
y = 82
print(x + y) # add
print(y - x) # subtract
print(8 - x)
print(y / x) # division
print(x * y) # multiplication
print(y // x) # Floor division
print(y % x) # Modulus
print(2 ** 2) # Exponentiation
print(4 ** 6) # 4 * 4 * 4 * 4 * 4 * 4

# Assignment Operators
print("\n" + "Assignment Operators".center(40, '*'))
x = 5
x += 1 # same as x = x + 1
print(x)
x -= 1
print(x)

x *= 2 # same as x = x * 2
print(x)
x /= 2 # same as x = x / 2
print(x)
print(round(x))

# same shorthands also applies to other operators

# Immediate Assignment
print(q := 6)
print(q)

# Comparison Operators
a = 4
b = 6
print(a == b) # True or False
print(a == 4) # True or False

print(a != b) # True or False

print(a > b) # True or False
print(a < b) # True or False

print(a >= b) # True or False
print(a <= b) # True or False

# Logical Operators
print("Logical Operators".center(40, '*'))
print(a == b and b > 5)
print(a == 4 and b > 5)

# or operator
print(a == b or b > 5)

print(not(a == b or b > 5))


# Conditional Statement
print('\n' + 'Conditional Statement'.center(40, '*'))
if a == 4:
    print("a is equals to 4")
print("outside if block")

ebuka_age = 14
israel_age = 12
david_age = 23
emmanuel_age = 10

if emmanuel_age > 11:
    print("Emmanuel is greater than 11 years of age")
elif israel_age < 11:
    print("Israel is greater than 11 years of age")
elif ebuka_age > 11:
    print("Ebuka is greater than 11 years of age")
else:
    print("David is older")

# I/O
name = input("What is your name?")
print("My name is:" + name)

# writing program that will only log you in when the name is umar
if name == "umar":
    print("Welcome to our application!")
elif name == 'emmanuel':
    print("You have limited permission")
else:
    print("You're not welcome!")

# Voting like application
inputted_age = input("What is your age? ")
eligible_age = 12

if int(inputted_age) >= eligible_age:
    print(name)
    print("You are eligible to cast a vote!!")
else:
    print("Please wait till you are " + str(eligible_age))

print("Vote execution has ended")