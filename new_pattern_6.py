n = int(input("Enter your number: "))
for i in range(n, 0, -1):
    for j in range(n- i + 1):
        print(i, end=" ")

    print()