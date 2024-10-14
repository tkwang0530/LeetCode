"""
2530. Maximal Score After Applying K Operations
description: https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/
"""

"""
Note:
1. maxHeap: O(n+klogn) time | O(n) space - where n is the length of array nums
"""

import heapq
import math
from typing import List
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        score = 0
        while k:
            negNum = heapq.heappop(maxHeap)
            num = -negNum
            score += num
            heapq.heappush(maxHeap, -1*math.ceil(num/3))
            k -= 1
        return score

funcs = [Solution().maxKelements]

import unittest
class TestMaxKelements(unittest.TestCase):
    def testMaxKelements1(self):
        for func in funcs:
            nums = [10,10,10,10,10]
            k = 5
            self.assertEqual(func(nums=nums, k=k), 50)

    def testMaxKelements2(self):
        for func in funcs:
            nums = [1,10,3,3,3]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 17)

if __name__ == "__main__":
    unittest.main()
