"""
724. Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

Constraints:
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
"""

""" 
1. Left Prefix Sum + Right Prefix Sum: O(n) time | O(n) space
"""

from typing import List
class Solution(object):
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        leftPrefixSums = [0] * len(nums)
        rightPrefixSums = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            rightPrefixSums[i] += (rightPrefixSums[i+1] + nums[i+1])
        for i in range(len(nums)):
            if i > 0:
                leftPrefixSums[i] += (leftPrefixSums[i-1] + nums[i-1])
            if leftPrefixSums[i] == rightPrefixSums[i]:
                return i
        return -1

# Unit Tests
import unittest
funcs = [Solution().pivotIndex]
class TestPivotIndex(unittest.TestCase):
    def testPivotIndex1(self):
        for func in funcs:
            nums = [1,7,3,6,5,6]
            self.assertEqual(func(nums=nums), 3)

    def testPivotIndex2(self):
        for func in funcs:
            nums = [1,2,3]
            self.assertEqual(func(nums=nums), -1)

    def testPivotIndex3(self):
        for func in funcs:
            nums = [2, 1, -1]
            self.assertEqual(func(nums=nums), 0)

if __name__ == "__main__":
    unittest.main()
