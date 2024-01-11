n = int(input("Enter the stars you want to print: "))

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")
    print()



