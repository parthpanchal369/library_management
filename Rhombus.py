
n = int(input("Enter your number for print stars: "))

for i in range(n):
    print(" " * i, end="")
    for j in range(n):
        print("*", end=" ")

    print()