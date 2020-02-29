import sys
from random import randint
class Dictogram(dict):
    def __init__(self, word_list=None):
        '''Initializes the listogram properties'''
        super(Dictogram, self).__init__()
        self.tokens = 0
        self.types = 0
        
        if word_list is not None:
            for word in word_list:
                self.add_word_to_histogram(word)
        
    
    def build_from_file(self, filename):
        with open(filename, 'r') as f:
            text_body = f.read()

            replace_new_lines = text_body.replace("\n", '')
            prunned_text_body = replace_new_lines.strip(",. ")
            word_list = prunned_text_body.split(" ")

            for index in range(len(word_list)):
                word = word_list[index].lower()
                word_list[index] = word
            for word in word_list:
                if word == ' ':
                    word_list.remove(word)
                    continue
                self.add_word_to_histogram(word)
            return self


    def add_word_to_histogram(self, word):
        if word not in self:
            self[word] = 1
            self.types += 1
            self.tokens += 1           
        else:
            self[word] += 1
            self.tokens += 1

    def frequency(self, word):
        if word not in self:
            raise ValueError(f"{word} wasn't found")
        else:
            return self.get(word)


if __name__ == "__main__":
    dicto = Dictogram()
    histo = dicto.build_from_file(sys.argv[1])
    # word_list = word_list.build_from_file(sys.argv[1])
    # histArr = dicto.histogram(wordList)
    print(histo.frequency("and"))

    # print(f"Histogram : {histArr}")
    # print("Histogram :" + str(listo.unique_words))
    # print("Unique words:" + str(listo.uniqueTypes))
    # print("# of 'The':" + str(frequency(arr, "the")))
    # print("# of 'And':" + str(frequency(arr, "and")))    
