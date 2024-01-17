n = int(input("Enter your number: "))
k = 1

for i in range(1,n+1):
    for j in range(0,i):
        print(k,end=" ")
        k = k + 1

    print()


