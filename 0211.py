"""
211. Design Add and Search Words Data Structure
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example1:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""

"""
Note:
1. Using Hash Table as base:
{wordLength: {"bad", "dad", "mad"}}

addWord: O(1) time | O(1) space
search: O(L*W) time | O(1) space
Total Space Complexity: O(L*W)
where L is the number of words in the dictionary
where W is the longest word length in the dictionary

2. Using Trie as base: 
addWord: O(w) time | O(1) space
search: O(n) time | O(w) space
Total Space Complexity: O(n)
where w is the length of the given word
where n is sum of lengths of all words in our Trie
"""
from collections import defaultdict
class WordDictionary:
    def __init__(self) -> None:
        self.lookup = defaultdict(set)

    def addWord(self, word: str) -> None:
        length = len(word)
        self.lookup[length].add(word)

    def search(self, word: str) -> bool:
        length = len(word)
        if length not in self.lookup:
            return False
        for item in self.lookup[length]:
            matched = False
            for i in range(length):
                if word[i] == item[i] or word[i] == ".":
                    matched = True
                else:
                    matched = False
                    break
            if matched:
                return True
        return matched

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary2:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        result = [False]
        self.dfs(node, word, 0, result)
        return result[0]

    def dfs(self, node, word, i, result):
        if result[0]:
            return
        if i == len(word):
            if node.isWord:
                result[0] = True
            return
        if word[i] == ".":
            for child in node.children.values():
                self.dfs(child, word, i + 1, result)
        else:
            child = node.children.get(word[i])
            if not child:
                return
            self.dfs(child, word, i + 1, result)

# Unit Tests
import unittest

classes = [WordDictionary, WordDictionary2]

class TestWordDictionary(unittest.TestCase):
    def testWordDictionary1(self):
        for myclass in classes:
            wordDictionary = myclass()
            wordDictionary.addWord("bad")
            wordDictionary.addWord("dad")
            wordDictionary.addWord("mad")
            self.assertEqual( wordDictionary.search("pad"), False)
            self.assertEqual( wordDictionary.search("bad"), True)
            self.assertEqual( wordDictionary.search(".ad"), True)
            self.assertEqual( wordDictionary.search("b.."), True)
        

if __name__ == "__main__":
    unittest.main()