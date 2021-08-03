"""
875. Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example2:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
"""

"""
Note:
1. Binary Search: O(nlog(maxP)) time | O(1) space
"""

from typing import List
import unittest, math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) + 1
        while left < right:
            mid = left + (right - left) // 2
            used = sum([math.ceil(pile / mid) for pile in piles])
            if used <= h: # can finish in time
                right = mid
            else:
                left = mid + 1
        return left



# Unit Tests
funcs = [Solution().minEatingSpeed]

class TestMinEatingSpeed(unittest.TestCase):
    def testMinEatingSpeed1(self):
        for func in funcs:
            piles = [3, 6, 7, 11]
            h = 8
            self.assertEqual(
                func(piles=piles, h=h), 4)
    
    def testMinEatingSpeed2(self):
        for func in funcs:
            piles = [30,11,23,4,20]
            h = 5
            self.assertEqual(
                func(piles=piles, h=h), 30)

    def testMinEatingSpeed3(self):
        for func in funcs:
            piles = [30,11,23,4,20]
            h = 6
            self.assertEqual(
                func(piles=piles, h=h), 23)


if __name__ == "__main__":
    unittest.main()
