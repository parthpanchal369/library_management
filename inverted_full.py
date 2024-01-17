n = int(input("Enter your number for printing stars: "))
k = 0

for i in range(n, 0, -1):
    for j in range(0, k):
        print(end=" ")
    k = k + 1
    for j in range(0, i):
        print("*", end=" ")

    print()








