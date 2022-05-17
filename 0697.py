"""
697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example1:
Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Constraints:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

"""
Notes:
1. Hash Table: O(n) time | O(n) space - where n is the length of nums
"""

import collections
from typing import List
class Solution(object):
    def findShortestSubArray(self, nums: List[int]) -> int:
        numStartEnd = collections.defaultdict(list)
        numCount = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if num not in numStartEnd:
                numStartEnd[num].append(i)
                numStartEnd[num].append(i)
            else:
                numStartEnd[num][-1] = i
            
            numCount[num] += 1
            
        maxCount = max(numCount.values())
        minLength = len(nums)
        for num, count in numCount.items():
            if count != maxCount:
                continue
            
            minLength = min(minLength, numStartEnd[num][1] - numStartEnd[num][0] + 1)
        return minLength

# Unit Tests
import unittest
funcs = [Solution().findShortestSubArray]

class TestFindShortestSubArray(unittest.TestCase):
    def testFindShortestSubArray1(self):
        for func in funcs:
            nums = [1,2,2,3,1]
            self.assertEqual(func(nums=nums), 2)

    def testFindShortestSubArray2(self):
        for func in funcs:
            nums = [1,2,2,3,1,4,2]
            self.assertEqual(func(nums=nums), 6)

if __name__ == "__main__":
    unittest.main()