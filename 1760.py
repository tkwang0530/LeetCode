"""
1760. Minimum Limit of Balls in a Bag
description: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/
"""

"""
Note:
1. Binary Search:  O(nlog(max(nums)) time | O(1) space - where n is the length of array nums 
"""

from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def condition(maxSize):
            ops = 0
            for num in nums:
                if num <= maxSize:
                    continue

                # num = 8, maxSize = 5
                # 8 // 5 = 1 ... 3
                ops += num // maxSize - (num % maxSize == 0)
            return ops <= maxOperations

        left, right = 1, max(nums)+1
        minPenalty = float("inf")
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                minPenalty = min(minPenalty, mid)
                right = mid
            else:
                left = mid + 1
        
        return minPenalty

import unittest
funcs = [Solution().minimumSize]

class TestMinimizeSize(unittest.TestCase):
    def testMinimizeSize1(self):
        for func in funcs:
            nums = [9]
            maxOperations = 2
            self.assertEqual(func(nums=nums, maxOperations=maxOperations), 3)

    def testMinimizeSize2(self):
        for func in funcs:
            nums = [2,4,8,2]
            maxOperations = 4
            self.assertEqual(func(nums=nums, maxOperations=maxOperations), 2) 

if __name__ == "__main__":
    unittest.main()
