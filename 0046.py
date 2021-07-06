"""
46. Permutations
Given a collection of distinct integers, return all possible permutations.

Example1:
    Input: [1, 2, 3]
    Output: [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

"""
Note:
1. Recursion with concatenation: O(n^2*n!) time | O(n + n*n!) space
2. Recursion (swap element + snapshot): O(n*n!) time | O(n + n*n!) space
"""




import unittest
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permutationsHelper(nums, [], permutations)
        return permutations

    def permutationsHelper(self, nums: List[int], currentPermutation: List[int], permutations: List[int]):
        if len(nums) == 0:
            permutations.append(currentPermutation)
        else:
            for i in range(len(nums)):
                newArray = nums[:i] + nums[i+1:]
                newPermutation = currentPermutation + [nums[i]]
                self.permutationsHelper(
                    newArray, newPermutation, permutations)

    def permute2(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permutationsHelper2(nums, 0, permutations)
        return permutations

    def permutationsHelper2(self, nums: List[int], i: int, permutations: List[List[int]]):
        if i == len(nums) - 1:
            permutations.append(nums[:])
        else:
            for j in range(i, len(nums)):
                self.swap(nums, i, j)
                self.permutationsHelper2(nums, i + 1, permutations)
                self.swap(nums, i, j)

    def swap(self, arr: List[int], i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]


# Unit Tests
funcs = [Solution().permute, Solution().permute2]


class TestPermute(unittest.TestCase):
    def testPermute1(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[1, 2, 3]).sort(),
                [[1, 2, 3], [1, 3, 2], [2, 1, 3], [
                    2, 3, 1], [3, 1, 2], [3, 2, 1]].sort(),
            )

    def testPermute2(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[0, 1]).sort(),
                [[0, 1], [1, 0]].sort(),
            )

    def testPermute3(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[1]).sort(),
                [[1]].sort(),
            )


if __name__ == "__main__":
    unittest.main()
