# Fibonacci program


# def fibonacci(n):
#     if n < 0:
#         print("Incorrect value")
#
#     elif n == 0:
#         return 0
#
#     elif n == 1 or n ==2:
#         return 1
#
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# print(fibonacci(9))

# def fibonacci(n):
#     if n < 0:
#         return []
#
#     elif n == 0:
#         return [0]
#
#     elif n == 1 or n == 2:
#         return [0, 1]
#
#     else:
#         fibonacci_series = [0, 1]
#         a, b = 0, 1
#         for i in range(2,n+1):
#             a, b = b, a + b
#             fibonacci_series.append(b)
#
#         return fibonacci_series
#
#
# n = int(input("Enter your number for series: "))
# print(f"fibonacci series {fibonacci(n)}")
#

def new_data(string):
    get_Data = []

    for i in string:
        get_Data.append(i)

    return get_Data

string = "Hello"
print(new_data(string))