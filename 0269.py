"""
269. Alien Dictionary
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Example1:
Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"

Example2:
Input: words = ["z", "x"]
Output: "zx"

Example3:
Input: words = ["z", "x", "z"]
Output: ""
Explanation: The order is invalid, so return "".
"""

"""
Note:
1. Recursive DFS (post order graph traversal): O(n) time | O(n) space
where n is the number of characters in the dictionary (including duplicates)
(1) use set as value because the duplication of char
(2) use post order traversal in dfs
(3) return the reverse version of the result we build during the graph traversal
"""

import unittest
from typing import List
class Solution(object):
    def alienOrder(self, words: List[str]) -> str:  # dfs
        graph = {}
        visiting = {}
        result = []

        # graph = { char: set() for word in words for char in word }
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
        
        # words[:-1] == words[:len(words) - 1]
        for word1, word2 in zip(words[:-1], words[1:]): 
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    graph[char1].add(char2)
                    break
            
        for node in graph:
            if self.dfs(node, graph, visiting, result):
                return ""
        return "".join(result[::-1])
    
    # return True if breaks rule (find loop in graph)
    def dfs(self, node, graph, visiting, result) -> bool:
        if node in visiting:
            return visiting[node]
        visiting[node] = True
        for neighbor in graph[node]:
            if self.dfs(neighbor, graph, visiting, result):
                return True
        visiting[node] = False
        result.append(node)
        return False



        
    
# Unit Tests
funcs = [Solution().alienOrder]


class TestAlienOrder(unittest.TestCase):
    def testAlienOrder1(self):
        for func in funcs:
            words = ["wrt", "wrf", "er", "ett", "rftt"]
            self.assertEqual(func(words=words), "wertf")

    def testAlienOrder2(self):
        for func in funcs:
            words = ["z", "x"]
            self.assertEqual(func(words=words), "zx")

    def testAlienOrder3(self):
        for func in funcs:
            words = ["z", "x", "z"]
            self.assertEqual(func(words=words), "")


if __name__ == "__main__":
    unittest.main()
