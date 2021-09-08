"""
216. Combination Sum III
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
- Only numbers 1 through 9 are used.
- Each number is used at most once.

Example1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Example4:
Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.

Example5:
Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.

Constraints:
2 <= k <= 9
1 <= n <= 60
"""

"""
Note:
1. Recursion with backtracking (1): O(k * C(n,k)) time | O(k) space
"""




import unittest
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45 or n < 1:
            return []
        result = []
        self.dfs(k, n, [], result, 1)
        return result
    
    def dfs(self, k: int, n: int, current: List[int], result: List[List[int]], start: int) -> None:
        if n < 0:
            return
        if len(current) == k:
            if n == 0:
                result.append(current[:])   
            return
        if start > 9:
            return
        self.dfs(k, n, current, result, start + 1)
        current.append(start)
        self.dfs(k, n-start, current, result, start + 1)
        current.pop()


# Unit Tests
funcs = [Solution().combinationSum3]


class TestCombinationSum(unittest.TestCase):
    def testCombinationSum1(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(k=3, n=7)),
                sorted([[1,2,4]]),
            )

    def testCombinationSum2(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(k=3, n=9)),
                sorted([[1,2,6],[1,3,5],[2,3,4]]),
            )

    def testCombinationSum3(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(k=4, n=1)),
                sorted([]),
            )

    def testCombinationSum4(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(k=3, n=2)),
                sorted([]),
            )

    def testCombinationSum5(self):
        for func in funcs:
            self.assertEqual(
                sorted(func(k=9, n=45)),
                sorted([[1,2,3,4,5,6,7,8,9]]),
            )


if __name__ == "__main__":
    unittest.main()
