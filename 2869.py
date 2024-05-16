"""
2869. Minimum Operations to Collect Elements
description: https://leetcode.com/problems/minimum-operations-to-collect-elements/description/
"""

"""
Note:
1. HashSet: O(n) time | O(k) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        kSet = {i for i in range(1, k+1)}
        ops = 0
        while kSet:
            n = nums.pop()
            ops += 1
            if n in kSet:
                kSet.remove(n)
        return ops

# Unit Tests
import unittest
funcs = [Solution().minOperations]

class TestMinOperations(unittest.TestCase):
    def testMinOperations1(self):
        for func in funcs:
            nums = [3,1,5,4,2]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 4)

    def testMinOperations2(self):
        for func in funcs:
            nums = [3,1,5,4,2]
            k = 5
            self.assertEqual(func(nums=nums, k=k), 5)

    def testMinOperations3(self):
        for func in funcs:
            nums = [3,2,5,3,1]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 4)


if __name__ == "__main__":
    unittest.main()
