"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
description: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
"""

"""
Note:
1. SortedList + queue: O(nlogn) time | O(n) space - where n is the length of the array nums
2. Monotonic Queues: O(n) time | O(n) space - where n is the length of the array nums
ref: Editorial
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

class Solution2:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQueue = collections.deque()
        minQueue = collections.deque()
        start = 0
        longest = 0
        n = len(nums)
        for end in range(n):
            # maintain the maxQueue in decreasing order
            while maxQueue and maxQueue[-1] < nums[end]:
                maxQueue.pop()
            maxQueue.append(nums[end])

            # maintain the minQueue in increasing order
            while minQueue and minQueue[-1] > nums[end]:
                minQueue.pop()
            minQueue.append(nums[end])

            while maxQueue[0] - minQueue[0] > limit:
                # Remove the elements that are out of the current window
                if maxQueue[0] == nums[start]:
                    maxQueue.popleft()
                if minQueue[0] == nums[start]:
                    minQueue.popleft()
                start += 1

            longest = max(longest, end-start+1)
        return longest
# Unit Tests
import unittest
funcs = [Solution().longestSubarray, Solution2().longestSubarray]

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
