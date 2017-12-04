
# 12.4.17
# Write a python function
# which accepts the user's
# first and last name
# and print them in reverse


def reverse_order(first_name, last_name):
    print("%s, %s" % (last_name, first_name))
    # or print(last_name + " " + first_name) #concatenation

first = input('what is your first name?')
last = input('what is your last name?')

reverse_order(first, last)