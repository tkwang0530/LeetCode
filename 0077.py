"""
77. Combinations
description: https://leetcode.com/problems/combinations/description/
"""

"""
Note:
1. backtracking (1): O(k * C(n,k)) time | O(k) space
2. backtraking (2): O(k * C(n,k)) time | O(k) space
"""




import unittest
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        self.helper(n, k, 1, [], combinations)
        return combinations

    def helper(self, n, k, start, combination, combinations):
        if len(combination) == k:
            combinations.append(combination[:])
        else:
            for i in range(start, n+1):
                combination.append(i)
                self.helper(n, k, i + 1, combination, combinations)
                combination.pop()

class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        current = []
        def backtrack(i):
            if len(current) == k:
                output.append(current.copy())
                return

            for j in range(i, n+1):
                current.append(j)
                backtrack(j+1)
                current.pop()

        backtrack(1)
        return output


# Unit Tests
funcs = [Solution().combine, Solution2().combine]


class TestCombine(unittest.TestCase):
    def testCombine1(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(n=4, k=2)),
                sorted([
                    [2, 4],
                    [3, 4],
                    [2, 3],
                    [1, 2],
                    [1, 3],
                    [1, 4],
                ]),
            )

    def testCombine2(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(n=1, k=1)),
                sorted([[1]]),
            )


if __name__ == "__main__":
    unittest.main()
