n = int(input("enter your number of lines for print: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end=" ")

    for j in range(1,i+1):
        print(j,end=" ")

    print()