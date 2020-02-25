from random import randint
def sample(histogram):
  fence = 0
  dart = randint(0, sum(histogram.values()) - 1)
 
  for word, count in histogram.items():
    fence += count
    if fence >= dart:
      return word