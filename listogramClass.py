import sys
from random import randint
class Listogram:
    def __init__(self, word_list=None):
        '''Initializes the listogram properties'''
        super(Listogram, self).__init__()
        self.word_list = word_list
        self.listo = self.buildHistogram()
        self.uniqueTypes = self.unique_words()

    def buildHistogram(self):
        wordList = self.get_text(sys.argv[1])
        histo = self.histogram(wordList)
        return histo

    def histogram(self, wordsList):
        arr = []
        found = False
        for word in wordsList: 
            for j in arr:
                if j[0] == word:
                    found = True
                    j[1] += 1
                    break
            if not found:
                arr.append([word, 1])
        return arr

    def unique_words(self):
        return len(self.listo)   

    def frequency(self, arr, word):
        for j in arr:
            if j[0] == word:
                return j[1]
            else: 
                return None

    def get_text(self, filename):
        with open(filename, 'r') as f:
            data = f.read().splitlines()
        return data


if __name__ == "__main__":
    listo = Listogram()
    wordList = listo.get_text(sys.argv[1])
    histArr = listo.histogram(wordList)

    print(f"Histogram : {histArr}")
    # print("Histogram :" + str(listo.unique_words))
    # print("Unique words:" + str(listo.uniqueTypes))
    # print("# of 'The':" + str(frequency(arr, "the")))
    # print("# of 'And':" + str(frequency(arr, "and")))    
