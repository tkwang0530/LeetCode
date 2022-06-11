"""
677. Map Sum Pairs
Design a map that allows you to do the following:
- MapSum() Initializes the MapSum object.
- void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
- int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Example1:
Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

Constraints:
1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase Englilsh letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
"""

"""
Note:
1. Trie + HashTable:
for all methods
O(n) time | O(1) space - where n is the length of string s
"""

import collections
class Node:
    def __init__(self, char, score=0):
        self.char = char
        self.score = score
        self.children = {}   

class MapSum:

    def __init__(self):
        self.root = Node("", 0)
        self.wordScores = collections.defaultdict(int)
        

    def insert(self, word: str, score: int) -> None:
        newScore = score
        if word in self.wordScores:
            score = score - self.wordScores[word]
        
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node(char, score)
            else:
                current.children[char].score += score
            current = current.children[char]
        
        self.wordScores[word] = newScore

    def sum(self, prefix: str) -> int:
        current = self.root
        for i, char in enumerate(prefix):
            if char not in current.children:
                return 0
            else:
                current = current.children[char]
        return current.score

# Unit Tests
import unittest
classes = [MapSum]

class TestMapSum(unittest.TestCase):
    def testMapSum1(self):
        for myclass in classes:
            mapSum = myclass()
            mapSum.insert("apple", 3)
            self.assertEqual(mapSum.sum("ap"), 3)
            mapSum.insert("app", 2)
            self.assertEqual(mapSum.sum("ap"), 5)

if __name__ == "__main__":
    unittest.main()
