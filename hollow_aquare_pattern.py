n = int(input("Enter your number for print: "))

for i in range(1,n):
    for j in range(n):
        print("*" if i == 1 or i == n-1 or j ==0 or j == n-1 else " ", end=" ")

    print()