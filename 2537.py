"""
2537. Count the Number of Good Subarrays
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

Example1:
Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.

Example2:
Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i], k <= 10^9
"""

"""
Note:
1. Sliding Window: O(n) time | O(n) space - where n is the length of array nums
"""

import unittest, collections
from typing import List
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def getMatches(count):
            return  count * (count-1) // 2
        
        numCount = collections.defaultdict(int)
        matches = 0
        goods = 0
        start = 0
        for end in range(n):
            numCount[nums[end]] += 1
            endCount = numCount[nums[end]]
            
            if endCount >= 2:
                    matches += getMatches(endCount)
                    if endCount-1 >= 2:
                        matches -= getMatches(endCount-1)

            valid = matches >= k
            oldStart = start
            while start < end and matches >= k:
                original = numCount[nums[start]]
                if original >= 2:
                    matches -= getMatches(original)
                    if original-1 >= 2:
                        matches += getMatches(original-1)
                
                numCount[nums[start]] -= 1
                start += 1
            if valid:
                goods += (start - oldStart) * ((n-1) - end+1)
        return goods

# Unit Tests
import unittest
funcs = [Solution().countGood]
class TestCountGood(unittest.TestCase):
    def testCountGood1(self):
        for func in funcs:
            nums = [1,1,1,1,1]
            k = 10
            self.assertEqual(func(nums=nums, k=k), 1)

    def testCountGood2(self):
        for func in funcs:
            nums = [3,1,4,3,2,2,4]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 4)

if __name__ == "__main__":
    unittest.main()
