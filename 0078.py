"""
78. Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

"""
Note:
1. Iteration: O(n * 2^n) time | O(n * 2^n) space
2. Recursion: O(n * 2^n) time | O(n * 2^n) space
"""




import unittest
from  typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                currentSubset = subsets[i]
                subsets.append(currentSubset + [num])
        return subsets

    def subsets2(self, nums: List[int], idx=None) -> List[List[int]]:
        if idx is None:
            idx = len(nums) - 1
        if idx < 0:
            return [[]]
        else:
            element = nums[idx]
            subsets = self.subsets2(nums, idx - 1)
            for i in range(len(subsets)):
                subset = subsets[i]
                subsets.append(subset + [element])
        return subsets


# Unit Tests
funcs = [Solution().subsets, Solution().subsets2]


class TestSubsets(unittest.TestCase):
    def testSubsets1(self):
        for func in funcs:
            nums = [1, 2, 3]
            self.assertEqual(func(nums=nums).sort(), [[], [1], [2], [
                             1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].sort())

    def testSubsets2(self):
        for func in funcs:
            nums = [0]
            self.assertEqual(func(nums=nums).sort(), [[], [0]].sort())


if __name__ == "__main__":
    unittest.main()
