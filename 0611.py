"""
611. Valid Triangle Number
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example2:
Input: nums = [4,2,3,4]
Output: 4

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""

"""
Note:
1. Binary Search: O(n^2) time | O(n) space - where n is the length of array nums
"""




from typing import List
import unittest
import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n-2):
            if nums[i] == 0:
                continue
            for j in range(i+1, n):
                firstTwoSum = nums[i] + nums[j]
                idx = bisect.bisect_right(nums, firstTwoSum-1, j+1)
                count += (idx-j-1)
        return count


# Unit Tests
funcs = [Solution().triangleNumber]


class TestTriangleNumber(unittest.TestCase):
    def testTriangleNumber1(self):
        for func in funcs:
            nums = [2, 2, 3, 4]
            self.assertEqual(func(nums=nums), 3)

    def testTriangleNumber2(self):
        for func in funcs:
            nums = [4, 2, 3, 4]
            self.assertEqual(func(nums=nums), 4)


if __name__ == "__main__":
    unittest.main()
