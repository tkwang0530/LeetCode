"""
448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

"""
Notes:
1. Hash Table: O(n) time | O(n) space
2. Use Sign as marker: O(n) time | O(1) space
"""
from typing import List
class Solution(object):
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet = {num for num in nums}
        output = []
        for i in range(1, len(nums)+1):
            if i not in numSet:
                output.append(i)
        return output

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            nums[abs(num)-1] = -1 * abs(nums[abs(num)-1])
        
        output = []
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i+1)
        return output

# Unit Tests
import unittest
funcs = [Solution().findDisappearedNumbers, Solution().findDisappearedNumbers2]

class TestFindDisappearedNumbers(unittest.TestCase):
    def testFindDisappearedNumbers1(self):
        for func in funcs:
            nums = [4,3,2,7,8,2,3,1]
            self.assertEqual(func(nums=nums), [5,6])

    def testFindDisappearedNumbers2(self):
        for func in funcs:
            nums = [1,1]
            self.assertEqual(func(nums=nums), [2])

if __name__ == "__main__":
    unittest.main()