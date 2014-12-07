__author__ = 'liam'

import unittest
from trie import Trie
import auto_complete


class TrieTester(unittest.TestCase):

    def setUp(self):
        self.Trie = Trie()

    def test_simple_insert(self):
        self.Trie.insert("hel")
        self.Trie.insert("hello")
        self.assertTrue("hello" in self.Trie)

    def test_contains_prefix(self):
        self.Trie.insert("Hello")
        self.assertTrue(self.Trie.contains_prefix("Hel"))



    """
    def test_dictionary_insert(self):
        with open('american-english.txt', 'r') as f:
            for line in f:
                self.Trie.insert(line.rstrip())
    """

if __name__ == '__main__':
    unittest.main()
