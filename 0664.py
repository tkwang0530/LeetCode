"""
664. Strange Printer
description: https://leetcode.com/problems/strange-printer/description/
"""

"""
Note:
1. dfs+memo: O(n^3) time | O(n^2) space - where n is the length of string s
ref: https://www.youtube.com/watch?v=YQQUGsb7mww
"""

import unittest, functools
class Solution:
    def strangePrinter(self, s: str) -> int:
        @functools.lru_cache(None)
        def turns(i, j):
            if i > j: return 0

            minOp = turns(i, j-1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    minOp = min(minOp, turns(i, k) + turns(k+1, j-1))
            return minOp

        return turns(0, len(s)-1)
# Unit Tests
funcs = [Solution().strangePrinter]

class TestStrangePrinter(unittest.TestCase):
    def testStrangePrinter1(self):
        for func in funcs:
            s = "aaabbb"
            self.assertEqual(func(s=s), 2)

    def testStrangePrinter2(self):
        for func in funcs:
            s = "aba"
            self.assertEqual(func(s=s), 2)



if __name__ == "__main__":
    unittest.main()
