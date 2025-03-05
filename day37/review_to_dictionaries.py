# 1. Create a list of 3 fruits and store it in a variable called "fruits"

#    b. Check if "apples" is in your list of fruits (True or False)

#    c. Append 2 more fruits to your list of fruits

#    d. Update your fruits variable to contain the values of the original
#       fruits list, but in reverse order

#    e. Print the very first in your list of fruits

#    f. Print the 3rd and 4th fruits as a sublist (shorter list)

#    g. Add the string 'big ' in front of the last item in the list
#       If the last fruit was "pineapple", update it to be "big pineapple"

#    h. Pop off the last fruit in the list and store it in variable big_fruit

#    i. Print the current length of the fruits list

#    j. Print the length of big_fruit
fruits = ["apple", "orange", "kiwi"]

print("1b", end=" ")
if "apple" not in fruits:
    print("NO", end=" ")
print("APPLES")

fruits.append("watermelon")
fruits.append("grape")
print("1c", fruits)

fruits = fruits[::-1]
print("1d", fruits)

print("1e", fruits[0])

print("1f", fruits[2:4])

fruits[-1] = "big " + fruits[-1]
print("1g", fruits)

big_fruit = fruits.pop()
print("1h", big_fruit)

print("1i", len(fruits))

print("1h", len(big_fruit))
print()


# 2. Create an empty dictionary and store it in the variable shopping_cart.
#     Then add the following keys:
#     - "items" key should correspond to an empty list
#     - "created_at" key should correspond to today's date as a string
#     - "total" key is the total value of the items in shopping_cart (0)
#     - "recent" key should correspond to True

#    b. Update the "total" in the shopping_cart by increasing it by 5000

#    c. Update the "items" in the shopping_cart by appending to it big_fruit

#    d. Check if "big apples" is in the "items" list in your shopping_cart
shopping_cart = {}
shopping_cart["items"] = []
shopping_cart["created_at"] = "2024-05-07"
shopping_cart["total"] = 0
shopping_cart["recent"] = True
print("2a", shopping_cart)

shopping_cart["total"] += 5000
print("2b", shopping_cart["total"])

shopping_cart["items"] += [big_fruit]
print("2c", shopping_cart["items"])

if "big apples" in shopping_cart["items"]:
    print("BIG APPLES!")
else:
    print("No big apples.")
print()


# 3. Create a dictionary called favorites. It should have...
#    an "items" property that corresponds to ["water", "juice", "bread"]
#    a "total" property that corresponds to 15000
#    a "recent" property that corresponds to False
#    and a "created_at" property that is yesterday's date as a string
favorites = {
    "items": ["water", "juice", "bread"],
    "total": 15_000,
    "recent": False,
    "created_at": "2024-05-06"
}
print("3", favorites)
print()


# 4. Create a dictionary called order. It should have...
#    an "items" property which is the combination of
#         "items" from shopping_cart and
#         "items" from favorites
#    a "total" property which is the sum of
#         "total" from shopping_cart and
#         "total" from favorites
#    a "created_at" property which corresponds to today's date as a string
#    a "recent" property which corresponds to applying logical or to
#         "recent" of shopping_cart and
#         "recent" of favorites
order = {
    "items": shopping_cart["items"] + favorites["items"],
    "total": shopping_cart["total"] + favorites["total"],
    "created_at": shopping_cart["created_at"],
    "recent": shopping_cart["recent"] or favorites["recent"]
}
print("4", order)