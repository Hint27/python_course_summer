# how to generate random number
import random

print(int(random.random() * 10) + 1)
# 20 to 30
# formula: random() * (max - min + 1) + min
print(int(random.random() * (30 - 20 + 1)) + 20)
print(int(random.random() * (100 - 50 + 1)) + 50)

# Game
print("\n" + "Game".center(30, '='))
max_num = 30
num_to_guess = int(random.random() * max_num) + 1

your_guess = 0

while your_guess != num_to_guess:
    your_guess = int(input("New Number: "))

    if your_guess > 0:
        if your_guess < num_to_guess:
            print("Too low")
        elif your_guess > num_to_guess:
            print("Too high")
    else:
        print("You're giving up 😢")
        break
else:
    print("You guess right! 🎉")