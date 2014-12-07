""" Basic submission tests for Trie class (PA5).

Fall 2014
"""

import unittest

from trie import Trie

class TrieBasicTester(unittest.TestCase):

    def test_basic(self):
        trie = Trie()
        trie.insert("cat")
        self.assertEqual(trie.__len__(), 1)
        self.assertTrue(trie.__contains__("cat"))
        self.assertEqual([x for x in trie.__iter__()], ["cat"])
        self.assertTrue(trie.contains_prefix("ca"))
        self.assertEqual([x for x in trie.prefix_iter("ca")], ["cat"])

if __name__ == "__main__":
    unittest.main()
