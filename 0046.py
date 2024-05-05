"""
46. Permutations
description: https://leetcode.com/problems/permutations/description/
"""

"""
Note:
1. backtrack O(n*n!) time | O(n + n*n!) space - where n is the length of nums
"""




import unittest
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        def dfs(i):
            if i == n - 1:
                output.append(nums.copy())
                return

            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return output


# Unit Tests
funcs = [Solution().permute]


class TestPermute(unittest.TestCase):
    def testPermute1(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[1, 2, 3]).sort(),
                [[1, 2, 3], [1, 3, 2], [2, 1, 3], [
                    2, 3, 1], [3, 1, 2], [3, 2, 1]].sort(),
            )

    def testPermute2(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[0, 1]).sort(),
                [[0, 1], [1, 0]].sort(),
            )

    def testPermute3(self):
        for func in funcs:
            self.assertEqual(
                func(nums=[1]).sort(),
                [[1]].sort(),
            )


if __name__ == "__main__":
    unittest.main()
