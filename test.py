from random import randint

filename = "/Users/localscrub/dev/makeSchool/CS/1.2/cs-intro-to-data-structures-2.0/words.txt"

my_file = open(filename, "r")

lines = my_file.readlines()

random_index = randint(0, len(lines)-1)
print(lines[random_index])