"""
1561. Maximum Number of Coins You Can Get
description: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/
"""

"""
Note:
1. Greedy: O(nlogn) time | O(sort) space - where n is the length of array piles
"""

from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        left = len(piles) // 3
        piles.sort(reverse=True)
        i = 1
        coins = 0
        while left > 0:
            coins += piles[i]
            i += 2
            left -= 1
        return coins

# Unit Tests
import unittest
funcs = [Solution().maxCoins]
class TestMaxCoins(unittest.TestCase):
    def testMaxCoins1(self):
        for maxCoins in funcs:
            piles = [2,4,1,2,7,8]
            self.assertEqual(maxCoins(piles=piles), 9)

    def testMaxCoins2(self):
        for maxCoins in funcs:
            piles = [2,4,5]
            self.assertEqual(maxCoins(piles=piles), 4)

    def testMaxCoins3(self):
        for maxCoins in funcs:
            piles = [9,8,7,6,5,1,2,3,4]
            self.assertEqual(maxCoins(piles=piles), 18)

if __name__ == "__main__":
    unittest.main()
