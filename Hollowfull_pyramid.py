n = int(input("Enter your number for printing stars: "))
k = n-1
for i in range(0, n):
    for j in range(0,k):
        print(end=" ")
    k = k - 1
    for j in range(0,i+1):
        print("*" if i == 1 or i == n-1 or j == 0 or j == n-1 or i == j else " ", end=" ")

    print()
