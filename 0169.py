"""
169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than [n / 2] times. You may assume that the majority element always exists in the array.

Example1:
Input: nums = [3,2,3]
Output: 3

Example2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Cound you solve the problem in linear time and in O(1) space?
"""

"""
Notes:
1. Hash Table: O(n) time | O(n) space
2. Boyer Moore's Algorithm: O(n) time | O(1) space
"""
from typing import List
class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {} # <num, count>
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        for num in numCount:
            if numCount[num] >= len(nums) / 2:
                return num

    def majorityElement2(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate

# Unit Tests
import unittest
funcs = [Solution().majorityElement, Solution().majorityElement2]

class TestMajorityElement(unittest.TestCase):
    def testMajorityElement1(self):
        for func in funcs:
            nums = [3,2,3]
            self.assertEqual(func(nums=nums), 3)

    def testMajorityElement2(self):
        for func in funcs:
            nums = [2,2,1,1,1,2,2]
            self.assertEqual(func(nums=nums), 2)

if __name__ == "__main__":
    unittest.main()