"""
2485. Find the Pivot Integer
description: https://leetcode.com/problems/find-the-pivot-integer/description
"""

"""
Note:
1. binary search: O(logn) time | O(1) space
"""

class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 1, n+1
        while left < right:
            mid = left + (right - left) // 2
            sumOneToMid = (1+mid)*mid//2
            sumOneToN = (1+n)*n//2
            sumMidToN = sumOneToN-sumOneToMid+mid
            if sumOneToMid == sumMidToN:
                return mid
            elif sumOneToMid > sumMidToN:
                right = mid
            else:
                left = mid + 1
        
        return -1

# Unit Tests
import unittest
funcs = [Solution().pivotInteger]
class TestPivotInteger(unittest.TestCase):
    def testPivotInteger1(self):
        for func in funcs:
            n = 1
            self.assertEqual(func(n=n), 1)

    def testPivotInteger2(self):
        for func in funcs:
            n = 8
            self.assertEqual(func(n=n), 6)

    def testPivotInteger3(self):
        for func in funcs:
            n = 4
            self.assertEqual(func(n=n), -1)

if __name__ == "__main__":
    unittest.main()
