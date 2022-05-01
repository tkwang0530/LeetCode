"""
1268. Search Suggestion System
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example3:
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Constraints:
1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 10^4
All the strings of products are unique.
products[i] consist of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
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

    def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prevPrefix = ""
        ans = []
        for i in range(len(searchWord)):
            prefix = prevPrefix + searchWord[i]
            first = bisect.bisect_left(products, prefix)

            last = bisect.bisect_left(products, prevPrefix+chr(ord(searchWord[i])+1), first)
            if first == last:
                ans.append([])
            else:
                ans.append(products[first:min(last, first+3)])
            prevPrefix = prefix
        return ans


# Unit Tests
import unittest
funcs = [Solution().suggestedProducts, Solution().suggestedProducts2]


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
