"""
2444. Count Subarrays With Fixed Bounds
description: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/
"""

"""
Note:
1.  Sliding Window: O(n) time | O(1) space - where n is the length of array nums
ref: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/2708099/java-c-python-sliding-window-with-explanation
"""




import unittest
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        jmin = jmax = jbad = -1
        output = 0
        for end in range(n):
            num = nums[end]
            if num < minK or num > maxK:
                jbad = end
            if num == minK:
                jmin = end
            if num == maxK:
                jmax = end
            output += max(0, min(jmin, jmax) - jbad)
        return output
        pass

# Unit Tests
funcs = [Solution().countSubarrays]


class TestCountSubarrays(unittest.TestCase):
    def testCountSubarrays1(self):
        for func in funcs:
            nums = [1, 3, 5, 2, 7, 5]
            minK = 1
            maxK = 5
            self.assertEqual(func(nums=nums, minK=minK, maxK=maxK), 2)

    def testCountSubarrays2(self):
        for func in funcs:
            nums = [1, 1, 1, 1]
            minK = 1
            maxK = 1
            self.assertEqual(func(nums=nums, minK=minK, maxK=maxK), 10)


if __name__ == "__main__":
    unittest.main()
