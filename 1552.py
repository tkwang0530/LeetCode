"""
1552. Magnetic Force Between Two Balls
description: https://leetcode.com/problems/magnetic-force-between-two-balls/description/
"""

"""
Note:
1. Binary Search: O(plogp + plogR) time | O(sort) space - where p is the length of array position and R is the range of position[i]
"""

from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def condition(mid) -> bool:
            currentM = m
            previous = float("inf")
            for p in position:
                if abs(p-previous) >= mid:
                    previous = p
                    currentM -= 1
                if currentM == 0:
                    return True
            return False

        left, right = 1, 10**9
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1

# Unit Tests
import unittest
funcs = [Solution().maxDistance]
class TestMaxDistance(unittest.TestCase):
    def testMaxDistance1(self):
        for maxDistance in funcs:
            position = [1,2,3,4,7]
            m = 3
            self.assertEqual(maxDistance(position=position, m=m), 3)

    def testMaxDistance2(self):
        for maxDistance in funcs:
            position = [5,4,3,2,1,1000000000]
            m = 2
            self.assertEqual(maxDistance(position=position, m=m), 999999999)

if __name__ == "__main__":
    unittest.main()
