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
2. DFS (append to result during traversal): O(n * 2^n) time | O(n * 2^n) space
3. DFS (append to result when index == len(nums)): O(n * 2^n) time | O(n * 2^n) space
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

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.dfs(nums, result, [], 0)
        return result
    
    def dfs(self, nums: List[int], result: List[List[int]], subset: List[int], index: int):
        result.append(subset[:])
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, result, subset, i + 1)
            subset.pop()

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.dfs2(nums, result, [], 0)
        return result

    def dfs2(self, nums: List[int], result: List[List[int]], subset: List[int], index: int):
        if index == len(nums):
            result.append(subset[:])
        else:
            self.dfs2(nums, result, subset, index + 1)
            subset.append(nums[index])
            self.dfs2(nums, result, subset, index + 1)
            subset.pop()
        


# Unit Tests
funcs = [Solution().subsets, Solution().subsets2, Solution().subsets3]


class TestSubsets(unittest.TestCase):
    def testSubsets1(self):
        for func in funcs:
            nums = [1, 2, 3]
            self.assertEqual(sorted(func(nums=nums)), sorted([[], [1], [2], [
                             1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]))

    def testSubsets2(self):
        for func in funcs:
            nums = [0]
            self.assertEqual(sorted(func(nums=nums)), sorted([[], [0]]))


if __name__ == "__main__":
    unittest.main()
