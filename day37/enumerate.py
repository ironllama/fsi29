# 1. Use a loop to display elements from the following list that are 
#     present at odd index positions.
num_li = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# for num in num_li[1::2]:
#     print(num)

# for items in enumerate(num_li):
#     if items[0] % 2 != 0:
#         print(items[1])

# for i, num in enumerate(num_li):
#     if i % 2 != 0:
#         print(num)

for i in range(1, len(num_li), 2):
    print(num_li[i])

# 2. Filter the following list, so that you only print out the line position
#     and names of people who are 21 or over. Print out all the positions and
#     names comma delimited, with the position in square brackets.
#     (Example output: "[2]: Peter, [3]: Paul, [4]: Mary")
people_in_line = [ 
    ("Boyd", 52),
    ("Mylene", 19),
    ("Retta", 31),
    ("Ethyl", 23),
    ("Irwin", 12),
    ("Murray", 30)
]

# for i, (name, age) in enumerate(people_in_line):
#     if age >= 21:
#         print(f"[{i}]: {name}")

for i, person in enumerate(people_in_line):
    if person[1] >= 21:
        print(f"[{i}]: {person[0]}")