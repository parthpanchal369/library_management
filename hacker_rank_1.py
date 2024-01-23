l = ["a","b","c","d"]
# string ="".join(l)
print(l[0:10:2])
dict1={"fruit1":"apple","fruit2":"banana","veg1":"tomato"}
dict1.update({"veg2":"brinjal"})
print(dict1)
dict1.update({"veg3":"chilli"})  # updates the dictionary at the end
print(dict1)
dict1.pop("veg2")
print(dict1)
