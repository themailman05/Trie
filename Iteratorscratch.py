from trie import Trie


Trie = Trie()
Trie.insert("PaulaDeen")
Trie.insert("Hemlock")
Trie.insert("Hello")
Trie.insert("Ball")
for item in Trie:
    print(item)