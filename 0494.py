"""
494. Target Sum
description: https://leetcode.com/problems/target-sum/description/
"""

"""
Note:
1. dfs+memo: O(n*2000) time | O(n*2000) space - where n is the length of nums
"""

import unittest, functools
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i, target):
            if i == n:
                if target == 0:
                    return 1
                else:
                    return 0
            

            expressions = 0
            # +
            expressions += dfs(i+1, target-nums[i])


            # -
            expressions += dfs(i+1, target+nums[i])
            return expressions
        return dfs(0, target)

# Unit Tests
funcs = [Solution().findTargetSumWays]


class TestFindTargetSumWays(unittest.TestCase):
    def testFindTargetSumWays1(self):
        for func in funcs:
            nums = [1,1,1,1,1]
            target = 3
            self.assertEqual(func(nums=nums, target=target), 5)

    def testFindTargetSumWays2(self):
        for func in funcs:
            nums = [1]
            target = 1
            self.assertEqual(func(nums=nums, target=target), 1)

if __name__ == "__main__":
    unittest.main()
