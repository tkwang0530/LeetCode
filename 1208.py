"""
1208. Get Equal Substrings Within Budget
description: https://leetcode.com/problems/get-equal-substrings-within-budget/description/
"""

"""
Note:
1. Sliding Window: O(n) time | O(1) space - where n is the length of string s
"""




import unittest
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currentCost = 0
        start = 0
        maxLen = 0
        for end in range(len(s)):
            currentCost += abs(ord(s[end])-ord(t[end]))
            while currentCost > maxCost:
                currentCost -= abs(ord(s[start])-ord(t[start]))
                start += 1
            maxLen = max(maxLen, end-start+1)
        return maxLen


# Unit Tests
funcs = [Solution().equalSubstring]


class TestEqualSubstring(unittest.TestCase):
    def testEqualSubstring1(self):
        for func in funcs:
            s = "abcd"
            t = "bcdf"
            maxCost = 3
            self.assertEqual(func(s=s, t=t, maxCost=maxCost), 3)

    def testEqualSubstring2(self):
        for func in funcs:
            s = "abcd"
            t = "cdef"
            maxCost = 3
            self.assertEqual(func(s=s, t=t, maxCost=maxCost), 1)

    def testEqualSubstring3(self):
        for func in funcs:
            s = "abcd"
            t = "acde"
            maxCost = 0
            self.assertEqual(func(s=s, t=t, maxCost=maxCost), 1)


if __name__ == "__main__":
    unittest.main()
