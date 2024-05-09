"""
1005. Maximize Sum Of Array After K Negations
description: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
"""

"""
Note:
1. maxHeap: O(nlog(min(k, n))) time | O(min(k, n)) space - where n is the length of array nums
"""

import unittest, heapq
from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        maxHeap = []
        containsZero = False
        for i, num in enumerate(nums):
            if num == 0:
                containsZero = True
            if num >= 0:
                continue                

            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-num, i))
            else:
                heapq.heappushpop(maxHeap, (-num, i))
        
        flips = len(maxHeap)
        for _, idx in maxHeap:
            nums[idx] *= -1

        total = sum(nums)
        if (k-flips) % 2 > 0 and not containsZero:
            total -= 2 * min(nums)
        return total

# Unit Tests
funcs = [Solution().largestSumAfterKNegations]


class TestLargestSumAfterKNegations(unittest.TestCase):
    def testLargestSumAfterKNegations1(self):
        for func in funcs:
            nums = [4,2,3]
            k = 1
            self.assertEqual(func(nums=nums, k=k), 5)

    def testLargestSumAfterKNegations2(self):
        for func in funcs:
            nums = [3,-1,0,2]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 6)

    def testLargestSumAfterKNegations3(self):
        for func in funcs:
            nums = [2,-3,-1,5,-4]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 13)

if __name__ == "__main__":
    unittest.main()
