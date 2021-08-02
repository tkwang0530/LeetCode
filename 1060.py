"""
1060. Missing Element in Sorted Array
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array

Example1:
Input: nums = [4, 7, 9, 10], k = 1
Output: 5
Explanation: The first missing number is 5.

Example2:
Input: nums = [4, 7, 9, 10], k = 3
Output: 8
Explanation: The missing numbers are [5, 6, 8, ...], hence the third missing number is 8.

Example3:
Input: nums = [1, 2, 4], k = 3
Output: 6
Explanation: The missing numbers are [3, 5, 6, 7, ...], hence the third missing number is 6.

Constraints:
1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^7
nums is sorted in ascending order, and all the elements are unique.
1 <= k <= 10^8
"""

"""
Note:
1. Binary Search: O(logn) time | O(1) space
How many missing number between index 0 and index mid?
nums[mid] - nums[0] - mid
numOfMissingNumbers < k: left = mid + 1, otherwise right = mid - 1
"""

from typing import List
import unittest
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            numOfMissingNumbers = nums[mid] - nums[0] - mid
            if numOfMissingNumbers < k:
                left = mid + 1
            else:
                right = mid
        return nums[0] + k + left - 1



# Unit Tests
funcs = [Solution().missingElement]


class TestMissingElement(unittest.TestCase):
    def testMissingElement1(self):
        for func in funcs:
            nums = [4, 7, 9, 10]
            k = 1
            self.assertEqual(func(nums=nums, k=k), 5)

    def testMissingElement2(self):
        for func in funcs:
            nums = [4, 7, 9, 10]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 8)

    def testMissingElement3(self):
        for func in funcs:
            nums = [1, 2, 4]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 6)


if __name__ == "__main__":
    unittest.main()
