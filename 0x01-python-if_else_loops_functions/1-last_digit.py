#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    LastNum = number % 10
else:
    LastNum = number % -10
if LastNum > 5:
    print("Last digit of", number, "is", LastNum, "and is greater than 5")
elif LastNum == 0:
    print("Last digit of", number, "is", LastNum, "and is 0")
else:
    print("Last digit of", number, "is", LastNum,
          "and is less than 6 and not 0")
