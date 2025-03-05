# 1. Write a Python function that takes a list of words and returns the
#     longest word and the length of the longest word.
def longest(words):
    longest_len = 0
    longest_word = ""

    for word in words:
        if len(word) > longest_len:
            longest_len = len(word)
            longest_word = word

    return longest_word, longest_len

#    b. Call the function with positional arguments
print("1b: (chimpanzee, 10):", longest(["bear", "tiger", "elephant", "chimpanzee", "giraffe"]))

#    c. Call the function with keyword arguments
print("1c: (watermelon, 10):", longest(["apple", "orange", "eggplant", "watermelon", "grapefruit"]))


# 2. Write a Python function to remove the n-th index character from a
#     nonempty string.

#    b. Call the function with positional arguments

#    c. Call the function with keyword arguments
def removeNth(in_str, pos):
    # temp_arr = []
    # for i, char in enumerate(in_str):
    #     if i != pos:
    #         temp_arr.append(char)
    # return "".join(temp_arr)

    # temp_arr = list(in_str)
    # del temp_arr[pos]
    # return "".join(temp_arr)

    return in_str[:pos] + in_str[pos + 1:]

print(removeNth("mango", 3))
print(removeNth(pos=3, in_str="mango"))


# 3. Create a function called add_title which takes a name and gender as
#     arguments and returns either "Mr. <name>" or "Ms. <name>"
#     (eg. Calling `add_title("Pam", "F")` returns "Ms. Pam")

#    b. Call the function with positional arguments

#    c. Call the function with keyword arguments
def add_title(name, gender):
    # if gender == "M":
    #     return f"Mr. {name}"
    # else:
    #     return f"Ms. {name}"

    title = "Mr."

    if gender == "F":
        title = "Ms."

    return title + " " + name
    

print(add_title("Pam", "F"))
print(add_title(gender="F", name="Pam"))

print(add_title("Flavio", "M"))
print(add_title(gender="M", name="Flavio"))

color = "red"
print(f"{color} apple")  # {f}ormatted string


# 4. Create a function called multiply_elements which takes a list and a
#     number as arguments. It multiplies each element in the list by the
#     number, and returns the list

#    b. Call the function with positional arguments

#    c. Call the function with keyword arguments

nums = [57, 24, 6, 1, 778]

def multiply_elements(the_list, multiplier):
    for i in range(len(the_list)):
        the_list[i] = the_list[i] * multiplier

    return the_list

print(multiply_elements(nums, 2))
print(multiply_elements(multiplier=2, the_list=nums))
