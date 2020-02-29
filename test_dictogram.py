from dictogramClass import Dictogram
import unittest

# # known inputs and their expected results
# fish_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
# fish_dict = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}/
class DictogramTest(unittest.TestCase):
    def test_init(self):
        dicto = Dictogram()
        assert dicto.tokens is 0
        assert dicto.types is 0 

    def test_build_from_file(self):
        dicto = Dictogram()
        dicto.build_from_file("text.txt")
        assert dicto.tokens is 8
        assert dicto.types is 5

    def test_add_word_to_histogram(self):
        dicto = Dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
        assert dicto.tokens is 8
        assert dicto.types is 5

    def test_frequency(self):
        dicto = Dictogram(['one', 'fish', 'two', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
        assert dicto.frequency("one") is 1
        assert dicto.frequency("two") is 2
        assert dicto.frequency("red") is 1
        assert dicto.frequency("blue") is 1
        assert dicto.frequency("fish") is 4
        with self.assertRaises(ValueError): 
            dicto.frequency("stuff")
            dicto.frequency("things")

if __name__ == '__main__':
    unittest.main()