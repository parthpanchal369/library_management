n = 5
for i in range(n,0,-1):
    for j in range(i-1,0,-1):
        print(" ", end=" ")

    for j in range(i,n+1):
        print(j,end=" ")
    print()