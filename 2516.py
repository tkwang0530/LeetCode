"""
2516. Take K of Each Character From Left and Right
description: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/
"""

"""
Note:
1. Sliding Window + HashTable: O(n) time | O(1) space - where n is the length of string s 
"""

import collections
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)

        limits = collections.defaultdict(int)
        counter = collections.Counter(s)
        for char in "abc":
            limits[char] = counter[char] - k

        if any([limits[char] < 0 for char in "abc"]):
            return -1
         
        keep = 0
        runningCounter = collections.defaultdict(int)
        L = 0
        for R in range(n):
            c = s[R]
            runningCounter[c] += 1
            while runningCounter[c] > limits[c]:
                runningCounter[s[L]] -= 1
                L += 1
            
            keep = max(keep, R-L+1)
        return n-keep

import unittest
funcs = [Solution().takeCharacters]

class TestTakeCharacters(unittest.TestCase):
    def testTakeCharacters1(self):
        for func in funcs:
            s = "aabaaaacaabc"
            k = 2
            self.assertEqual(func(s=s, k=k), 8)

    def testTakeCharacters2(self):
        for func in funcs:
            s = "a"
            k = 1
            self.assertEqual(func(s=s, k=k), -1) 

if __name__ == "__main__":
    unittest.main()
