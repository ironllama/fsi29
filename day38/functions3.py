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


# 4. Write a function to reverse a string, without using the built-in
#     `reverse` function.
def rev_string(in_str):
    return in_str[::-1]

print("#4: olleh - ", rev_string("hello"))


# 5. Write a function called 'withinRange' that takes three parameters,
#     a number you are checking for, the first number to check against and
#     the last number to check against. Check whether the first number falls
#     in between the other numbers (inclusive) and return a boolean.

def withinRange(target, start, end):
    return start <= target <= end

print("#5: True - ", withinRange(4, 1, 10))
print("#5: True - ", withinRange(1, 1, 10))
print("#5: True - ", withinRange(10, 1, 10))
print("#5: False - ", withinRange(11, 1, 10))


# 6. Write a function that takes a list and returns a new list with
#     unique elements of the first list. (Duplicates removed.)
def uniques(in_list):
    return list(set(in_list))

print("#6: [3, 5, 6] - ", uniques([3, 5, 3, 6, 5, 6]))


# 7. Write a function that takes a number as a parameter and checks if the
#     number is prime or not.
def is_prime(num):
    if num <= 3:  # 1, 2, and 3 are already known as prime.
        return True
    
    if num % 2 == 0:  # Even numbers are automatically not prime.
        return False

    # Test if wholly divisible by a factor.
    # Only use odd numbers starting with 3; num is already odd; can't divide even and odd
    # Only test up to num/2 since factors will be mirrored around the mid-point
    for d in range(3, int(num/2), 2):
        if num % d == 0:
            return False
    
    return True
        
print("#7: - True: ", is_prime(1))
print("#7: - True: ", is_prime(3))
print("#7: - True: ", is_prime(13))
print("#7: - False: ", is_prime(15))
print("#7: - False: ", is_prime(16))


# 8. Write a function to print only the even numbers from a given list.
def only_evens(in_list):
    for num in in_list:
        if num % 2 == 0:
            print(num)

print("#8: [4, 24, 2, 200]")
only_evens([67, 4, 24, 33, 971, 2, 13, 200])

# 9. Write a function to create and print the list of squares for the
#      numbers between 1 and 30 (both included).
def squares():
    res = []
    for num in range(1, 31):
        res.append(num * num)
    print("#9: squares: ", res)

squares()
