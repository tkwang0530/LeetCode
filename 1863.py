"""
1863. Sum of All Subset XOR Totals
description: https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
"""

"""
Note:
1. Backtrack: O(2^n * n) time | O(n) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        container = [0]
        current = []

        def calculate():
            if not current:
                return 0
            
            ans = current[0]
            for i in range(1, len(current)):
                ans ^= current[i]
            return ans
        def backtrack(i):
            if i == n:
                container[0] += calculate()
                return

            # skip
            backtrack(i+1)

            # include
            current.append(nums[i])
            backtrack(i+1)
            current.pop()
        backtrack(0)
        return container[0]

# Unit Tests
import unittest
funcs = [Solution().subsetXORSum]

class TestSubsetXORSum(unittest.TestCase):
    def testSubsetXORSum1(self):
        for func in funcs:
            nums = [1,3]
            self.assertEqual(func(nums=nums), 6)
            

    def testSubsetXORSum2(self):
        for func in funcs:
            nums = [5,1,6]
            self.assertEqual(func(nums=nums), 28)

    def testSubsetXORSum3(self):
        for func in funcs:
            nums = [3,4,5,6,7,8]
            self.assertEqual(func(nums=nums), 480)

if __name__ == "__main__":
    unittest.main()
