"""
3068. Find the Maximum Sum of Node Values
description: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description/
"""

"""
Note:
1. Greedy: O(n) time | O(1) space - where n is the length of array nums
ref: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/solutions/4811460/greedy-sacrifice
"""

from typing import List
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        maxSum = sum([max(n, k ^ n) for n in nums])
        count = sum([(n ^ k) > n for n in nums])
        return maxSum - (min(abs(n-(n^k)) for n in nums) if count % 2 else 0)

# Unit Tests
import unittest
funcs = [Solution().maximumValueSum]

class TestMaximumValueSum(unittest.TestCase):
    def testMaximumValueSum1(self):
        for func in funcs:
            nums = [1,2,1]
            k = 3
            edges = [[0,1],[0,2]]
            self.assertEqual(func(nums=nums, k=k, edges=edges), 6)
            

    def testMaximumValueSum2(self):
        for func in funcs:
            nums = [2,3]
            k = 7
            edges = [[0,1]]
            self.assertEqual(func(nums=nums, k=k, edges=edges), 9)

    def testMaximumValueSum3(self):
        for func in funcs:
            nums = [7,7,7,7,7,7]
            k = 3
            edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
            self.assertEqual(func(nums=nums, k=k, edges=edges), 42)

if __name__ == "__main__":
    unittest.main()
