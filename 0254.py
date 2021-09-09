"""
254. Factor Combinations
Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
   = 2 x 4.

Write a function that takes an integer n and return all possible combinations of its factors.

Note:
1. You may assume that n is always positive.
2. Factors should be greater than 1 and less than n.

Example1:
Input: n = 1
Output: []

Example2:
Input: n = 37
Output: []

Example3:
Input: n = 12
Output: [
    [2, 6],
    [2, 2, 3],
    [3, 4]
]

Example4:
Input: n = 32
Output: [
    [2, 16],
    [2, 2, 8],
    [2, 2, 2, 4],
    [2, 2, 2, 2, 2],
    [2, 4, 4],
    [4, 8]
]
"""

"""
Note:
1. DFS (Backtracking): O(?) time | O(logn) space
"""

from typing import List
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n < 4:
            return []
        result = []
        self.dfs(n, [], result, 2)
        return result

    def dfs(self, n: int, current: List[int], result: List[List[int]], start: int) -> None:
        if n == 1:
            if len(current) > 1:
                result.append(current[:])
            return

        for i in range(start, n+1):
            if i > n / i: break
            if n % i == 0:
                current.append(i)
                self.dfs(n // i, current, result, i)
                current.pop()
        
        # 8 = 2 * 4
        # if start = 2, we will break at 2*sqrt(2)
        # so we need to add back the case with 4
        current.append(n)
        self.dfs(1, current, result, n)
        current.pop()



# Unit Tests
import unittest
funcs = [Solution().getFactors]


class TestGetFactors(unittest.TestCase):
    def testGetFactors1(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(n=1)),
                sorted([]),
            )

    def testGetFactors2(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(n=37)),
                sorted([]),
            )

    def testGetFactors3(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(n=12)),
                sorted([[2, 6],[2, 2, 3],[3, 4]]),
            )

    def testGetFactors4(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(n=32)),
                sorted([[2, 16],[2, 2, 8],[2, 2, 2, 4],[2, 2, 2, 2, 2],[2, 4, 4],[4, 8]])
            )

if __name__ == "__main__":
    unittest.main()
