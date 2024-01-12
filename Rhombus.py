
rows = int(input("Enter your number for print stars: "))

for i in range(rows):

    print(" " * (i), end=" ")
    for j in range(rows):
        print("*", end=" ")

    print()