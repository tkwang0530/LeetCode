"""
1608. Special Array With X Elements Greater Than or Equal X
description: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/
"""

"""
Note:
1. Counter: O(n) time | O(n) space - where n is the length of array nums
2. Sort + Binary Search: O(nlogn) time | O(sort) space - where n is the length of array nums
"""

from typing import List
import bisect
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
    
class Solution2:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for x in range(n+1):
            count = bisect.bisect_right(nums, x-1)
            if x == n-count:
                return x
        return -1

# Unit Tests
import unittest
funcs = [Solution().specialArray, Solution2().specialArray]

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