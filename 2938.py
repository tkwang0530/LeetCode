"""
2938. Separate Black and White Balls
description: https://leetcode.com/problems/separate-black-and-white-balls/description/
"""

"""
Note:
1. Two Pointers: O(n) time | O(1) space - where n is the length of string s
"""

class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        L, R = 0, len(s)-1

        while L < R:
            while L < R and s[R] == "1":
                R -= 1

            while L < R and s[L] == "0":
                L += 1

            if L < R:
                steps += R-L

            R -= 1
            L += 1
        return steps

funcs = [Solution().minimumSteps]

import unittest
class TestMinimumSteps(unittest.TestCase):
    def testMinimumSteps1(self):
        for func in funcs:
            s = "101"
            self.assertEqual(func(s=s), 1)

    def testMinimumSteps2(self):
        for func in funcs:
            s = "100"
            self.assertEqual(func(s=s), 2)

    def testMinimumSteps3(self):
        for func in funcs:
            s = "0111"
            self.assertEqual(func(s=s), 0)


if __name__ == "__main__":
    unittest.main()
