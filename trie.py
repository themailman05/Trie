#! /usr/bin/env python

""" This module contains a trie data structure, used for spell checking
and auto-completion.

Implemented for CS240 by Liam Sargent, December 2014


This Submission complies with the JMU Honor Code.
All code was written by the submitter, and no unauthorized assistance
was used while completing this assignment.

"""

class Trie:
    """Trie class that supports spell checking and auto-completion"""

    class _Node:
        """Underlying node class for each char in Trie"""

        def __init__(self, char, isword):
            self.char = char
            self.isword = isword
            self.outgoing = {}

    def __init__(self):
        """Create a new empty Trie."""
        self._root = self._Node(None, True)
        self._size = 0

    def __len__(self):
        """Return the number of words stored in this Trie"""
        return self._size

    def __contains__(self, word):
        """Return True if the word is in the Trie, False otherwise."""

        intrie = True
        cur = self._root
        for ii in range(len(word)):
            letter = word[ii]
            if letter in cur.outgoing:
                cur = cur.outgoing[letter]
            else:
                intrie = False
                break
        return intrie

    def __iter__(self):
        """
        Return an iterator that will allow iteration of all words in
        the Trie in lexicographical order
        """
        raise NotImplementedError

    def insert(self, word):
        """
        Insert the indicated word into the Trie. This method has no
        effect if the word is already in the Trie.
        No Return value.
        """
        if word not in self:
            cur = self._root
            for ii in range(len(word)):
                letter = word[ii]
                if letter not in cur.outgoing:
                    cur.outgoing[letter] = self._Node(letter, False)
                    cur = cur.outgoing[letter]
                elif letter in cur.outgoing:
                    cur = cur.outgoing[letter]
            cur.isword = True
            self._size += 1


    def contains_prefix(self, prefix):
        """
        Return True if the indicated string is a word in the Trie or
        is a prefix of any word in the Trie. Return False otherwise.
        """
        raise NotImplementedError

    def prefix_iter(self, prefix):
        """
        Return an iterator that will allow iteration over all of
        the words in the Trie that have the indicated prefix, in
        lexicographical order.
        """
        raise NotImplementedError