"""
18. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
- 0 <= a, b, c, d < n
- a, b, c and d are distinct
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


Example2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""

"""
Note:
1. Two Pointers: O(n^3) time | O(1) space
nested 3Sum
"""

import unittest
from  typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        if len(nums) < 4:
            return result
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    currSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if currSum > target:
                        right -= 1
                    elif currSum < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        while right > left and nums[right] == nums[right+1]:
                            right -= 1
                        left += 1
                        while right > left and nums[left] == nums[left - 1]:
                            left += 1
        return result

# Unit Tests
funcs = [Solution().fourSum]


class TestFourSum(unittest.TestCase):
    def testFourSum1(self):
        for func in funcs:
            nums = [1,0,-1,0,-2,2]
            target = 0
            self.assertEqual(
                func(nums=nums, target=target), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])

    def testFourSum2(self):
        for func in funcs:
            nums = [2,2,2,2,2]
            target = 8
            self.assertEqual(
                func(nums=nums, target=target), [[2,2,2,2]])

if __name__ == "__main__":
    unittest.main()
