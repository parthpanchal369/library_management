# def second_highest_occurrence(numbers):
#
#     counters_occurrence = {}
#     # digits = [int(digit) for digit in str(numbers)]
#     for num in numbers:
#         if num in counters_occurrence:
#             counters_occurrence[num] += 1
#
#         else:
#             counters_occurrence[num] = 1
#
#     # for key,value in counters_occurrence.items():
#     #     print(f"{key} = {value}")
#
#     sorting_string = sorted(counters_occurrence.items(), key=lambda x: x[1], reverse=True)
#
#     # if len(sorting_string) > 1:
#     #     second_highest = sorting_string[1][0]
#     #     return second_highest, counters_occurrence[second_highest]
#     #
#     # else:
#     #     return None
#
#     if len(sorting_string) > 1:
#         second_highest_occurrence = sorting_string[1][1]
#         second_highest_numbers = [item[0] for item in sorting_string if item[1] == second_highest_occurrence]
#         return second_highest_numbers, second_highest_occurrence
#     else:
#         return None
#
#
# numbers = [1, 2, 2, 3, 3, 33, 4, 4, 4, 4, 3,3]
# result = (second_highest_occurrence(numbers))
#
# if result:
#     number, occurrence = result
#     print(f"THe second Highest occurring number is {number} with {occurrence} time occurrences")


# def second_highest_occurrence(numbers):
#     counters_occurrence = {}
#     for num in numbers:
#         if num in counters_occurrence:
#             counters_occurrence[num] += 1
#         else:
#             counters_occurrence[num] = 1
#
#     sorting_string = sorted(counters_occurrence.items(), key=lambda x: x[1], reverse=True)
#
#     if len(sorting_string) > 1:
#         second_highest_occurrence = sorting_string[2][1]
#         second_highest_numbers = [item[0] for item in sorting_string if item[1] == second_highest_occurrence]
#         return second_highest_numbers, second_highest_occurrence
#     else:
#         return None
#
#
# numbers = [1, 2, 2, 3, 3, 33, 4, 4, 4, 4, 3, 2]
# result = second_highest_occurrence(numbers)
#
# if result:
#     numbers, occurrence = result
#     print(f"The numbers with the second-highest occurrences are {numbers} with {occurrence} occurrences")
# else:
#     print("There is no second-highest occurrence.")


# from collections import Counter
#
#
# def second_highest_occurrence(numbers):
#
#     count_dict = Counter(numbers)
#
#     sorted_count = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
#
#     second_highest_occurrence = None
#     for num, count in sorted_count[1:]:
#         second_highest_occurrence = num
#         break
#
#     return second_highest_occurrence
#
#
#
# numbers = [1, 2,2,3,3,33,4,4,4,4,3,3]
# result = second_highest_occurrence(numbers)
# print("Second highest occurrence number:", result)


# def second_highest_occurrence(numbers):
#     count_dict = {}
#
#     for num in numbers:
#         count_dict[num] = count_dict.get(num, 0) + 1
#
#     max_occurrence = max(count_dict.values())
#
#
#     filtered_numbers = [num for num, count in count_dict.items() if count != max_occurrence]
#
#     if filtered_numbers:
#         second_max_occurrence = max([count_dict[num] for num in filtered_numbers])
#         second_highest_occurrence = next(num for num, count in count_dict.items() if count == second_max_occurrence)
#         return second_highest_occurrence
#
#     return None
#
#
# numbers = (1,2,2,3,3,33,4,4,4,4)
# result = second_highest_occurrence(numbers)
# print("Second highest occurrence number:", result)


# def second_highest_occurence(numbers):
#
#     count_dict = {}
#
#     for num in numbers:
#         count_dict[num] = count_dict.get(num, 0) + 1
#
#     max_occurrence = max(count_dict.values())


def second_highest_occurence(numbers):

    count_occurence = {}

    for num in numbers:
        if num in count_occurence:
            count_occurence[num] += 1

        else:
            count_occurence[num] = 1

    max_occurence = max(count_occurence.values())

    sorting_occurence = sorted(set(count_occurence.values()))
    second_higest_sorting = sorting_occurence[-2]
    return second_higest_sorting

result = second_highest_occurence(numbers)
if result:
    print(f"Your second higest occurence number is {result}")





