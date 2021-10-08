"""
229. Majority Element II
Given an integer array of size n, find all elements that appear more than n/3 times.

Example1:
Input: nums = [3,2,3]
Output: [3]

Example2:
Input: nums = [1]
Output: [1]

Example3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
"""

""" 
1. Use Hash Tables to store number counts: O(n) time | O(n) space - where n is the length of nums
2. Boyer-Moore Majority Vote algorithm: O(n) time | O(1) space
two candidates
"""

from typing import List
class Solution(object):
    def majorityElement(self, nums: List[int]) -> List[int]:
        satisfied = set()
        numCount = {} # <num, count>
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
            if numCount[num] > len(nums) // 3:
                satisfied.add(num)
        return list(satisfied)

    def majorityElement2(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = 0, 0
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        if candidate1 == candidate2:
            return [candidate1]
        return [num for num in (candidate1, candidate2) if nums.count(num) > len(nums) // 3]
            


# Unit Tests
import unittest
funcs = [Solution().majorityElement, Solution().majorityElement2]


class TestMajorityElement(unittest.TestCase):
    def testMajorityElement1(self):
        for func in funcs:
            nums = [3,2,3]
            self.assertEqual(sorted(func(nums=nums)), sorted([3]))

    def testMajorityElement2(self):
        for func in funcs:
            nums = [1]
            self.assertEqual(sorted(func(nums=nums)), sorted([1]))

    def testMajorityElement3(self):
        for func in funcs:
            nums = [1,2]
            self.assertEqual(sorted(func(nums=nums)), sorted([1, 2]))

    def testMajorityElement4(self):
        for func in funcs:
            nums = [1,1,1,3,3,2,2,2]
            self.assertEqual(sorted(func(nums=nums)), sorted([1, 2]))

    def testMajorityElement5(self):
        for func in funcs:
            nums = [0,0,0]
            self.assertEqual(sorted(func(nums=nums)), sorted([0]))

if __name__ == "__main__":
    unittest.main()
