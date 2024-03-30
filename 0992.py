"""
992. Subarrays with K Different Integers
description: https://leetcode.com/problems/subarrays-with-k-different-integers/description
"""

"""
Note:
1. Sliding Window: O(n) time | O(n) space - where n is the length of array nums
ref: https://leetcode.com/problems/subarrays-with-k-different-integers/solutions/523136/java-c-python-sliding-window
"""

import collections
from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k: int) -> int:
            counter = collections.Counter()
            output = start = 0
            for end in range(len(nums)):
                counter[nums[end]] += 1
                while len(counter) > k:
                    counter[nums[start]] -= 1
                    if counter[nums[start]] == 0:
                        del counter[nums[start]]
                    start += 1
                output += end - start + 1
            return output
        
        return atMostK(k) - atMostK(k-1)

# Unit Tests
import unittest
funcs = [Solution().subarraysWithKDistinct]


class TestSubarraysWithKDistinct(unittest.TestCase):
    def testSubarraysWithKDistinct1(self):
        for func in funcs:
            nums = [1,2,1,2,3]
            k = 2
            self.assertEqual(func(nums=nums, k=k), 7)

    def testSubarraysWithKDistinct2(self):
        for func in funcs:
            nums = [1,2,1,3,4]
            k = 3
            self.assertEqual(func(nums=nums, k=k), 3)

if __name__ == "__main__":
    unittest.main()
