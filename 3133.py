"""
3133. Minimum Array End
description: https://leetcode.com/problems/minimum-array-end/description/ 
"""

"""
Note:
1. bitwise operation: O(logn) time | O(1) space
ref: https://www.youtube.com/watch?v=4pP-0UpEok4
"""

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        candidate = x
        i_x = 1
        i_n = 1 # for n-1
        while i_n <= n-1:
            if i_x & x == 0:
                if i_n & (n-1):
                    candidate = candidate | i_x
                i_n = i_n << 1
            i_x = i_x << 1
        return candidate

import unittest
funcs = [Solution().minEnd]

class TestMinEnd(unittest.TestCase):
    def testMinEnd1(self):
        for func in funcs:
            n = 3
            x = 4
            self.assertEqual(func(n=n, x=x), 6)

    def testMinEnd2(self):
        for func in funcs:
            n = 2
            x = 7
            self.assertEqual(func(n=n, x=x), 15) 

if __name__ == "__main__":
    unittest.main()
