# 1. Ask the user for a number. Depending on whether the number is even or
#     odd, print out an appropriate message to the user. If the number is a
#     multiple of 4, print out yet another message.
# number = input("Gimme a number: ")
# number = int(number)

# if number % 2 == 0:
#     print("Your number is even!")

# if number % 4 == 0:
#     print("You number is a multiple of four!")


# 2. Use the following list and write a function that prints out all the
#     elements of the list that are less than 5.
arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def less_than_five(in_list):
    for num in in_list:
        if num < 5:
            print(num)

less_than_five(arr)


#    b. Instead of printing the elements one by one, make a new list that
#        has all the elements from arr that are less than 5 and print
#        out this new list.
def less_than_five_b(in_list):
    new_list = []
    for num in in_list:
        if num < 5:
            new_list.append(num)
    print(new_list)

less_than_five_b(arr)


# 3. Create a function that asks the user for a number and then prints out a
#     list of all the divisors of that number.
def get_divisors(num):
    divisors = []
    for x in range(1, num + 1):
        if num % x == 0:
            divisors.append(x)
    print(divisors)

get_divisors(12)
get_divisors(13)


# 4. Use the following lists and write a function that returns a new list that
#     contains only the elements that are common between the lists (without 
#     duplicates).
arr1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def get_common(one, two):
    # return list(set(one) & set(two))
    result = []
    for x in one:
        if x in two and x not in result:
            result.append(x)
    return result

print(get_common(arr1, arr2))


# 5. Write a function that asks the user for a string and prints out whether
#     this string is a palindrome or not. (A palindrome is a string that
#     reads the same forwards and backwards.)

def check_palindrome():
    word = input("Give me a word: ")
    if word == word[::-1]:
        print("That is a palindrome!")
    else:
        print("Not a palindrome. :(")

check_palindrome()
