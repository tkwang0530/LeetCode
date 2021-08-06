"""
713. Subarray Product Less Than K
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example2:
Input: nums = [1,2,3], k = 0
Output: 0
"""

"""
Note:
1. Sliding Window: O(n) time | O(1) space 
"""

import unittest
from  typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start, product, count = 0, 1, 0
        for end in range(len(nums)):
            product *= nums[end]
            while product >= k and start <= end:
                product /= nums[start]
                start += 1
            count += end - start + 1
        return count

# Unit Tests
funcs = [Solution().numSubarrayProductLessThanK]


class TestNumSubarrayProductLessThanK(unittest.TestCase):
    def testNumSubarrayProductLessThanK1(self):
        for func in funcs:
            nums = [10,5,2,6]
            k = 100
            self.assertEqual(
                func(nums=nums, k=k), 8)

    def testNumSubarrayProductLessThanK2(self):
        for func in funcs:
            nums = [1,2,3]
            k = 0
            self.assertEqual(
                func(nums=nums, k=k), 0)

if __name__ == "__main__":
    unittest.main()
