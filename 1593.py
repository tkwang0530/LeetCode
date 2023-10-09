"""
1593. Split a String Into the Max Number of Unique Substrings
description: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/
"""

"""
Note:
1. Backtracking: O(2^n * n) time | O(n) space - where n is the length of string s
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        def dfs(i, uniqueStrSet):
            if i == n:
                return 0

            maxUniques = 0
            for j in range(i+1, n+1):
                currentStr = s[i:j]
                if currentStr in uniqueStrSet:
                    continue
                uniqueStrSet.add(currentStr)
                maxUniques = max(maxUniques, 1 + dfs(j, uniqueStrSet))
                uniqueStrSet.remove(currentStr)
            return maxUniques
        
        uniqueStrSet = set()
        return dfs(0, uniqueStrSet)

# Unit Tests
import unittest
funcs = [Solution().maxUniqueSplit]

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