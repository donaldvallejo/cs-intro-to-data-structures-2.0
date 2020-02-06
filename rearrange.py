import sys as sys
import random

# arguments = sys.argv
arguments = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def rearrange():
    for i in arguments:
        i = random.randint(0, len(arguments) - 1)
        print(arguments[i])
rearrange()