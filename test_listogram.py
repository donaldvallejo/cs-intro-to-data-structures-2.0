from listogramClass import Listogram
import unittest

class ListogramTest(unittest.TestCase):
    def test_init(self):
        listo = Listogram()
        assert listo.word_list is None
        listo.buildHistogram()
        assert listo.listo == [["one", 1],["fish", 4],["two", 1],["red", 1],["blue", 1]]
        assert listo.types is 5
        
    def test_build_histogram(self):
        listo = Listogram()
        listo.buildHistogram()
        assert listo.listo == [["one", 1],["fish", 4],["two", 1],["red", 1],["blue", 1]]

    def test_histogram(self):
        listo = Listogram()
        assert listo.histogram(["one", "two", "red", "blue", "fish", "fish", "fish", "fish"]) == [["one", 1],["two", 1],["red", 1],["blue", 1], ["fish", 4]]
        assert listo.types == 5
