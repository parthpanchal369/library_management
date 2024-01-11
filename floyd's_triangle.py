n = int(input("Enter number here: "))
k = 1

for i in range(1,n):
    for j in range(i):
        print(k, end=" ")
        k += 1

    print()
