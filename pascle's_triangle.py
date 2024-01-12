n = int(input("Enter the number for print: "))

for i in range(n):
    k = 1

    for j in range(1, n - i):
        print(" ", end="")

    for j in range(0, i + 1):
        if j > 0:
            k = k * (i - j + 1) // j
        print(k, end=" ")

    print()