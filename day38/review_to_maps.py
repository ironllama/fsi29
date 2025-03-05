# 1. Write a function to find the sum of the series, up to n terms.
#     ie. 2 + 22 + 222 + 2222 + .. n terms
#     Call the function with number_of_terms to verify that your
#     function works as expected. Choose any number for the term.
number_of_terms = 5  # => 24690 (total of 2 + 22 + 222 + 2222 + 22222)

def number_of_terms(n):
    sum = 0
    for i in range(1, n+1):
        sum += int('2' * i)
        print("number_of_terms: adding: ", '2' * i, "sum:", sum)
    return sum

print("1. 2 - ", number_of_terms(2))

#    b. Change number_of_terms to verify that your function is correct.

print("1. 4 - ", number_of_terms(4))
print("1. 5 - ", number_of_terms(5))
print("1. 7 - ", number_of_terms(7))


# 2. Print out the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# print('*')
# print('* *')
# print('* * *')
# print('* * * *')
# print('* * *')
# print('* *')
# print('*')

# print('*\n* *\n* * *\n* * * *\n* * *\n* *\n*')

num = 1
dir = 1
while num > 0:
    print("* " * num)
    if num < 4 and dir == 1:
        num += 1
    else:
        num -= 1
        dir = -1


# 3. Write a function calculation() such that it can accept two variables
#     and calculate the addition and subtraction of them. It must return
#     both addition and subtraction results in a single function call.

def calculation(one, two):
    add_res = one + two
    sub_res = one - two
    return add_res, sub_res

print("3. (30, -10) - ", calculation(10, 20))
print("3. (77, 7) - ", calculation(42, 35))
