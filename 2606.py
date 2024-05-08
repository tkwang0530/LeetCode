"""
2606. Find the Substring With Maximum Cost
description: https://leetcode.com/problems/find-the-substring-with-maximum-cost/description/
"""

"""
Notes:
1. prefixSum + suffixMax: O(n) time | O(n) space - where n is the length of s
2. Kadane's algorithm: O(n) time | O(1) space - where n is the length of s
"""

from typing import List

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        charVal = {char: 1+ord(char)-ord('a') for i, char in enumerate(alphabets)}
        for i in range(len(chars)):
            charVal[chars[i]] = vals[i]
        
        n = len(s)
        prefixSum = [0] *  n
        for i in range(n):
            if i == 0:
                prefixSum[i] = charVal[s[i]]
            else:
                prefixSum[i] = prefixSum[i-1] + charVal[s[i]]

        suffixMax = [-float("inf")] * n
        for i in range(n-1, -1, -1):
            if i == n-1:
                suffixMax[i] = prefixSum[i]
            else:
                suffixMax[i] = max(suffixMax[i+1], prefixSum[i])
        
        maxCost = 0
        for i in range(n):
            startVal = charVal[s[i]]
            maxCost = max(maxCost, suffixMax[i]-(prefixSum[i]-startVal))
        return maxCost

class Solution2:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        charVal = {char: 1+ord(char)-ord('a') for i, char in enumerate(alphabets)}
        for i in range(len(chars)):
            charVal[chars[i]] = vals[i]
        
        maxCost = current = 0
        for char in s:
            current = max(current+charVal[char], 0)
            maxCost = max(maxCost, current)
        return maxCost

# Unit Tests
import unittest
funcs = [Solution().maximumCostSubstring, Solution2().maximumCostSubstring]

class TestMaximumCostSubstring(unittest.TestCase):
    def testMaximumCostSubstring1(self):
        for func in funcs:
            s = "adaa"
            chars = "d"
            vals = [-1000]
            self.assertEqual(func(s=s, chars=chars, vals=vals), 2)

    def testMaximumCostSubstring2(self):
        for func in funcs:
            s = "abc"
            chars = "abc"
            vals = [-1,-1,-1]
            self.assertEqual(func(s=s, chars=chars, vals=vals), 0)

if __name__ == "__main__":
    unittest.main()