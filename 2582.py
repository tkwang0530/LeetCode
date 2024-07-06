"""
2582. Pass the Pillow
description: https://leetcode.com/problems/pass-the-pillow/description/
"""

"""
Note:
1. Math: O(1) time | O(1) space
"""

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        period = 2*(n-1)
        time %= period
        if time <= n-1:
            return time+1
        else:
            time -= n-1
            return n - time
        
# Unit Tests
import unittest
funcs = [Solution().passThePillow]

class TestPassThePillow(unittest.TestCase):
    def testPassThePillow(self):
        for passThePillow in funcs:
            n, time = 4, 5
            self.assertEqual(passThePillow(n=n, time=time), 2)

    def testPassThePillow2(self):
        for passThePillow in funcs:
            n, time = 3, 2
            self.assertEqual(passThePillow(n=n, time=time), 3)

if __name__ == "__main__":
    unittest.main()