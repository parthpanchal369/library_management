n = int(input("Enter your number: "))
k = 0

for i in range(n,0,-1):
    for j in range(0,k):
        print("",end=" ")
    k = k + 1
    for j in range(0, i):
        print("*" if i == 0 or i == n or j == 0 or j == n or j == i-1 else " ",  end=" ")

    print()


k = n-1
for i in range(1, n):
    for j in range(1,k):
        print(end=" ")
    k = k - 1
    for j in range(0,i+1):
        print("*" if i == 1 or i == n-1 or j == 0 or j == n-1 or i == j else " ", end=" ")

    print()
