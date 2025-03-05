# 1. Create a variable, name, with your first name as a string

#    b. Add to the name variable your last name with a space in between

#    c. Add to the name variable "Mr." or "Ms." or "Mrs." before your full
#        name with a space in between

#    d. Create a variable, greeting, which contains the string "Hi my name
#        is [YOUR NAME]"

#    e. Print out the greeting
name = "George"
print("1a", name)

name += " Jetson"
print("1b", name)

name = "Mr. " + name
print("1c", name)

name = "Hi my name is " + name
print("1e", name)
print()


# 2. Create a variable, length, with the value 20

#    b. Create a variable, height, with the value 15

#    c. Create a variable, area, which is equal to length x height

#    d. Create a variable, analysis, which contains the string "the result
#        of [LENGTH] x [HEIGHT] is [AREA]"

#    e. Print out the analysis variable
length = 20
height = 15
area = length * height
analysis = f"the result of {length} x {height} is {area}"
print(2, analysis)
print()


# 3. Create a variable, fruits, which is a list of three fruits

#    b. Create a variable, veggies, which is a list of three vegetables

#    c. Create a variable, meats, which is a list of three meats

#    d. Create a variable, food, which is the combination of fruits,
#        veggies, meats

#    e. Update the value of the food variable by removing all duplicates
#        (food should still be a list)

#    f. Print out the food variable
fruits = ['apple', 'orange', 'kiwi']
veggies = ['asparagus', 'spinach', 'celery']
meats = ['beef', 'pork', 'chicken']
food = fruits + veggies + meats
food = list(set(food))
print(3, food)
print()


# 4. Create a variable, salary, with the numeric value, 1,000,000

#    b. Update the salary variable by adding 2,000 to it

#    c. Update the salary variable by multiplying it by 5

#    d. Update the salary variable by dividing it by 1000

#    e. Update the salary variable by floor dividing it by 3

#    f. Create a variable, phrase, which contains "my salary is $[SALARY]"

#    g. Print out the phrase variable
salary = 1_000_000
salary += 2_000
salary *= 5
salary /= 1000
salary = int(salary / 3)
phrase = 'my salary is $' + str(salary)
print(4, salary)
print()


# 5. Create a variable, grades, which contains 5 grades

#    b. Create a variable, remove_duplicates, which contains True

#    c. Create an if/else statement:
#     * remove all duplicates from grades if remove_duplicates is True
#     * append 'F' to grades if remove_duplicates is False

#    d. Print out the grades variable
grades = ["A", "B", "C", "B", "B"]

remove_duplicates = True
if remove_duplicates:
    grades = list(set(grades))
else:
    grades.append("F")

print(5, grades)