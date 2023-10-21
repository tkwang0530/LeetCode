"""
1608. Special Array With X Elements Greater Than or Equal X
description: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/
"""

"""
Note:
1. Counter: O(n) time | O(n) space - where n is the length of array nums
"""

from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        counter = [0] * 1001
        for num in nums:
            counter[num] += 1

        runningCount = 0
        for i in range(len(counter)-1, -1, -1):
            runningCount += counter[i]
            if runningCount == i:
                return i
        
        return -1

# Unit Tests
import unittest
funcs = [Solution().specialArray]

class TestSpecialArray(unittest.TestCase):
    def testSpecialArray1(self):
        for specialArray in funcs:
            nums = [3,5]
            self.assertEqual(specialArray(nums=nums), 2)

    def testSpecialArray2(self):
        for specialArray in funcs:
            nums = [0,0]
            self.assertEqual(specialArray(nums=nums), -1)

    def testSpecialArray3(self):
        for specialArray in funcs:
            nums = [0,4,3,0,4]
            self.assertEqual(specialArray(nums=nums), 3)

if __name__ == "__main__":
    unittest.main()