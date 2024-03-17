"""
1696. Jump Game VI
description: https://leetcode.com/problems/jump-game-vi/description/
"""

"""
Note:
1. Monotonic queue: O(n) time | O(k) space - where n is the length of array nums
"""

import collections
from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = collections.deque() # [(index, dp value)]
        queue.append((0, nums[0]))
        for i in range(1, n):
            # maintain the queue size
            if queue and i - queue[0][0] > k:
                queue.popleft()

            
            dp = queue[0][1] + nums[i]
            while queue and dp >= queue[-1][1]:
                queue.pop()
            queue.append((i, dp))
        return queue[-1][1]


# Unit Tests
import unittest
funcs = [Solution().maxResult]

class TestMaxResult(unittest.TestCase):
    def testMaxResult1(self):
        for func in funcs:
            nums = [1,-1,-2,4,-7,3]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 7)

    def testMaxResult2(self):
        for func in funcs:
            nums = [10,-5,-2,4,0,3]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 17)

    def testMaxResult3(self):
        for func in funcs:
            nums = [1,-5,-20,4,-1,3,-6,-3]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 0)

if __name__ == "__main__":
    unittest.main()