"""
90. Subsets II
description: https://leetcode.com/problems/subsets-ii/description/
"""

"""
Note:
1. Iteration: O(n * 2^n) time | O(n * 2^n) space
(0) initiate the subsets to [[]]
(1) sort nums before iteration
(2) if i > 0 and nums[i] == nums[i-1]: update startIdx = endIdx + 1
(3) update endIdx = len(subsets) - 1
(4) from subset[startIdx] to subset[endIdx]: subsets.append(currSubset + [nums[i]])

2. DFS (append to result during traversal): O(n * 2^n) time | O(n * 2^n) space
(1) sort nums before dfs
(2) in the for loop, if i > index and nums[index] == nums[index-1]: continue

3. DFS (append to result during traversal): O(n * 2^n) time | O(n * 2^n) space
(1) sort nums before dfs
(2) if not subset or subset[-1] != nums[index]: do the "not pick" dfs

4. DFS + hashSet: O(n * 2^n) time | O(n * 2^n) space
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()
        endIdx = 0
        for i in range(len(nums)):
            startIdx = endIdx + 1 if i > 0 and nums[i] == nums[i-1] else 0
            endIdx = len(subsets) - 1
            for j in range(startIdx, endIdx + 1):
                currSubset = subsets[j]
                subsets.append(currSubset + [nums[i]])
        return subsets

class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.dfs(nums, result, [], 0)
        return result

    def dfs(self, nums: List[int], result: List[List[int]], subset: List[int], index: int) -> None:
        result.append(subset[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, result, subset, i + 1)
            subset.pop()

class Solution3:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.dfs(nums, result, [], 0)
        return result

    def dfs(self, nums: List[int], result: List[List[int]], subset: List[int], index: int) -> None:
        if index == len(nums):
            result.append(subset[:])
        else:
            if not subset or subset[-1] != nums[index]:
                self.dfs(nums, result, subset, index + 1)
            subset.append(nums[index])
            self.dfs(nums, result, subset, index + 1)
            subset.pop()

class Solution4:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output = set()
        current = []
        def backtrack(i):
            if i == n:
                output.add(tuple(current))
                return
            
            # skip
            backtrack(i+1)

            # include
            current.append(nums[i])
            backtrack(i+1)
            current.pop()
        backtrack(0)
        return [list(subset) for subset in output]
# Unit Tests
import unittest
funcs = [Solution().subsetsWithDup, Solution2().subsetsWithDup, Solution3().subsetsWithDup, Solution4().subsetsWithDup]

class TestSubsetsWithDup(unittest.TestCase):
    def testSubsetsWithDup1(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(nums=[1, 2, 2])),
                sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
            )

    def testSubsetsWithDup2(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(nums=[0])),
                sorted([[], [0]]),
            )


if __name__ == "__main__":
    unittest.main()