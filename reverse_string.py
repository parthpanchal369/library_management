# def reverce_string(str):
#
#     str1 = " "
#
#     for i in str:
#         str1 = i + str1
#
#     return str1
#
#
# str = input("Enter your string:- ")
# print(reverce_string(str))

# str1 = "parth"
# new_str = "".join(reversed(str1))
# print(new_str)

def reverced_string(str):

    str1 = ""
    new_str = len(str)

    while new_str > 0:
        str1 += str[new_str-1]
        new_str = new_str - 1

    return str1


str = input("Enter your string:- ")
print(reverced_string(str))