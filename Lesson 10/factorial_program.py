n = int(input("Enter number to compute factorial of: "))

factorial = 1

if n < 0:
    print("No factorial below 0")
elif n == 0:
    print("factorial is: 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
        print(f"factorial of {i} is {factorial}")