"""
862. Shortest Subarray with Sum at Least K
description: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
"""

"""
Note:
1. monotonic queue: O(n) time | O(n) space - where n is the length of array nums 
"""

from typing import List
import collections
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        output = float("inf")

        # monotonic increaseing queue
        queue = collections.deque() # (prefixSum, endingIdx)
        runningSum = 0
        for R in range(len(nums)):
            runningSum += nums[R]
            if runningSum >= k:
                output = min(output, R+1)

            # find the minimum prefixSum from the queue
            while queue and runningSum - queue[0][0] >= k:
                _, endingIdx = queue.popleft()
                output = min(output, R-endingIdx)

            # maintain the queue
            while queue and queue[-1][0] >= runningSum:
                queue.pop()

            queue.append((runningSum, R))

        return -1 if output == float("inf") else output

import unittest
funcs = [Solution().shortestSubarray]

class TestShortestSubarray(unittest.TestCase):
    def testShortestSubarray1(self):
        for func in funcs:
            nums = [1]
            k = 1
            self.assertEqual(func(nums=nums, k=k), 1)

    def testShortestSubarray2(self):
        for func in funcs:
            nums = [1,2]
            k = 4
            self.assertEqual(func(nums=nums, k=k), -1) 

    def testShortestSubarray3(self):
        for func in funcs:
            nums = [2,-1,2]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 3) 

if __name__ == "__main__":
    unittest.main()
