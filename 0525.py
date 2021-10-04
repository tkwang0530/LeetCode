"""
525. Contiguous Array
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""

""" 
Notes:
1. Prefix Sum + Hash Map: O(n) time | O(n) space
store the count difference between one and zero into a Hash Map <diff, index>
"""

from collections import defaultdict
from typing import List
class Solution(object):
    def findMaxLength(self, nums: List[int]) -> int:
        oneZeroDiff = defaultdict(int)
        runningDiff = 0
        maxLength = 0
        for i, num in enumerate(nums):
            runningDiff += 1 if num == 1 else -1
                
            if runningDiff not in oneZeroDiff:
                oneZeroDiff[runningDiff] = i
            
            if runningDiff == 0:
                maxLength = max(maxLength, i + 1)
            if runningDiff in oneZeroDiff:
                maxLength = max(maxLength, i - oneZeroDiff[runningDiff])
        return maxLength

# Unit Tests
import unittest
funcs = [Solution().findMaxLength]

class TestFindMaxLength(unittest.TestCase):
    def testFindMaxLength1(self):
        for func in funcs:
            nums = [0,1]
            self.assertEqual(func(nums=nums), 2)

    def testFindMaxLength2(self):
        for func in funcs:
            nums = [0, 1, 0]
            self.assertEqual(func(nums=nums), 2)

if __name__ == "__main__":
    unittest.main()
