from random import randint
import sys as sys
import random

def histogram(longstring):
  list_of_tup = []
  
  for each_word in longstring: 
    
    to_add = True
    for j in range(len(list_of_tup)):
    #   print(list_of_tup[j], list_of_tup[j][0], list_of_tup[j][1])
      if list_of_tup[j][0] == each_word:
        list_of_tup[j] = (each_word, list_of_tup[j][1]+1)
        to_add = False
        break
 
    # if not in list-of-tuple, add it to the list
    if to_add:
      list_of_tup.append(tuple((each_word, 1)))

    
  return list_of_tup

def unique_words(tup):
  return len(tup)   

def frequency(tup, word):
  for j in tup:
    if j[0] == word:
      return j[1]
  else: 
    return None

def get_text(filename):
    with open(filename, 'r') as f:
        data = f.read().split(" ")
    print(len(data))
    return data


if __name__ == "__main__":
  wordList = get_text(sys.argv[1])
  tup = histogram(get_text(sys.argv[1]))
  print(unique_words(tup))
  print("Unique words:" + str(unique_words(tup)))
  print("# of 'and':" + str(frequency(tup, "and")))
  print("# of 'they':" + str(frequency(tup, "they")))