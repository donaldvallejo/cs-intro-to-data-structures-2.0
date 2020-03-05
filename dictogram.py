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

# class Dictogram(dict):
#     """Dictogram is a histogram implemented as a subclass of the dict type."""

#     def __init__(self, word_list=None):
#         """Initialize this histogram as a new dict and count given words."""
#         super(Dictogram, self).__init__()  # Initialize this as a new dict
#         # Add properties to track useful word counts for this histogram
#         self.types = 0  # Count of distinct word types in this histogram
#         self.tokens = 0  # Total count of all word tokens in this histogram
#         # Count words in given list, if any
#         if word_list is not None:
#             for word in word_list:
#                 self.add_count(word)

#     def add_count(self, word, count=1):
#         """Increase frequency count of given word by given count amount."""
#         # TODO: Increase word frequency by count

#         if word not in self:
#             self[word] = count
#             self.tokens += count
#             self.types += count
#         else:
#             self[word] += count
#             self.tokens += count

#     def frequency(self, word):
#         """Return frequency count of given word, or 0 if word is not found."""
#         # TODO: Retrieve word frequency count

#         if word not in self:
#             return 0
#         else:
#             return self.get(word)

# if __name__ == '__main__':
#     main()





