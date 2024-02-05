def chr_vowels(input_string):

    vowels = ""
    charchter = ""

    for char in input_string:
        if char.lower() in "aeiou":
            vowels += char

        elif char.isalpha():
            charchter += char

    return vowels, charchter


input_string = input("Enter your string:- ")
vowels, charchter = chr_vowels(input_string)
print("Vowels:-", vowels)
print("char:-", charchter)



