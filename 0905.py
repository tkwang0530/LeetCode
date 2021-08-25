"""
905. Sort Array By Parity
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""

"""
Note:
1. Two Pointers (leftIdx, i)
if we find a even number, swap nums[leftIdx] and nums[i] and then increase leftIdx by 1

2. Two Pointers (left, right)
"""

from typing import List
import unittest
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        leftIdx = 0
        for i, num in enumerate(nums):
            if num % 2 == 0:
                nums[i], nums[leftIdx] = nums[leftIdx], nums[i]
                leftIdx += 1
        return nums

    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] % 2 == 0:
                left += 1
            while left <= right and nums[right] % 2 == 1:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums


# Unit Tests
funcs = [Solution().sortArrayByParity, Solution().sortArrayByParity2]


class TestSortArrayByParity(unittest.TestCase):
    def testSortArrayByParity1(self):
        for func in funcs:
            nums = [3, 1, 2, 4]
            self.assertTrue(func(nums=nums) in ([2, 4, 3, 1], [4, 2, 1, 3]))

    def testSortArrayByParity2(self):
        for func in funcs:
            nums = [0]
            self.assertEqual(func(nums=nums), [0])

if __name__ == "__main__":
    unittest.main()
