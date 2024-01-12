n = int(input("Enter your number: "))
k = 1

for i in range(1,n):
    for j in range(i):
        print(k,end=" ")
        k = k + 1

    print()


