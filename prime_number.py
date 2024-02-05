def prime_number(numbers):

    if numbers <= 1:
        return False

    else:

        for i in range(2,numbers):
            if numbers % i == 0:
                return False

        return True

numbers = int(input())
# if prime_number(numbers):
#     print(f"your {numbers} is a prime numbr")
#
# else:
#     print(f"Your {numbers} is not a prime number")

for i in range(1,numbers):
    if prime_number(i):
        print(i)

