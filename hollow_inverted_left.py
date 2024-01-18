n = int(input("Enter your number:"))
for i in range(n):
    for j in range(i):
        print(" ", end=" ")

    for j in range(n - i):
        if j == 0 or j == n - i - 1 or i == 0 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

#