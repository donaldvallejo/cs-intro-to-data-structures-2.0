from dictogramClass import Dictogram
from sample import * 

class MarkovChain:

    def __init__(self, word_list):
        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
         self.markov_chain = self.build_markov(word_list)
         self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys(): #already there
                #get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                #add to count
                histogram[next_word] = histogram.get(next_word, 0) + 1
            else: #first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        # TODO: generate a sentence num_words long using the markov chain
        all_keys = []
        words_for_sentence = []
        new_sentence = ''

        word = self.first_word
        for i in range(num_words):
            '''for index, keys in enumerate(dictogram):
                all_keys.append(keys)
            
            random_set = random.choice(all_keys)
            if random_set is not None:
                words_for_sentence.append(random_set[0])
                words_for_sentence.append(random_set[1])
                words_for_sentence.append(random_set[2])
        
                get_next_set = dictogram[random_set]

        for word in words_for_sentence:
            new_sentence += word + " "'''
            new_sentence += word + " "
            dictogram = self.markov_chain[word]
            word = dictogram.sample()
        
        return new_sentence
    
    def main():
        sample = 'I like cats. I love dogs. I hate mr.max nasty food. Although I love love food.'
        with open( 'corpus.txt', "r") as f:
            data = f.read()
            # words_list = data.split()
            content = re.sub('[^a-zA-Z0-9 \n\.]', '', data)
            sample = data.split(' ')
            dict = markov_chain(sample)
            # print(dict)
            gen = generate_sentence(dict, 4)
            return gen

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram)

    

markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))