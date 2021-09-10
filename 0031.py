"""
31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the loweest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example4:
Input: nums = [1]
Output: [1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

"""
Notes:
1. Two Pointers: O(n) time | O(1) space
(1) find the first number which is less than it's right
(2) if the number doesn't exist, reverse the nums and return
(3) for right to left, find the index where its value is larger than small
(4) exchange the value of small and big
(5) reverse the numbers  after "small" index (from small+1 to len(nums) - 1)
"""
from typing import List


class Solution(object):
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums or len(nums) == 0:
            return

        small = big = -1

        # find the first number which is less than it's right
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                small = i
                break
        
        if small == -1:
            nums.reverse()
            return
        
        # for right to left, find the index where its value is larger than small
        for i in range(len(nums) - 1, small, -1):
            if nums[i] > nums[small]:
                big = i
                break
        
        # exchange small and big
        nums[small], nums[big] = nums[big], nums[small]

        # reverse the numbers  after "small" index
        self.reverseFrom(nums, small + 1, len(nums) - 1)

    def reverseFrom(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1



# Unit Tests
import unittest
funcs = [Solution().nextPermutation]

class TestNextPermutation(unittest.TestCase):
    def testNextPermutation1(self):
        for func in funcs:
            nums = [1,2,3]
            func(nums=nums)
            self.assertEqual(nums, [1, 3, 2])

    def testNextPermutation2(self):
        for func in funcs:
            nums = [3,2,1]
            func(nums=nums)
            self.assertEqual(nums, [1, 2, 3])

    def testNextPermutation3(self):
        for func in funcs:
            nums = [1,1,5]
            func(nums=nums)
            self.assertEqual(nums, [1, 5, 1])

    def testNextPermutation4(self):
        for func in funcs:
            nums = [1]
            func(nums=nums)
            self.assertEqual(nums, [1])


if __name__ == "__main__":
    unittest.main()