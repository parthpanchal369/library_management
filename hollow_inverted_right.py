n = int(input("Enter your number: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - i - 1 or i == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
