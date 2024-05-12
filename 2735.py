"""
2735. Collecting Chocolates
description: https://leetcode.com/problems/collecting-chocolates/description/
"""

"""
Note:
1. HashTable: O(n^2) time | O(n) space - where n is the length of array nums
hint: The array will be rotated for a max of N times, so try all possibilities as N = 1000.
"""

from typing import List
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        typeMinCost = {i: num for i, num in enumerate(nums)}
        minCost = runningCost = sum(nums)
        for shifts in range(1, n):
            runningCost += x
            for tp in range(n):
                if nums[(tp+shifts)%n] < typeMinCost[tp]:
                    runningCost -= (typeMinCost[tp] - nums[(tp+shifts)%n])
                    typeMinCost[tp] = nums[(tp+shifts)%n]
            
            minCost = min(minCost, runningCost)
        return minCost

# Unit Tests
import unittest
funcs = [Solution().minCost]


class TestMinCost(unittest.TestCase):
    def testMinCost1(self):
        for func in funcs:
            nums = [20,1,15]
            x = 5
            self.assertEqual(func(nums=nums, x=x), 13)

    def testMinCost2(self):
        for func in funcs:
            nums = [1,2,3]
            x = 4
            self.assertEqual(func(nums=nums, x=x), 6)


if __name__ == "__main__":
    unittest.main()