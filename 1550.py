"""
1550. Three Consecutive Odds
description: https://leetcode.com/problems/three-consecutive-odds/description/
"""

"""
Note:
1. Brute-Force: O(n) time | O(1) space
"""

from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0
        for num in arr:
            if num % 2 == 0:
                oddCount = 0
            else:
                oddCount += 1

            if oddCount == 3:
                return True

        return False

# Unit Tests
import unittest
funcs = [Solution().threeConsecutiveOdds]
class TestThreeConsecutiveOdds(unittest.TestCase):
    def testThreeConsecutiveOdds1(self):
        for threeConsecutiveOdds in funcs:
            arr = [2,6,4,1]
            self.assertEqual(threeConsecutiveOdds(arr=arr), False)

    def testThreeConsecutiveOdds2(self):
        for threeConsecutiveOdds in funcs:
            arr = [1,2,34,3,4,5,7,23,12]
            self.assertEqual(threeConsecutiveOdds(arr=arr), True)

if __name__ == "__main__":
    unittest.main()
