def get_unique_words(input_string):
    words = []
    current_word = '  '

    for char in input_string:
        if char.isalnum() or char == "'":
            current_word += char
        elif current_word:
            words.append(current_word.lower())
            current_word = ''

    if current_word:
        words.append(current_word.lower())

    unique_words = set(words)

    return unique_words


input_str = "Fear leads to anger; anger leads to hatred; hatred leads to conflict; conflict leads to suffering."
unique_words = get_unique_words(input_str)
print("Unique words:",", ".join(unique_words))

# def get_unique_words(input_string):
#     words = input_string.split()
#
#     words = [word.strip(".,;:'\"()[]{}") for word in words]
#
#     unique_words = set(words)
#
#     return unique_words
#
#
# input_str = "Fear leads to anger; anger leads to hatred; hatred leads to conflict; conflict leads to suffering."
# unique_words = get_unique_words(input_str)
# print("Unique words:", ", ".join(unique_words))

# def get_unique_words(input_string):
#
#     words = input_string.split()
#
#     words = [word.strip(";") for word in words]
#
#     unique_words = set(words)
#
#     return unique_words
#
#
# input_str = "Fear leads to anger; anger leads to hatred; hatred leads to conflict; conflict leads to suffering."
# unique_words = get_unique_words(input_str)
# print("Unique words: ",", ".join(unique_words))


