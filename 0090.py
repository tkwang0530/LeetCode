"""
90. Subsets II
Given an integer array nums that may contain duplicates, resultsurn all possible subsets (the power set)

Example1:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example2:
    Input: nums = [0]
    Output: [[],[0]]
"""

"""
Note:
1. Recursion with DFS: O(n * 2^n) time | O(n + n*2^n) space
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.dfs(sorted(nums), [], results)
        return results

    def dfs(self, nums: List[int], path: List[int], results: List[List[int]]):
        results.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[i + 1 :], path + [nums[i]], results)


# Unit Tests
import unittest


class TestSubsetsWithDup(unittest.TestCase):
    def testSubsetsWithDup1(self):
        func = Solution().subsetsWithDup
        self.assertEqual(
            func(nums=[1, 2, 2]).sort(),
            [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]].sort(),
        )

    def testSubsetsWithDup2(self):
        func = Solution().subsetsWithDup
        self.assertEqual(
            func(nums=[0]).sort(),
            [[], [0]].sort(),
        )


if __name__ == "__main__":
    unittest.main()