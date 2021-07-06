"""
77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Example1:
    Input: n = 4, k = 2
    Output: 
    [
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
    ]
Example2:
    Input: n = 1, k = 1
    Output: [[1]]

Constraints:
1 <= n <= 20
1 <= k <= n
"""

"""
Note:
1. Recursion with backtracking (1): O(k*n!) time | O(k + k*n!) space
2. Recursion with backtracking (2): O(k*n!) time | O(k + k*n!) space
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

    def combine2(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        self.helper2(n, k, 1, [], combinations)
        return combinations

    def helper2(self, n, k, start, combination, result):
        if len(combination) == k:  # backtrack
            result.append(combination.copy())
            return
        if start == n + 1:  # can't add n+1 to combination
            return
        # exclude start
        self.helper2(n, k, start + 1, combination, result)

        # include start
        combination.append(start)
        self.helper2(n, k, start + 1, combination, result)
        combination.pop()


# Unit Tests
funcs = [Solution().combine, Solution().combine2]


class TestCombine(unittest.TestCase):
    def testCombine1(self):
        for func in funcs:
            self.assertEqual(
                func(n=4, k=2).sort(),
                [
                    [2, 4],
                    [3, 4],
                    [2, 3],
                    [1, 2],
                    [1, 3],
                    [1, 4],
                ].sort(),
            )

    def testCombine2(self):
        for func in funcs:
            self.assertEqual(
                func(n=1, k=1).sort(),
                [[1]].sort(),
            )


if __name__ == "__main__":
    unittest.main()
