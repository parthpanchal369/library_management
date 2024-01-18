n = int(input("Enter Your number: "))
for i in range(n,0,-1):
    for j in range(i-1,0,-1):
        print(" ",end=" ")
    for j in range(n-i+1):
        print(i, end=" ")
    print()


