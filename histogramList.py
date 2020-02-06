# write a function that takes in a list of file as a list of words
# make an empty list
# loop through each word in the list
# loop through item with in each list
# check if in list loop through 
# loop though inner list
# if not already in then .append(word,1)
# list of lists .append([word, 1])
# else add one to the value
# list count [index][1] += 1

# make a helper function to look though if lists are in there make if else statement similarly to the dict way

from random import randint
import sys as sys
import random

def histogram(longstring):
  arr = []
  for i in longstring: 
    for j in arr:
      if j[0] == i:
        j[1] += 1
        break
    else:
      arr.append([i, 1])
  return arr

def unique_words(arr):
  return len(arr)   

def frequency(arr, word):
  for j in arr:
    if j[0] == word:
      return j[1]
  else: 
    return None

def get_text(filename):
    with open(filename, 'r') as f:
        data = f.read().split(" ")
    return data


if __name__ == "__main__":
  wordList = get_text(sys.argv[1])
  arr = histogram(get_text(sys.argv[1]))
  print(unique_words(arr))
  print("Unique words:" + str(unique_words(arr)))
  print("# of 'The':" + str(frequency(arr, "the")))
  print("# of 'And':" + str(frequency(arr, "and")))