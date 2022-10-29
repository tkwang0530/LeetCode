"""
2447. Number of Subarrays With GCD Equal to K
Given an integer array nums and an integer k, return the number of subarrays nums where the greatest common divisor of the subarray's element is k.

The greatest common divisor of an array is the largest integer that evenly divides all the array elements.

Example1:
Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]

Example2:
Input: nums = [4], k = 7
Output: 0
Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.

Constraints:
1 <= nums.length <= 1000
1 <= nums[i], k <= 10^9
"""

"""
Note:
1. Recursion: O(n^2) time | O(1) space - where n is the length of array nums
"""




import unittest
from typing import List
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if a > b:
                a, b = b, a

            if b % a == 0:
                return a
            return gcd(b % a, a)

        n = len(nums)
        output = 0
        for i in range(n):
            g = nums[i]
            if g == k:
                output += 1
            for j in range(i+1, n):
                g = gcd(g, nums[j])
                if g == k:
                    output += 1

                if g % k > 0:
                    break
        return output


# Unit Tests
funcs = [Solution().subarrayGCD]


class TestSubarrayGCD(unittest.TestCase):
    def testSubarrayGCD1(self):
        for func in funcs:
            nums = [9, 3, 1, 2, 6, 3]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 4)

    def testSubarrayGCD2(self):
        for func in funcs:
            nums = [4]
            k = 7
            self.assertEqual(func(nums=nums, k=k), 0)


if __name__ == "__main__":
    unittest.main()
