"""
2597. The Number of Beautiful Subsets
description: https://leetcode.com/problems/the-number-of-beautiful-subsets/description/
"""

"""
Note:
1. Backtracking: O(nlogn+2^n) time | O(n) space - where n is the length of array nums
"""

import collections
from typing import List
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        container = [0]
        currentCounter = collections.defaultdict(int)
        def backtrack(i) -> int:
            if i == n:
                container[0] += 1
                return
            
            # skip
            backtrack(i+1)

            # include (if allow)
            if currentCounter[nums[i]-k] == 0:
                currentCounter[nums[i]] += 1
                backtrack(i+1)
                currentCounter[nums[i]] -= 1
        
        backtrack(0)
        return container[0]-1

# Unit Tests
import unittest
funcs = [Solution().beautifulSubsets]


class TestBeautifulSubsets(unittest.TestCase):
    def testBeautifulSubsets1(self):
        for beautifulSubsets in funcs:
            nums = [2,4,6]
            k = 2
            self.assertEqual(beautifulSubsets(nums=nums, k=k), 4)

    def testBeautifulSubsets2(self):
        for beautifulSubsets in funcs:
            nums = [1]
            k = 1
            self.assertEqual(beautifulSubsets(nums=nums, k=k), 1)

if __name__ == "__main__":
    unittest.main()
