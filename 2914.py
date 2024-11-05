"""
2914. Minimum Number of Changes to Make Binary String Beautiful
description: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/
"""

"""
Note:
1. Greedy: O(n) time | O(1) space - where n is the length of string s
2. dp: O(4n) time | O(4n) space - where n is the length of string s
"""

import collections
class Solution:
    def minChanges(self, s: str) -> int:
        minChanges = 0
        for i in range(1, len(s), 2):
            if s[i] != s[i-1]:
                minChanges += 1
        return minChanges

class Solution2:
    def minChanges(self, s: str) -> int:
        n = len(s)
        dp = collections.defaultdict(lambda: float("inf"))
        dp[(n, "0", True)] = 0
        dp[(n, "1", True)] = 0
        for i in range(n-1, -1, -1):
            for prev, hasEven in [("0", True), ("0", False), ("1", True), ("1", False)]:
                minRemove = float("inf")
                if hasEven:
                    minRemove = min(minRemove, dp[(i+1, s[i], False)])
                else:
                    if s[i] == prev:
                        minRemove = min(minRemove, dp[(i+1, s[i], True)])
                    else:
                        # change to 0 or 1
                        minRemove = min(minRemove, 1+dp[(i+1, "0", True)])
                        minRemove = min(minRemove, 1+dp[(i+1, "1", True)])
                dp[(i, prev, hasEven)] = minRemove
        return dp[(0, "0", True)]

# Unit Tests
import unittest
funcs = [Solution().minChanges, Solution2().minChanges]

class TestMinChanges(unittest.TestCase):
    def testMinChanges1(self):
        for func in funcs:
            s = "1001"
            self.assertEqual(func(s=s), 2)

    def testMinChanges2(self):
        for func in funcs:
            s = "10"
            self.assertEqual(func(s=s), 1)

    def testMinChanges3(self):
        for func in funcs:
            s = "0000"
            self.assertEqual(func(s=s), 0)

if __name__ == "__main__":
    unittest.main()
