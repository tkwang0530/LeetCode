"""
491. Non-decreasing Subsequences
description: https://leetcode.com/problems/non-decreasing-subsequences/description/
"""

"""
Note:
1. DFS + hashSet: O(n * 2^n) time | O(n * 2^n) space - where n is the length of nums
"""

from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = set()
        current = []
        def backtrack(i):
            if i == n:
                if len(current) >= 2:
                    output.add(tuple(current))
                return

            # skip
            backtrack(i+1)

            # include if valid
            if not current or nums[i] >= current[-1]:
                current.append(nums[i])
                backtrack(i+1)
                current.pop()

        backtrack(0)
        return [list(subseq) for subseq in output]

# Unit Tests
import unittest
funcs = [Solution().findSubsequences]

class TestFindSubsequences(unittest.TestCase):
    def testFindSubsequences1(self):
        for func in funcs:
            nums = [4,6,7,7]
            self.assertEqual(
                sorted(func(nums=nums)),
                sorted([[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]),
            )

    def testFindSubsequences2(self):
        for func in funcs:
            nums = [4,4,3,2,1]
            self.assertEqual(
                sorted(func(nums=nums)),
                sorted([[4,4]]),
            )


if __name__ == "__main__":
    unittest.main()