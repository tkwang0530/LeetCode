"""
2799. Count Complete Subarrays in an Array
You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.

Example1:
Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

Example2:
Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 2000
"""

"""
Note:
1. Sliding Window: O(n) time | O(n) space - where n is the length of array nums
"""

import collections
from typing import List
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        k = len(set(nums))
        counter = collections.Counter()
        total = 0
        start = 0
        for end in range(n):
            counter[nums[end]] += 1
            while len(counter) == k:
                counter[nums[start]] -= 1
                if counter[nums[start]] == 0:
                    del counter[nums[start]]
                start += 1
            total += start
        return total

# Unit Tests
import unittest
funcs = [Solution().countCompleteSubarrays]


class TestCountCompleteSubarrays(unittest.TestCase):
    def testCountCompleteSubarrays1(self):
        for func in funcs:
            nums = [1,3,1,2,2]
            self.assertEqual(func(nums=nums), 4)

    def testCountCompleteSubarrays2(self):
        for func in funcs:
            nums = [5,5,5,5]
            self.assertEqual(func(nums=nums), 10)

    def testCountCompleteSubarrays3(self):
        for func in funcs:
            nums = [5,5,5,5,6,6,6,5,5]
            self.assertEqual(func(nums=nums), 26)


if __name__ == "__main__":
    unittest.main()
