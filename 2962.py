"""
2962. Count Subarrays Where Max Element Appears at Least K Times
description: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description
"""

"""
Note:
1. queue: O(n) time | O(k) space - where n is the length of array nums
"""

import unittest, collections
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxNum = max(nums)
        valids = 0
        queue = collections.deque()
        for i, num in enumerate(nums):
            if num == maxNum:
                queue.append(i)
            
            if len(queue) > k:
                queue.popleft()
            if len(queue) == k:
                valids += queue[0]+1
                
        return valids

# Unit Tests
import unittest
funcs = [Solution().countSubarrays]
class TestCountSubarrays(unittest.TestCase):
    def testCountSubarrays1(self):
        for func in funcs:
            nums = [1,3,2,3,3]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 6)

    def testCountSubarrays2(self):
        for func in funcs:
            nums = [1,4,2,1]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 0)

if __name__ == "__main__":
    unittest.main()
