# 1. Remove all odd numbers in a given list using a lambda.
nums = [74, 6, 3, 78, 25, 92, 44, 37]

print(list(filter(lambda x: x % 2 == 0, nums)))

# 2. Square every number in a given list of integers using a lambda.

print(list(map(lambda x: x*x, nums)))
