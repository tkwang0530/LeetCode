"""
15. 3Sum
description: https://leetcode.com/problems/3sum/description/
"""

"""
Note:
1. Two Pointers: O(n^2) time | O(n) space
"""




import unittest
from  typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif currentSum < 0:
                    left += 1
                elif currentSum > 0:
                    right -= 1
        return triplets


# Unit Tests

funcs = [Solution().threeSum]


class TestThreeSum(unittest.TestCase):
    def testThreeSum1(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def testThreeSum2(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[]), [])

    def testThreeSum3(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[0]), [])


if __name__ == "__main__":
    unittest.main()
