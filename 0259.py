"""
259. 3Sum Smaller
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target

Example1:
Input: nums = [-2, 0, 1, 3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]

Example2:
Input: nums = [], target = 0
Output: 0

Example3:
Input: nums = [0], target = 0
Output: 0

Follow up: Could you solve it in O(n^2) runtime?
"""

"""
Note:
1. Two Pointers: O(n^2) time | O(n) space
"""

import unittest
from  typing import List
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    result += right - left
                    left += 1
                else:
                    right -= 1
        return result


# Unit Tests
funcs = [Solution().threeSumSmaller]


class TestThreeSumSmaller(unittest.TestCase):
    def testThreeSumSmaller1(self):
        for func in funcs:
            nums = [-2, 0, 1, 3]
            target = 2
            self.assertEqual(
                func(nums=nums, target=target), 2)

    # def testThreeSumSmaller2(self):
    #     for func in funcs:
    #         nums = []
    #         target = 0
    #         self.assertEqual(
    #             func(nums=nums, target=target), 0)

    # def testThreeSumSmaller3(self):
    #     for func in funcs:
    #         nums = []
    #         target = 0
    #         self.assertEqual(
    #             func(nums=nums, target=target), 0)

    # def testThreeSumSmaller4(self):
    #     for func in funcs:
    #         nums = [-2, 0, 1, 3]
    #         target = 3
    #         self.assertEqual(
    #             func(nums=nums, target=target), 3)


if __name__ == "__main__":
    unittest.main()
