"""
41. First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example1:
Input: nums = [1,2,0]
Output: 3

Example2:
Input: nums = [3,4,-1,1]
Output: 2

Example3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""

"""
Note:
1. index as marker (basic): O(n) time | O(1) space
(1) find the first in range number [1, len(nums)]
(2) change all out of range number into firstInRangeNum
(3) use the negative sign and index as marker to record exist number

2. index as marker (advanced): O(n) time | O(1) space
(1) change all out of range number into 0
(2) go through nums, if nums[i] is in the range of [1:n], we use index (nums[i] - 1) to record that we have seen nums[i] by adding n+1 to nums[nums[i] - 1]
(3) find the first index i for which nums[i] is less than n+1 (which means we never met number i+1 so we did not add n+1 to nums[i])
"""

from typing import List
import unittest
class Solution(object):
    def firstMissingPositive(self, nums: List[int]) -> int:
        firstInRangeNum = -1
        for num in nums:
            if num > 0 and num <= len(nums):
                firstInRangeNum = num
                break
        if firstInRangeNum == -1:
            return 1
        for i, num in enumerate(nums):
            if num <= 0 or num > len(nums):
                nums[i] = firstInRangeNum
        
        for num in nums:
            nums[abs(num) - 1] = -1 * abs(nums[abs(num) - 1])
        
        for i, num in enumerate(nums):
            if num > 0:
                return i+1
        return len(nums) + 1

    def firstMissingPositive2(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0
        for i in range(n):
            if 1 <= nums[i] % (n+1) <= n:
                index = nums[i] % (n+1) - 1
                nums[index] += n+1
        for i in range(n):
            if nums[i] <= n:
                return i+1
        return n+1

# Unit Tests
funcs = [Solution().firstMissingPositive, Solution().firstMissingPositive2]

class TestFirstMissingPositive(unittest.TestCase):
    def testFirstMissingPositive1(self):
        for func in funcs:
            nums = [1,2,0]
            self.assertEqual(func(nums=nums), 3)

    def testFirstMissingPositive2(self):
        for func in funcs:
            nums = [3,4,-1,1]
            self.assertEqual(func(nums=nums), 2)

    def testFirstMissingPositive3(self):
        for func in funcs:
            nums = [7,8,9,11,12]
            self.assertEqual(func(nums=nums), 1)


if __name__ == "__main__":
    unittest.main()
