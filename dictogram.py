filename = "words.txt"
class Dictogram:
    def __init__(self, filename):
    self.histogram = {}
    
    def build_histogram(self):
        for word in self.lines:
            word = word.rstrip()
            self.histogram[word] = self.histogram.get(word, 0) + 1
        return histogram

    def get_frequency(self, word):
        return self.histogram[word]

my_file = open("words.txt", "r")
lines = my_file.readlines()
my_histogram = Dictogram()
my_histogram.build_histogram(lines)


