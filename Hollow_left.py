n = int(input("Enter your number: "))
for i in range(n):
    for j in range(n-i-1):
        print("_",end=" ")

    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()



