"""
2762. Continuous Subarrays
description: https://leetcode.com/problems/continuous-subarrays/description/
"""

"""
Note:
1. Sliding Window + HashTable: O(n) time | O(1) space - where n is the length of array nums
"""

import collections
from typing import List
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        L = 0
        counter = collections.defaultdict(int)
        for R in range(n):
            counter[nums[R]] += 1
            while max(counter.keys())-min(counter.keys()) > 2:
                counter[nums[L]] -= 1
                if counter[nums[L]] == 0:
                    del counter[nums[L]]
                L += 1
            
            Loption = R - L + 1
            count += Loption
        return count

# Unit Tests
import unittest
funcs = [Solution().continuousSubarrays]

class TestContinuousSubarrays(unittest.TestCase):
    def testContinuousSubarrays1(self):
        for func in funcs:
            nums = [5, 4, 2, 4]
            self.assertEqual(func(nums=nums), 8)
            

    def testContinuousSubarrays2(self):
        for func in funcs:
            nums = [1, 2, 3]
            self.assertEqual(func(nums=nums), 6)

if __name__ == "__main__":
    unittest.main()
