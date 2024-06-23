"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
description: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
"""

"""
Note:
1. SortedList + queue: O(nlogn) time | O(n) space - where n is the length of the array nums
"""

import collections
from typing import List
from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longest = 1
        bst = SortedList()
        queue = collections.deque()
        for num in nums:
            bst.add(num)
            queue.append(num)
            while bst[-1]-bst[0] > limit:
                numToRemove = queue.popleft()
                bst.remove(numToRemove)

            longest = max(longest, len(bst))
        return longest

# Unit Tests
import unittest
funcs = [Solution().longestSubarray]

class TestLongestSubarray(unittest.TestCase):
    def testLongestSubarray1(self):
        for func in funcs:
            nums = [8,2,4,7]
            limit = 4
            self.assertEqual(func(nums=nums, limit=limit), 2)

    def testLongestSubarray2(self):
        for func in funcs:
            nums = [10,1,2,4,7,2]
            limit = 5
            self.assertEqual(func(nums=nums, limit=limit), 4)

    def testLongestSubarray3(self):
        for func in funcs:
            nums = [4,2,2,2,4,4,2,2]
            limit = 0
            self.assertEqual(func(nums=nums, limit=limit), 3)

if __name__ == "__main__":
    unittest.main()
