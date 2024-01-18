
n = int(input("Enter the lines you want to print: "))
k = int((n * (n + 1))/2)

output = ""

for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        row = str(k) + " " + row
        k -= 1
    output += row.rstrip() + "\n"


print(output.rstrip())














