"""
523. Continuous Subarray Sum
description: https://leetcode.com/problems/continuous-subarray-sum/description/
"""

""" 
Notes:
1. Prefix Sum + Hash Map: O(n) time | O(k) space 
"""

from typing import List
class Solution(object):
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderIndice = {0: -1}
        currentSum = 0
        
        for i, num in enumerate(nums):
            currentSum += num
            remainder = currentSum % k
            if remainder in remainderIndice:
                if i - remainderIndice[remainder] > 1:
                    return True
            else:
                remainderIndice[remainder] = i
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
