n = int(input("Enter your number of lines you wants to print: "))
k = 1
for i in range(1,n*2,2):
    for j in range(i):
        print(k,end=" ")
        k = k + 1

    print()
