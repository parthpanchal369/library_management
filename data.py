# def not_participate(meetup_candidate, prama_employee):
#
#     not_signup = []
#
#     for person in prama_people:
#         if person["name"] not in {p["name"] for p in participants if p["signed_up"] == True}:
#             not_signed_up.append(person["name"])
#     return not_signed_up
#
# print("Person who have not signup for prama")
#
# for person in not_signup:
#     print(person)




# def identify_people_not_signed_up(participants, prama_people):
#
#     not_signed_up = [person["name"] for person in prama_people if person["name"] not in {p["name"] for p in participants if p["signed_up"]}]
#     return not_signed_up
#
#
# participants_data = [
#     {"name": "John", "signed_up": True},
#     {"name": "Jane", "signed_up": False},
#     {"name": "Bob", "signed_up": True},
#     # Add more participants as needed
# ]
#
# prama_people_data = [
#     {"name": "John"},
#     {"name": "Jane"},
#     {"name": "Alice"},
#     # Add more people from Prama as needed
# ]
#
# not_signed_up_people = identify_people_not_signed_up(participants_data, prama_people_data)

# print("People from Prama who haven't signed up:")
# for person in not_signed_up_people:
#     print(person)





# meetup_list = [1,2,3,4,5]
#
# prama_data = [1,3,5,7,9,6]
# new_list = []
# for person in prama_data:
#     if person not in meetup_list:
#         new_list.append(person)
#
#
# print(new_list)

import requests
response = requests.get("https://api.thecatapi.com/")
print(response.text)
# '{"message":"The Cat API","version":"1.2.5"}'

