#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
# YOUR CODE HERE

num = str(number)
if num[-1] > "5":
    print(f'Last digit of {num[:-1]} is {num[-1]} and is greater than 5')
elif num[-1] == 0:
    print(f'Last digit of {num[:-1]} is {num[-1]} and is 0')
elif num[-1] < '6' != '0':
    print(f'Last digit of {num[:-1]} is {num[-1]} and is less than 6 and not 0')

