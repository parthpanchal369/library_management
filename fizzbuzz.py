def fizz_buzz(numbers):

    for i in range(1,numbers+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 ==0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)

numbers = int(input("Enter the number: "))
fizz_buzz(numbers)