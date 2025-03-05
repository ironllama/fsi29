# 1. Reverse the following integer number:
num = 83275

num = str(num)
end = len(num)
while end > 0:
    print(num[end - 1], end="")
    end -= 1
print()
print()

# 2. Display the subsequent cubes of the following number up to 1 million:
grow = 3

while grow < 1_000_000:
    print(grow)
    grow **= 3

# 3. Ask the user for numbers until they enter no number. Then throw out the
#     max and min numbers (if max or min appear more than once, throw those
#     out, as well) and print out the mean of all the numbers up to 2
#     decimal places.
all_inputs = set()
while True:
    num = input("Enter a number: ")
    if num == '':
        break
    else:
        all_inputs.add(int(num))

all_inputs.remove(max(all_inputs))
all_inputs.remove(min(all_inputs))
final = sum(all_inputs) / len(all_inputs)

# All ways to get at most 2 decimal places.
final = int(final * 100) / 100
# final = round(final, 2)

# To force 2 decimal places.
# final = "%.2f" % final
# final = format(final, ".2f")
# final = "{:.2f}".format(final)

print(3, final)