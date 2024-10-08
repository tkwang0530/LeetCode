"""
1963. Minimum Number of Swaps to Make the String Balanced
description: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
"""

"""
Note:
1. Two Pointers: O(n) time | O(n) space - where n is the length of string s
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        L, R = 0, len(s)-1
        leftOpens = rightCloses = 0
        chars = list(s)

        swaps = 0
        while L < R:
            while L < R and (chars[L] == "[" or (chars[L] == "]" and leftOpens > 0)):
                leftOpens -= chars[L] == "]"
                leftOpens += chars[L] == "["
                L += 1
            while L < R and (chars[R] == "]" or (chars[R] == "[" and rightCloses > 0)):
                rightCloses -= chars[R] == "["
                rightCloses += chars[R] == "]"
                R -= 1
            
            if L != R:
                swaps += 1
                chars[L], chars[R] = chars[R], chars[L]
        return swaps

# Unit Tests
import unittest
funcs = [Solution().minSwaps]

class TestMinSwaps(unittest.TestCase):
    def testMinSwaps1(self):
        for func in funcs:
            s = "][]["
            self.assertEqual(func(s=s), 1)

    def testMinSwaps2(self):
        for func in funcs:
            s = "]]][[["
            self.assertEqual(func(s=s), 2)

    def testMinSwaps3(self):
        for func in funcs:
            s = "[]"
            self.assertEqual(func(s=s), 0)

if __name__ == "__main__":
    unittest.main()
