'''
# print("Hello world")
#
# # brenna
#
# a = 4
# b = 3
#
# print(3+5)
# print(5-3)
# print(3*5)
# print(6/2)
# print(3 ** 2)
#
# print("try to figure out how this works")
# print(11 % 5)
#
# # the "%" sign is a modulus. It finds a remainder.
#
# car_name = "the brenna mobile"
# car_type = "Porsche"
# car_cylinders = 10
# car_mpg = 6000
#
# print("I have a car called %s. It's pretty nice." % car_name)
# print("I have a car called %s. It's a %s."% (car_name, car_type)) #watch the order
#
# # here is where we get a little fancy
# print("What is your name?")
# name=input(">_")
# print("Hi %s." %name)
#
# age = input("How old are you?")
# print("%s?! That's really old. You belong in a retirement home." %age)
#
# print("wake up neo")

# functionsd
# def print_hw():
#     print("Hello world.")
#     print("Enjoy the day.")
#
#
# print_hw()
#
#
# def say_hi(name):  # Name is a "parameter"
#     print("Hello %s" % name)
#     print("Coding is great!")
#
#
# say_hi("Brenna")  # insert any name
#
#
# def print_age( name, age):
#     print("%s is %d years old" % (name, age))  # there can only be one item after the percent. ()'s combine them
#     age += 1 # age = age + 1   # += is the best way to add one to a digit. (+=, -=, *=, /=, %=)
#     print("Next year, %s will be %d years old" % (name, age))
#
#
# print_age("Brenna", 14)
#
#
# def algebra_hw(x):
#     return x**3 + 4*x**2 +7 * x - 4
#
#
# print(algebra_hw(3))
# print(algebra_hw(4))
# print(algebra_hw(5))
# print(algebra_hw(6))
# print(algebra_hw(7))
#
#
# # if statements
#
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80: # else if
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#         return "F"
#
#
# print(grade_calc(89))
#
#
# def happy_bday(name): # def defines a function
#     print("Happy birthday to you")
#     print("Happy birthday to you")
#     print("Happy birthday dear %s " %name) # also works as print("Happy birthday dear " + name)
#     print("Happy birthday to you!")
#
#
# (happy_bday("Brenna"))


# Loops
# for num in range(10):
#     print (num + 1)
#
# # While Loops (BEWARE)
# a = 1
# while a < 10:
#     print(a)
#     a += 1 # This iterates so that we can break the loop

# Random Numbers
# import random
# print(random.randint(0, 10))


# Recasting
c = '1'
print(c == 1) # we have a string and an integer
print(int(c) == 1)
print(c == str(1))


# Comparisons
print( 1 == 1) # Use a double equal sign
print(1 != 2) # One is not equal to two
print(not False) # "!" is the "not" operator


# Lists
the_count = [1, 2, 3, 4, 5]
cheeseburger_ingredients = ['cheese', 'beef', 'sauce', 'sesame seed bun', 'avocado', 'onion']
print(cheeseburger_ingredients[0])
print(cheeseburger_ingredients[3])
print(len(cheeseburger_ingredients))
print(len(the_count))

# Going through lists
for item in cheeseburger_ingredients:
    print(item)

for variable in the_count:
    print(variable * 2)

length = len(cheeseburger_ingredients)
range(5)  # A list of the numbers 0 through 4]
range(len(cheeseburger_ingredients))  # Generates a list of all indices

for num in range(len(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[num]
    print('The item at index %d is %s' % (num, item))


# Recasting into a list
strOne = "Hello World!"

listOne = list(strOne)
print(listOne)
print(listOne[-1])
listOne[11] = "."

# Adding things to a list
cheeseburger_ingredients.append("fries")
print(cheeseburger_ingredients)
cheeseburger_ingredients.append("tomato")
print(cheeseburger_ingredients)

# Remove things from a list
cheeseburger_ingredients.pop(1)  # removes from a specific index
print(cheeseburger_ingredients)
cheeseburger_ingredients.remove("tomato")
print(cheeseburger_ingredients)

# Getting the alphabet
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)

# Making things lowercase
strTwo = "ThIs Is A VeRY oDd sEnTeNCe"
lowercase = strTwo.lower()
print(lowercase)

# Joining lists
L1 = ["h", 'e', 'l', 'l', 'o']
print(L1)
L1 = ''.join(L1)
print(L1)
'''

# Dictionaries - Made up of key: value pair

dictionary = {'name': 'Lance', 'age': 26, 'height': 6 * 12 + 2}

# Accessing things from a dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Add a pair to a dictionary
dictionary['profession'] = 'telemarketer'

large_dictionary = {
    'CA': 'California',
    'AZ': 'Arizona',
    'NY': 'New York'
}
print(large_dictionary['NY'])

larger_dictionary = {
    'CA': [
        'Fresno',
        'San Francisco',
        'San Jose'
    ],
    'AZ': [
        'Phoenix',
        'Tuscon'
    ],
    'NY': [
        'New York',
        'Brooklyn'
    ]
}
print(larger_dictionary['NY'])
print(larger_dictionary['NY'][1])
print(larger_dictionary['AZ'][0])

largest_dictionary = {
    'CA': {
        "NAME": "California",
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    "AZ": {
        'NAME': "Arizona",
        'POPULATION': '6931000',
        "BORDER ST": [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    "NY": {
        'NAME': 'New York',
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            "Pennsylvania",
            'New Jersey'
        ]
    }
}
current_node = largest_dictionary['NY']
print(current_node['NAME'])
print(current_node["POPULATION"])
