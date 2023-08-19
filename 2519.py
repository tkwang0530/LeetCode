"""
2519. Count the Number of K-Big Indices
description: https://leetcode.com/problems/count-the-number-of-k-big-indices/description/
"""

"""
Note:
1. Two BSTs: O(nlogn) time | O(n) space - where n is the length of array nums
"""

from typing import List
from sortedcontainers import SortedList
class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        smallerProp = [[0,0] for _ in range(n)]
        bst = SortedList()
        for i in range(n):
            num = nums[i]
            smallerProp[i][0] = bst.bisect_right(num-1)
            bst.add(num)

        bst = SortedList()
        for i in range(n-1, -1, -1):
            num = nums[i]
            smallerProp[i][1] = bst.bisect_right(num-1)
            bst.add(num)

        kBigs = 0
        for i in range(n):
            if min(smallerProp[i]) >= k:
                kBigs += 1
        return kBigs

# Unit Tests
import unittest
funcs = [Solution().kBigIndices]
class TestKBigIndices(unittest.TestCase):
    def testKBigIndices1(self):
        for kBigIndices in funcs:
            nums = [2,3,6,5,2,3]
            k = 2
            self.assertEqual(kBigIndices(nums=nums, k=k), 2)

    def testKBigIndices2(self):
        for kBigIndices in funcs:
            nums = [1,1,1]
            k = 3
            self.assertEqual(kBigIndices(nums=nums, k=k), 0)

if __name__ == "__main__":
    unittest.main()
