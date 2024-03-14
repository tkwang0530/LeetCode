"""
1268. Search Suggestion System
description: https://leetcode.com/problems/search-suggestions-system/description/
"""

""" 
1. PreSum + Binary Search: O(n+nlogn) time | O(n) space - where n is array nums
2. PreSum + HashMap: O(n) time | O(n) space - where n is array nums
"""
import bisect, collections
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]
        
        count = 0
        for i in range(n):
            left = bisect.bisect_left(preSums, goal+preSums[i], lo=i+1)
            right = bisect.bisect_right(preSums, goal+preSums[i], lo=i+1)
            count += right-left
        return count

class Solution2:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        preSums = [0] * (n+1)
        for i in range(1, n+1):
            preSums[i] = preSums[i-1] + nums[i-1]
        
        count = 0
        numRanges = collections.defaultdict(list)
        for i, num in enumerate(preSums):
            if num not in numRanges:
                numRanges[num] = [i,i]
            else:
                numRanges[num][-1] = i

        for i in range(n):
            target = goal+preSums[i]
            left = numRanges[target][0] if target in numRanges else n+1
            right = numRanges[target][1] if target in numRanges else n+1
            count += right-max(i+1,left)+1 if left < n+1 else 0
        return count

# Unit Tests
import unittest
funcs = [Solution().numSubarraysWithSum, Solution2().numSubarraysWithSum]


class TestNumSubarraysWithSum(unittest.TestCase):
    def testNumSubarraysWithSum1(self):
        for func in funcs:
            nums = [1,0,1,0,1]
            goal = 2
            self.assertEqual(func(nums=nums, goal=goal), 4)

    def testNumSubarraysWithSum2(self):
        for func in funcs:
            nums = [0,0,0,0,0]
            goal = 0
            self.assertEqual(func(nums=nums, goal=goal), 15)

if __name__ == "__main__":
    unittest.main()
