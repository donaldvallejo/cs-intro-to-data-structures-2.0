import sys as sys
import random

arguments = sys.argv

def rearrange():
    for rand_arg in arguments:
        rand_arg = random.randint(0, len(arguments) - 1)
        print(arguments[rand_arg])
rearrange()
 