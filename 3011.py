"""
3011. Find if Array Can Be Sorted
description: https://leetcode.com/problems/find-if-array-can-be-sorted/description/ 
"""

"""
Note:
1. bit manipulation: O(n) time | O(n) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count(num):
            bits = 0
            while num > 0:
                bits += num % 2
                num //= 2
            return bits

        bitCounts = [count(num) for num in nums]

        minMaxs = []

        minNum = nums[0]
        maxNum = nums[0]
        for i in range(1, len(nums)):
            if bitCounts[i-1] == bitCounts[i]:
                minNum = min(minNum, nums[i])
                maxNum = max(maxNum, nums[i])
            else:
                minMaxs.append((minNum, maxNum))
                minNum = nums[i]
                maxNum = nums[i]
        
        minMaxs.append((minNum, maxNum))
        for i in range(1, len(minMaxs)):
            if minMaxs[i-1][1] > minMaxs[i][0]:
                return False
        
        return True

# Unit Tests
import unittest
funcs = [Solution().canSortArray]

class TestCanSortArray(unittest.TestCase):
    def testCanSortArray1(self):
        for func in funcs:
            nums = [8,4,2,30,15]
            self.assertEqual(func(nums=nums), True)

    def testCanSortArray2(self):
        for func in funcs:
            nums = [1,2,3,4,5]
            self.assertEqual(func(nums=nums), True)

    def testCanSortArray3(self):
        for func in funcs:
            nums = [3,16,8,4,2]
            self.assertEqual(func(nums=nums), False)

if __name__ == "__main__":
    unittest.main()
