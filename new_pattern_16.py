# n = 5
# k = 0
#
# for i in range(1,n+1):
#     for j in range(i):
#         print(i ,end=" ")
#     for j in range(n,i):
#         k+=1
#         print(k,end=" ")
#     print()
#
# def print_pattern(rows):
#     num = 1
#
#     for i in range(rows):
#         current_num = num
#         for j in range(i + 1):
#             print(current_num, end=" ")
#             current_num += rows - j
#         print()
#         num += i + 2
#
# # Given number of rows
# num_rows = 5
#
# # Print the pattern
# print_pattern(num_rows)

# def print_pattern(rows):
#     num = 1
#
#     for i in range(rows):
#         current_num = num
#         for j in range(i + 1):
#             if j == 0:
#                 print(current_num, end=" ")
#             else:
#                 print(current_num, end=" ")
#                 current_num += rows - j
#         print()
#         num += 1
#
# # Given number of rows
# num_rows = 5
#
# # Print the pattern
# print_pattern(num_rows)



# def generate_pattern(rows):
#     current_number = 1
#
#     for i in range(1, rows + 1):
#         count = i
#         for j in range(1, i + 1):
#             if j % 2 != 0:
#                 print(current_number, end=" ")
#                 current_number += 1
#             else:
#                 print(current_number + count, end=" ")
#                 current_number += 1
#                 count += 2
#
#         print()
#
# # Adjust the number of rows as needed
# generate_pattern(5)


# n = 5
# k = 1
# for i in range(1,n+1):
#
#     for j in range(i):
#         print(i,end=" ")
#         k+=1
#
#     print()
# def generate_pattern(rows):
#     for i in range(1, rows + 1):
#         current_number = i
#         increment = i - 1
#
#         for j in range(1, i + 1):
#             if j == 1:
#                 print(current_number, end=" ")
#             else:
#                 if i % 2 == 0:
#                     current_number += increment
#                 else:
#                     current_number += 1
#                 increment += 2
#                 print(current_number, end=" ")
#
#         print()
#
#
# generate_pattern(5)
#

# generate_pattern(5)

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#
#             print(5, end=" ")
#         else:
#             print(i, end=" ")
#     print()



# def generate_pattern(rows):
#     for i in range(1, rows + 1):
#         current_number = i
#         increment = i - 1
#
#         for j in range(1, i + 1):
#             print(current_number, end=" ")
#             current_number += increment
#             increment += 2
#
#         print()
#
# # Adjust the number of rows as needed
# generate_pattern(5)


# def generate_pattern(rows):
#     for i in range(1, rows + 1):
#         current_number = i
#         increment = rows - 1
#
#         for j in range(1, i + 1):
#             print(current_number, end=" ")
#             current_number += increment
#             increment -= 1
#
#         print()
#
# # Adjust the number of rows as needed
# generate_pattern(5)



# n = 5
# for i in range(1,n+1):
#     num = i
#     increment = n - 1
#
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num += increment
#         increment -= 1
#
#     print()
# n = 5
# for i in range(1, n + 1):
#     current_number = i
#     increment = n - 1
#
#     for j in range(1, i + 1):
#         print(current_number, end=" ")
#
#         if j < i:
#             current_number += increment
#             increment -= 1
#
#     print()







