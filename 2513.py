"""
2513. Minimize the Maximum of Two Arrays
description: https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/description/
"""

"""
Note:
1. binary search: O(log10**10) time | O(1) space
"""

import functools
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        @functools.lru_cache(None)
        def gcd(d1, d2):
            if d1 == 0:
                return d2
            if d2 == 0:
                return d1
    
            if d1 > d2:
                return gcd(d1 % d2, d2)
            else:
                return gcd(d1, d2 % d1)

        def lcm(d1, d2):
            return d1*d2//gcd(d1, d2)

        left, right = 1, 10**10+1
        mininumMax = float("inf")

        def condition(n):
            dn1 = n // divisor1 # divisor1 的倍數個數
            dn2 = n // divisor2 # divisor2 的倍數個數
            return n - dn1 >= uniqueCnt1 and n - dn2 >= uniqueCnt2 and  n - n//lcm(divisor1, divisor2) >= (uniqueCnt1+uniqueCnt2)

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
                mininumMax = mid
            else:
                left = mid+1
        return mininumMax

# Unit Tests
import unittest
funcs = [Solution().minimizeSet]
class TestMinimizeSet(unittest.TestCase):
    def testMinimizeSet1(self):
        for func in funcs:
            divisor1 = 2
            divisor2 = 7
            uniqueCnt1 = 1
            uniqueCnt2 = 3
            self.assertEqual(func(divisor1=divisor1, divisor2=divisor2, uniqueCnt1=uniqueCnt1, uniqueCnt2=uniqueCnt2), 4)

    def testMinimizeSet2(self):
        for func in funcs:
            divisor1 = 3
            divisor2 = 5
            uniqueCnt1 = 2
            uniqueCnt2 = 1
            self.assertEqual(func(divisor1=divisor1, divisor2=divisor2, uniqueCnt1=uniqueCnt1, uniqueCnt2=uniqueCnt2), 3)

    def testMinimizeSet3(self):
        for func in funcs:
            divisor1 = 2
            divisor2 = 4
            uniqueCnt1 = 8
            uniqueCnt2 = 2
            self.assertEqual(func(divisor1=divisor1, divisor2=divisor2, uniqueCnt1=uniqueCnt1, uniqueCnt2=uniqueCnt2), 15)

if __name__ == "__main__":
    unittest.main()
