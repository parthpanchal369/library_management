n = int(input("Enter your number for print stars: "))

for i in range(n, 0, -1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()