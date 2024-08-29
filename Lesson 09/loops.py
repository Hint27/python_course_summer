# while loop
# while True:
#     print("Good!")

# x = 1
#
# while x < 10:
#     # if x == 7:
#     #     break
#
#     print(x)
#     x += 1 # remember to increment x, or else the loop will continue forever.

x = 0

while x < 10:
    x += 1

    if x % 2 == 0:
        continue

    print(x)
else:
    print("Those are odd numbers.")


print("\n" + "for loop".center(30, '='))

animals = ["Dog", "Cat", "Lion", "Giraffe", "Donkey"]

print(animals[0])
print(animals[1])
print(animals[2])

for animal in animals:
    if animal == 'Cat':
        break
    print(animal)

# string
for i in "classroom":
    print(i)

# range
for i in range(5, 101, 5):
    print(i)

# making statements with loops.
# Nested Loop
names = ["Ebuka", "David", "Israel", "Emmanuel"]
actions = ["Code", "Eat", "Sleep"]

for name in names:
    for action in actions:
        print(f"{name} {action}")

        if name == "Emmanuel" and action == "Sleep":
            print(f"{name} is a very lazy boy! 😞😞😞")
