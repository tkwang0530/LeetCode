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
1. Using HashMap: O(n) time | O(1) space
{wordLength: ["bad", "dad", "mad"]}
"""

class WordDictionary:
    def __init__(self) -> None:
        self.lookup = {}

    def addWord(self, word: str) -> None:
        length = len(word)
        if length not in self.lookup:
            self.lookup[length] = [word]
        else:
            self.lookup[length].append(word)

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


# Unit Tests
import unittest

class TestWordDictionary(unittest.TestCase):
    def testWordDictionary1(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        self.assertEqual( wordDictionary.search("pad"), False)
        self.assertEqual( wordDictionary.search("bad"), True)
        self.assertEqual( wordDictionary.search(".ad"), True)
        self.assertEqual( wordDictionary.search("b.."), True)
        

if __name__ == "__main__":
    unittest.main()