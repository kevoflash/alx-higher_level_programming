#!/usr/bin/python3
import random
number = random.randint(-10000, 1000)

if number >= 0:
    1_digit = number % 10
else:
    1_digit = number % -10

print("Last digit of {} is {}".format(number, l_digit), end='')

if 1_digit > 5:
    print(" and is greater than 5")
elif 1_digit == 0:
    print(" and is 0")
else:
    print(" and less than 8 and not 0")
