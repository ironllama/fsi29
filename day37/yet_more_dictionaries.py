# 1. Create an empty dictionary called monster. Then add the following properties:
#     "damage" property set to 500
#     "defense" property set to 70
#     "weakness" property set to "water"

#    b. Do it again, all in one line of Python code

#    c. Set its "name" property to "Gogomish" in a separate line of code

#    d. Print out the monster
monster = {}
monster.setdefault("damage", 500)
monster.update({ "defense": 70 })
monster["weakness"] = "water"
print("1a", monster)

monster = { "damage": 500, "defense": 70, "weakness": "water" }
print("1b", monster)

monster["name"] = "Gogomish"
print("1c", monster)

# 2. Starting with the dictionary:
boy = {"height": 100, "weight": 250}

#    a. Delete the "height" property from boy
del boy["height"]
print("2a", boy)

#    b. Delete the "weight" property from boy
del boy["weight"]
print("2b", boy)

#    c. Print out the boy