from random import randint
import sys as sys
import random

def run_dictionary():
    filename = "/usr/share/dict/words"
    with open(filename, "r") as f:
        lines = f.readlines()
    i = len(lines)
    for n in range(0, i-1):
        lines[n] = lines[n].replace("\n", "")
    return lines

def rearrange_words():
    sentence = []
    arguments = int(sys.argv[1])
    lines = run_dictionary()
    for rand_arg in range(arguments):
        rand_words = random.randint(1, len(lines) - 1)
        sentence.append(lines[rand_words])
    st = " "
    print(st.join(sentence))
rearrange_words()
 