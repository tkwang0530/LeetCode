"""
1268. Search Suggestion System
description: https://leetcode.com/problems/search-suggestions-system/description/
"""

""" 
1. Trie + DFS (Backtracking): O(nwk) time | O(3k) space - where n is len(products), w is the average length of products[i], and k is the len(searchWord)
2. Binary Search: O(k * (k+2wlogn)) time | O(3k) space - where n is len(products), w is the average length of products[i], and k is the len(searchWord)
"""
import bisect
from typing import List

class Node:
    def __init__(self, char):
        self.char = char
        self.isWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node("")

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.isWord = True
    
    def find(self, node, prefixChars, result):
        self.dfs(node, result, prefixChars)
    
    def dfs(self, node, result, path):
        if len(result) == 3:
            return
        if len(result) < 3 and node.isWord:
            result.append("".join(path))

        for i in range(26):
            char  = chr(ord("a")+i)
            if char not in node.children:
                continue
            child = node.children[char]
            path.append(char)
            self.dfs(child, result, path)
            path.pop()

class Solution(object):
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.addWord(product)
        
        ans = [[] for _ in range(len(searchWord))]
        prefixChars = []
        node = trie.root
        for i, char in enumerate(searchWord):
            result = []
            prefixChars.append(char)
            if char not in node.children:
                return ans
            node = node.children[char]
            trie.find(node, prefixChars, result)
            ans[i] = result
        return ans

class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        output = []
        prefix = ""
        afterZ = chr(ord("z")+1)
        for char in searchWord:
            prefix += char
            rightBoundStr = prefix+afterZ
            leftIdx = bisect.bisect_left(products, prefix)
            rightIdx = bisect.bisect_left(products, rightBoundStr)
            output.append(products[leftIdx:min(rightIdx, leftIdx+3)])
        return output


# Unit Tests
import unittest
funcs = [Solution().suggestedProducts, Solution2().suggestedProducts]


class TestSuggestedProducts(unittest.TestCase):
    def testSuggestedProducts1(self):
        for func in funcs:
            products = ["mobile","mouse","moneypot","monitor","mousepad"]
            searchWord = "mouse"
            output = [
                ["mobile","moneypot","monitor"],
                ["mobile","moneypot","monitor"],
                ["mouse","mousepad"],
                ["mouse","mousepad"],
                ["mouse","mousepad"]
            ]
            self.assertEqual(func(products=products, searchWord=searchWord), output)

    def testSuggestedProducts2(self):
        for func in funcs:
            products = ["havana"]
            searchWord = "havana"
            output = [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
            self.assertEqual(func(products=products, searchWord=searchWord), output)

    def testSuggestedProducts3(self):
        for func in funcs:
            products = ["bags","baggage","banner","box","cloths"]
            searchWord = "bags"
            output = [
                ["baggage","bags","banner"],
                ["baggage","bags","banner"],
                ["baggage","bags"],
                ["bags"]
            ]
            self.assertEqual(func(products=products, searchWord=searchWord), output)

if __name__ == "__main__":
    unittest.main()
