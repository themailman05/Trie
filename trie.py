#! /usr/bin/env python

""" This module contains a trie data structure, used for spell checking
and auto-completion.

Implemented for CS240 by Liam Sargent, December 2014


This Submission complies with the JMU Honor Code.
All code was written by the submitter, and no unauthorized assistance
was used while completing this assignment.

"""
from collections import deque

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
        self._root = self._Node(None, False)
        self._size = 0

    def __len__(self):
        """Return the number of words stored in this Trie"""
        return self._size

    def __contains__(self, word):
        """Return True if the word is in the Trie, False otherwise."""
        word = word.lower()
        intrie = True
        cur = self._root
        for ii in range(len(word)):
            letter = word[ii]
            if letter in cur.outgoing:
                cur = cur.outgoing[letter]
            else:
                intrie = False
                break
        if not cur.isword:
            intrie = False
        return intrie

    def __iter__(self):
        """
        Return an iterator that will allow iteration of all words in
        the Trie in lexicographical order
        """
        root = self._root
        if len(self) > 0:
            for node in self._recurse_helper("", root):
                yield node

    def _recurse_helper(self, wordchunk, node):
        """
        recursive helper method for traversing the trie in alphabetical
        order.
        """
        if node.isword:
            yield wordchunk
        for letter in sorted(node.outgoing):
            for word in self._recurse_helper(str(wordchunk)+str(letter),
                                             node.outgoing[letter]):
                yield word


    def insert(self, word):
        """
        Insert the indicated word into the Trie. This method has no
        effect if the word is already in the Trie.
        No Return value.
        """
        word = word.lower()
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
        """Return True if the word is in the Trie, False otherwise."""
        word = prefix.lower()
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

    def prefix_iter(self, prefix):
        """
        Return an iterator that will allow iteration over all of
        the words in the Trie that have the indicated prefix, in
        lexicographical order.
        """
        cur = self._root
        pref = prefix.lower()
        for ii in range(len(pref)):
            letter = pref[ii]
            if letter in cur.outgoing:
                cur = cur.outgoing[letter]
        for node in self._recurse_helper(pref, cur):
                yield node
