"""
140. Word Break II
description: https://leetcode.com/problems/word-break-ii/description/
"""

"""
Note:
1. backtrack: O(2^n * n) time | O(ans) space - where n is the length of s and ans is the number of valid sentences
"""


import unittest
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordMap = set(wordDict)
        
        current = []
        output = []
        def backtrack(i):
            if i == n:
                output.append(" ".join(current))
                return
            
            for j in range(i+1, n+1):
                word = s[i:j]
                if word in wordMap:
                    current.append(word)
                    backtrack(j)
                    current.pop()
        backtrack(0)
        return output

# Unit Tests
funcs = [Solution().wordBreak]


class TestWordBreak(unittest.TestCase):
    def testWordBreak1(self):
        for func in funcs:
            s = "catsanddog"
            wordDict = ["cat","cats","and","sand","dog"]
            self.assertEqual(
                sorted(func(s=s, wordDict=wordDict)),
                sorted(["cats and dog","cat sand dog"]),
            )

    def testWordBreak2(self):
        for func in funcs:
            s = "pineapplepenapple"
            wordDict = ["apple","pen","applepen","pine","pineapple"]
            self.assertEqual(
                sorted(func(s=s, wordDict=wordDict)),
                sorted(["pine apple pen apple","pineapple pen apple","pine applepen apple"]),
            )

    def testWordBreak3(self):
        for func in funcs:
            s = "catsandog"
            wordDict = ["cats","dog","sand","and","cat"]
            self.assertEqual(
                sorted(func(s=s, wordDict=wordDict)),
                sorted([]),
            )

if __name__ == "__main__":
    unittest.main()
