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
1. Recursion with backtracking: O(k*n!) time | O(k + k*n!) space
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.helper(n, 1, k, [], result)
        return result

    def helper(self, n, i, k, curr_list, result):
        if len(curr_list) == k:  # backtrack
            result.append(curr_list.copy())
            return
        if i == n + 1:  # can't add n+1 to curr_list
            return
        # exclude i
        self.helper(n, i + 1, k, curr_list, result)

        # include i
        curr_list.append(i)
        self.helper(n, i + 1, k, curr_list, result)
        curr_list.pop()


# Unit Tests
import unittest


class TestCombine(unittest.TestCase):
    def testCombine1(self):
        func = Solution().combine
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
        func = Solution().combine
        self.assertEqual(
            func(n=1, k=1).sort(),
            [[1]].sort(),
        )


if __name__ == "__main__":
    unittest.main()