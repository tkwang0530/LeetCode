"""
16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""

"""
Note:
1. Two Pointers: O(n^2) time | O(n) space
"""




import unittest
from  typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if abs(target - currSum) < abs(diff):
                    diff = target - currSum
                if currSum > target:
                    right -= 1
                elif currSum < target:
                    left += 1
                else:
                    return target
        return target - diff


# Unit Tests

funcs = [Solution().threeSumClosest]


class TestThreeSumClosest(unittest.TestCase):
    def testThreeSumClosest1(self):
        for func in funcs:
            nums = [-1,2,1,-4]
            target = 1
            self.assertEqual(
                func(nums=nums, target=target), 2)


if __name__ == "__main__":
    unittest.main()
