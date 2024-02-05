# def brackets_check(brackets):
#
#     get_box = []
#     opening_brackets = "({["
#     closing_brackets = ")}]"
#
#     for char in brackets:
#         if char in opening_brackets:
#             get_box.append(char)
#
#         elif char in closing_brackets:
#             if not get_box or opening_brackets[closing_brackets.index(char)] != get_box.pop():
#                 return False
#
#     return not get_box
#
#
# input_brackets = input("Enter your brackets:- ")
# if brackets_check(input_brackets):
#     print(True)
#
# else:
#     print(False)


def brackets_check(expressions):
    get_expressions = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in expressions:
        if char in brackets.values():
            get_expressions.append(char)

        elif char in brackets.keys():
            if not get_expressions or get_expressions.pop() != brackets[char]:
                return False

    return not get_expressions


input_expressions = input("Enter your expressions:- ")
if brackets_check(input_expressions):
    print(True)

else:
    print(False)




