from random import randint
from sample import sample


#TODO: 1. Write the generate_words function here
def generate_words(my_histogram, num_words):
  for word in range(num_words):
    word = sample(my_histogram)
    print(word)
  # print(sample(histogram))

#Uncomment this to test printing 5 words
my_histogram = {"one":1, "fish":4, "two":1, "red":1, "blue":1}
generate_words(my_histogram, 5)


#TODO: 2. Make the functions in color.py into methods in the Rainbow class
class Rainbow:
  def __init__(self, colors):
    self.colors = colors
    
  def add_color(self, color):
    self.colors.append(color)

  def remove_color(self, color):
    if color in self.colors:
      self.colors.remove(color)
    
  def print_colors(self):
    for color in self.colors:
      print(color)
    
#uncomment to test
my_rainbow = Rainbow(["orange", "green", "pink"])
my_rainbow.add_color("red")
my_rainbow.remove_color("orange")
#Should see green, pink, red printed
my_rainbow.print_colors()
