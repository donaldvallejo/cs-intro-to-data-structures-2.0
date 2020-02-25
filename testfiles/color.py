#TODO: 2. Refactor these functions to be methods in the Rainbow class inside main
colors = ["red", "blue", "violet"]
def add_color(color):
  colors.append(color)

def remove_color(color):
  if color in colors:
    colors.remove(color)
    
def print_colors():
  for color in colors:
    print(color)
