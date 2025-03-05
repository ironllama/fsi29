# # 2. Write a Python function to remove the n-th index character from a
# #     nonempty string.

# #    b. Call the function with positional arguments

# #    c. Call the function with keyword arguments

# def removeNth(in_str, pos):
#     # temp_arr = []
#     # for i, char in enumerate(in_str):
#     #     if i != pos:
#     #         temp_arr.append(char)
#     # return "".join(temp_arr)

#     # temp_arr = list(in_str)
#     # del temp_arr[pos]
#     # return "".join(temp_arr)

#     return in_str[:pos] + in_str[pos + 1:]

# print(removeNth("mango", 3))
# print(removeNth(pos=3, in_str="mango"))




# 3. Create a function called add_title which takes a name and gender as
#     arguments and returns either "Mr. <name>" or "Ms. <name>"
#     (eg. Calling `add_title("Pam", "F")` returns "Ms. Pam")

#    b. Call the function with positional arguments

#    c. Call the function with keyword arguments

# def add_title(name, gender):
#     # if gender == "M":
#     #     return f"Mr. {name}"
#     # else:
#     #     return f"Ms. {name}"

#     title = "Mr."

#     if gender == "F":
#         title = "Ms."

#     return title + " " + name
    

# print(add_title("Pam", "F"))
# print(add_title(gender="F", name="Pam"))

# print(add_title("Flavio", "M"))
# print(add_title(gender="M", name="Flavio"))

# color = "red"
# print(f"{color} apple")  # {f}ormatted string


# # 4. Create a function called multiply_elements which takes a list and a
# #     number as arguments. It multiplies each element in the list by the
# #     number, and returns the list

# #    b. Call the function with positional arguments

# #    c. Call the function with keyword arguments

# nums = [57, 24, 6, 1, 778]

# def multiply_elements(the_list, multiplier):
#     for i in range(len(the_list)):
#         the_list[i] = the_list[i] * multiplier

#     return the_list

# print(multiply_elements(nums, 2))
# print(multiply_elements(multiplier=2, the_list=nums))


# 1. Write a function to find the largest of three numbers, without using
#     the built-in `max` function.
def largest_num(one, two, three):
    largest = one

    if two > largest:
        largest = two
    if three > largest:
        largest = three
    
    return largest


print("#1: 34 - ", largest_num(4, 34, 2))

# 2. Write a function to sum all the numbers in a list, without using the
#     built-in `sum` function.
def sum_nums(in_list):
    the_sum = 0

    for num in in_list:
        the_sum += num

    return the_sum

print("#2: 13 - ", sum_nums([5, 2, 6]))


# 3. Write a function to multiply all the numbers in a list, without using
#     any library functions.
def multiply_nums(in_list):
    the_product = 1

    for num in in_list:
        the_product *= num

    return the_product

print("#3: 64 - ", multiply_nums([2, 8, 4]))
