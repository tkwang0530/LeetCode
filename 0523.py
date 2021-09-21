"""
523. Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example3:
Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1
"""

""" 
Notes:
1. Prefix Sum + Hash Map: O(n) time | O(k) space 
"""

from typing import List
class Solution(object):
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderToIndex = {0: -1}
        subarraySum = 0
        for i in range(len(nums)):
            subarraySum += nums[i]
            if k != 0:
                subarraySum %= k
            if subarraySum in remainderToIndex:
                if i - remainderToIndex[subarraySum] > 1:
                    return True
            else:
                remainderToIndex[subarraySum] = i
        return False

# Unit Tests
import unittest
funcs = [Solution().checkSubarraySum]

class TestCheckSubarraySum(unittest.TestCase):
    def testCheckSubarraySum1(self):
        for func in funcs:
            nums = [23,2,4,6,7]
            k = 6
            self.assertEqual(func(nums=nums, k=k), True)

    def testCheckSubarraySum2(self):
        for func in funcs:
            nums = [23,2,6,4,7]
            k = 6
            self.assertEqual(func(nums=nums, k=k), True)

    def testCheckSubarraySum3(self):
        for func in funcs:
            nums = [23,2,6,4,7]
            k = 13
            self.assertEqual(func(nums=nums, k=k), False)

if __name__ == "__main__":
    unittest.main()
