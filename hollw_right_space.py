n = 5
for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# my_num = 1
# for i in range(1,65):
#     print(my_num)
#
#     my_num *= 2





