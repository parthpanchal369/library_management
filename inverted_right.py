n = int(input("Enter the number for pattern: "))

for i in range(n):
    for j in range(i,n):
        print("*", end=" ")

    print()