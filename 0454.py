"""
454. 4Sum II
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
- 0 <= i, j, k, l < n
- nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example2:
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

Constraints:
n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
"""

""" 
1. count sum12 and sum34 and store in HashTable: O(n^2) time | O(n^2) space
2. count sum12 and sum34 and store in HashTable (clean version): O(n^2) time | O(n^2) space
"""

from typing import List
from collections import Counter
class Solution(object):
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        numCount4 = Counter(nums4)
        numCount3 = Counter(nums3)
        numCount2 = Counter(nums2)
        numCount1 = Counter(nums1)
        numCount34 = {}
        numCount12 = {}
        total = 0
        for num3 in numCount3:
            for num4 in numCount4:
                numCount34[num3+num4] = numCount34.get(num3+num4, 0) + numCount3[num3] * numCount4[num4]
        
        for num2 in numCount2:
            for num1 in numCount1:
                numCount12[num1+num2] = numCount12.get(num1+num2, 0) + numCount1[num1] * numCount2[num2]
                
        for num12 in numCount12:
            for num34 in numCount34:
                if num12 + num34 == 0:
                    total += numCount12[num12] * numCount34[num34]
        return total

    def fourSumCount2(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        numCount12 = Counter(num1+num2 for num1 in nums1 for num2 in nums2)
        return sum(numCount12[-(num3+num4)] for num3 in nums3 for num4 in nums4)

# Unit Tests
import unittest
funcs = [Solution().fourSumCount, Solution().fourSumCount2]


class TestFourSumCount(unittest.TestCase):
    def testFourSumCount1(self):
        for func in funcs:
            nums1 = [1,2]
            nums2 = [-2,-1]
            nums3 = [-1,2]
            nums4 = [0,2]
            self.assertEqual(func(nums1=nums1, nums2=nums2, nums3=nums3, nums4=nums4), 2)

    def testFourSumCount2(self):
        for func in funcs:
            nums1 = [0]
            nums2 = [0]
            nums3 = [0]
            nums4 = [0]
            self.assertEqual(func(nums1=nums1, nums2=nums2, nums3=nums3, nums4=nums4), 1)

if __name__ == "__main__":
    unittest.main()
