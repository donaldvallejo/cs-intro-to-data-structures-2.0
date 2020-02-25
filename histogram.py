from random import randint
import sys as sys
import random

# def histogram(lines):
#   string = lines.split(" ")
#   di = dict()
#   for i in string: 
#     if i in di:
#       di[i] += 1
#     else:
#       di[i] = 1
#   return di

# def unique_words(di):
#   occ = 0
#   for i in di:
#     if di[i] == 1:
#       occ += 1
#   return occ   
  

# def frequency(di, word):
#   return di[word] 

# def get_text(filename):
#     with open(filename, 'r') as f:
#         data = f.read().replace("\n", "")
#     return data

# if __name__ == "__main__":
#     di = histogram(get_text(sys.argv[1]))
#     print("Unique words:" + str(unique_words(di)))
#     print("# of 'The':" + str(frequency(di, "the")))
#     print("# of 'And':" + str(frequency(di, "and")))

filename = "words.txt"
# jess histogram
def histogram(lines):
  histogram = {}
  for word in lines:
    word = word.rstrip()
    histogram[word] = histogram.get(word, 0) + 1
  return histogram

def get_frequency(word, histogram):
  
  return histogram

def get_lines(filename):
  with open(filename, "r") as fh:
    return fh.readlines()
