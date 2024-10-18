"""
2044. Count Number of Maximum Bitwise-OR Subsets
description: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/
"""

"""
Note:
1. backtracking: O(2^n) time | O(n) space
"""

from typing import List
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0
        for num in nums:
            maxOR |= num
        
        n = len(nums)
        diffs = 0
        def backtrack(i, val):
            nonlocal diffs
            if i == n:
                if val == maxOR:
                    diffs += 1
                return
            
            # skip
            backtrack(i+1, val)

            # include
            backtrack(i+1, val | nums[i])
        
        backtrack(0, 0)
        return diffs

funcs = [Solution().countMaxOrSubsets]

import unittest
class TestCountMaxOrSubsets(unittest.TestCase):
    def testCountMaxOrSubsets1(self):
        for func in funcs:
            nums = [3,1]
            self.assertEqual(func(nums=nums), 2)

    def testCountMaxOrSubsets2(self):
        for func in funcs:
            nums = [2,2,2]
            self.assertEqual(func(nums=nums), 7)

    def testCountMaxOrSubsets3(self):
        for func in funcs:
            nums = [3, 2, 1, 5]
            self.assertEqual(func(nums=nums), 6)

if __name__ == "__main__":
    unittest.main()
