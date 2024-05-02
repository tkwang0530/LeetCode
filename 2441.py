"""
2441. Largest Positive Integer That Exists With Its Negative
description: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/
"""

"""
Note:
1. HashTable: O(n) time | O(n) space - where n is the length of array nums
"""




import unittest
from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numSet = set()
        largest = -float("inf")
        for num in nums:
            numSet.add(num)

            if num in numSet and -num in numSet:
                largest = max(largest, abs(num))
            
        return largest if largest != -float("inf") else -1


# Unit Tests
funcs = [Solution().findMaxK]


class TestFindMaxK(unittest.TestCase):
    def testFindMaxK1(self):
        for func in funcs:
            nums = [-1, 2, -3, 3]
            self.assertEqual(func(nums=nums), 3)

    def testFindMaxK2(self):
        for func in funcs:
            nums = [-1, 10, 6, 7, -7, 1]
            self.assertEqual(func(nums=nums), 7)

    def testFindMaxK3(self):
        for func in funcs:
            nums = [-10, 8, 6, 7, -2, -3]
            self.assertEqual(func(nums=nums), -1)


if __name__ == "__main__":
    unittest.main()
