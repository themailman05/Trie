from trie import Trie


Trie = Trie()
Trie.insert("Hello")
Trie.insert("Her")
Trie.insert("PaulaDeen")
Trie.insert("Hemlock")
for item in Trie:
    print(item)