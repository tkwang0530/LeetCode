"""
78. Subsets
description: https://leetcode.com/problems/subsets/description/
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

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        current = []
        def backtrack(i):
            if i == n:
                output.append(current.copy())
                return

            # skip
            backtrack(i+1)

            # include
            current.append(nums[i])
            backtrack(i+1)
            current.pop()
        backtrack(0)
        return output

class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
funcs = [Solution().subsets, Solution2().subsets, Solution3().subsets]


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
