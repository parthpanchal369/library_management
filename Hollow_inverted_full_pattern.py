n = int(input("Enter your number: "))
k = 0

for i in range(n,0,-1):
    for j in range(0,k):
        print("",end=" ")
    k = k + 1
    for j in range(0, i):
        print("*" if i == 0 or i == n or j == 0 or j == n or j == i-1 else " ",  end=" ")

    print()