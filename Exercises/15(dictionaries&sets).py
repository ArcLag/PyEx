fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# fruit_list = ["Orange ", "Apple ", "Lemon ", "Grape ", "Lime "]



# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit["pear"])

# while True:
#     print("Please type one of the following fruit: " + str(fruit_list))
#     dict_key = input()
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# for snack in fruit:
#     # print(fruit[snack])

# bike = {"make": "Honda",
#         "model": "250 dream",
#         "colour": "red",
#         "engine_size": 250}

# print(bike)
# print(bike["make"])

# fruit_keys = fruit.keys()
# print(fruit_keys)

# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)


print(dict(f_tuple))
