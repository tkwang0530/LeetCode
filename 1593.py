"""
1593. Split a String Into the Max Number of Unique Substrings
description: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/ 
"""

"""
Note:
1. backtracking + HashSet: O(2^n*n^2) time | O(2^n * n) space - where n is the length of string s
"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        subStrSet = set()
        n = len(s)
        maxSplit = 0
        def backtrack(i):
            nonlocal maxSplit
            if i == n:
                maxSplit = max(maxSplit, len(subStrSet))
                return

            for end in range(i+1, n+1):
                subStr = s[i:end]
                if subStr not in subStrSet:
                    subStrSet.add(subStr)
                    backtrack(end)
                    subStrSet.remove(subStr)
        
        backtrack(0)
        return maxSplit

funcs = [Solution().maxUniqueSplit]

import unittest
class TestMaxUniqueSplit(unittest.TestCase):
    def testMaxUniqueSplit1(self):
        for func in funcs:
            s = "ababccc"
            self.assertEqual(func(s=s), 5)

    def testMaxUniqueSplit2(self):
        for func in funcs:
            s = "aba"
            self.assertEqual(func(s=s), 2)

    def testMaxUniqueSplit3(self):
        for func in funcs:
            s = "aa"
            self.assertEqual(func(s=s), 1)

if __name__ == "__main__":
    unittest.main()
