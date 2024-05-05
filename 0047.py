"""
47. Permutations II
description: https://leetcode.com/problems/permutations-ii/description/
"""

"""
Note:
1. Recursion with concatenation: O(n*n!) time | O(n^2) space
2. Recursion (swap element + snapshot + set): O(n*n!) time | O(n) space
3. backtrack + hashSet: O(n*n!) time | O(n) space - where n is the length of nums
"""




import unittest
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        self.helper(nums, [], answers)
        return answers

    def helper(self, nums: List[int], curr: List[int], answers: List[List[int]]):
        if len(nums) == 0:
            answers.append(curr.copy())
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            self.helper(nums[0:i] + nums[i + 1:], curr, answers)
            curr.pop()

class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.helper(nums, 0, permutations)
        return permutations

    def helper(self, nums, i, permutations):
        if i == len(nums) - 1:
            permutations.append(nums[:])
        else:
            visited = set()
            for j in range(i, len(nums)):
                if nums[j] not in visited:
                    visited.add(nums[j])
                    self.swap(nums, i, j)
                    self.helper(nums, i + 1, permutations)
                    self.swap(nums, i, j)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

class Solution3:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output = []
        def backtrack(i):
            if i == n-1:
                output.append(nums.copy())
                return

            visited = set()
            for j in range(i, n):
                if nums[j] in visited:
                    continue

                visited.add(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        backtrack(0)
        return output

# Unit Tests
funcs = [Solution().permuteUnique, Solution2().permuteUnique, Solution3().permuteUnique]


class TestPermuteUnique(unittest.TestCase):
    def testPermuteUnique1(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[1, 1, 2]).sort(),
                [[1, 1, 2], [1, 2, 1], [2, 1, 1]].sort(),
            )

    def testPermuteUnique2(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[1, 2, 3]).sort(),
                [[1, 2, 3], [1, 3, 2], [2, 1, 3], [
                    2, 3, 1], [3, 1, 2], [3, 2, 1]].sort(),
            )


if __name__ == "__main__":
    unittest.main()
