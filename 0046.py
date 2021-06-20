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
"""

"""
Note:
1. Recursion with string concatenation: O(n*n!) time | O(n + n*n!) space
2. Backtracking with same curr_list: O(n*n!) time | O(n + n*n!) space
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(curr_list, choices):  # everything has been chosen
            if len(choices) == 0:
                result.append(curr_list)
            else:
                for i in range(len(choices)):  # choose one from choices

                    # 0 ~ i-1 elements + i+1 ~ last elements
                    new_choices = choices[0:i] + choices[i + 1 :]
                    helper(curr_list + [choices[i]], new_choices)

        helper([], nums)
        return result

    def permute2(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(nums, i, curr_list):
            if i == len(nums):
                result.append(curr_list.copy())  # make a copy O(n)
            else:
                for j in range(i, len(nums)):
                    self.swap(nums, i, j)  # swap i, j elements
                    curr_list.append(nums[i])
                    helper(nums, i + 1, curr_list)
                    curr_list.pop()  # remove last element
                    self.swap(nums, i, j)  # swap back

        helper(nums, 0, [])
        return result

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


# Unit Tests
import unittest


class TestPermute(unittest.TestCase):
    def testPermute1(self):
        func = Solution().permute
        func2 = Solution().permute2
        self.assertEqual(
            func(nums=[1, 2, 3]).sort(),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]].sort(),
        )
        self.assertEqual(
            func2(nums=[1, 2, 3]).sort(),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]].sort(),
        )


if __name__ == "__main__":
    unittest.main()