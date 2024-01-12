n = int(input("Enter your number for printing stars: "))
k = n-1
for i in range(0, n):
    for j in range(0,k):
        print(end="_")
    k = k - 1
    for j in range(0,i+1):
        print("*", end=" ")

    print()










