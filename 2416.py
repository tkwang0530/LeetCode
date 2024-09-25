"""
2416. Sum of Prefix Scores of Strings
description: https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/ 
"""

"""
Note:
1. Trie: O(n*w) time | O(n*w) space - where n is the length of array words and w is the average length of words[i]
"""

import collections
from typing import List

class Node:
    def __init__(self):
        self.val = 0
        self.children = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        current = self.root
        for char in word:
            current.children[char].val += 1
            current = current.children[char]

    
    def search(self, word: str) -> int:
        current = self.root
        score = 0
        for char in word:
            score += current.children[char].val
            current = current.children[char]
        
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        n = len(words)
        output = [0] * n
        trie = Trie()
        for word in words:
            trie.insert(word)

        for i, word in enumerate(words):
            output[i] = trie.search(word)

        return output

funcs = [Solution().sumPrefixScores]

import unittest
class TestSumPrefixScores(unittest.TestCase):
    def testSumPrefixScores1(self):
        for func in funcs:
            words = ["abc","ab","bc","b"]
            self.assertEqual(func(words=words), [5,4,3,2])

    def testSumPrefixScores2(self):
        for func in funcs:
            words = ["abcd"]
            self.assertEqual(func(words=words), [4])

if __name__ == "__main__":
    unittest.main()
