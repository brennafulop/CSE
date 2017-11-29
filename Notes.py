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

#functions


def print_hw():
    print("Hello world.")
    print("Enjoy the day.")


print_hw()


def say_hi(name):  # Name is a "parameter"
    print("Hello %s" % name)
    print("Coding is great!")


say_hi("Brenna")  # insert any name


def print_age( name, age):
    print("%s is %d years old" % (name, age))  # there can only be one item after the percent. ()'s combine them
    age += 1 # age = age + 1   # += is the best way to add one to a digit. (+=, -=, *=, /=, %=)
    print("Next year, %s will be %d years old" % (name, age))


print_age("Brenna", 14)


def algebra_hw(x):
    return x**3 + 4*x**2 +7 * x - 4


print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))


# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80: # else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc(89))