# n = 5
#
# k = n-1
# for i in range(0, n):
#     for j in range(0,k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0,i+1):
#         print("*", end=" ")
#
#     print()
#
# k = 0
#
# for i in range(n, 0, -1):
#     for j in range(0, k):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i):
#         print("*", end=" ")
#
#     print()


n = int(input("Enter your number for printing stars: "))
k = n - 1
for i in range(0, n):
    for j in range(0, k):
        print(end="_")
    k = k - 1
    for j in range(0, i + 1):
        print("*", end=" ")

    print()

k = 0
for i in range(n, 0,-1):
    for j in range(0, k):
        print(end="_")
    k = k + 1
    for j in range(0, i):
        print("*", end=" ")

    print()
