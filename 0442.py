"""
442. Find All Duplicates in an Array
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example2:
Input: nums = [1,1,2]
Output: [1]

Example3:
Input: nums = [1]
Output: []

Constraints:
1 <= nums.length <= 3 * 10^4
-10^5 <= nums[i] <= 10^5

"""

"""
Note:
1. use negative sign as marker: O(n) time | O(1) space
"""

import unittest
from  typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                result.append(abs(num))
            else:
                nums[abs(num)-1] = -nums[abs(num)-1]
        return result


# Unit Tests
funcs = [Solution().findDuplicates]


class TestFindDuplicates(unittest.TestCase):
    def testFindDuplicates1(self):
        for func in funcs:
            nums = [4,3,2,7,8,2,3,1]
            self.assertEqual(func(nums=nums), [2,3])

    def testFindDuplicates2(self):
        for func in funcs:
            nums = [1,1,2]
            self.assertEqual(func(nums=nums), [1])

    def testFindDuplicates3(self):
        for func in funcs:
            nums = [1]
            self.assertEqual(func(nums=nums), [])




if __name__ == "__main__":
    unittest.main()
