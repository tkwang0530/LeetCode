"""
1937. Maximum Number of Points with Cost
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m-1), picking cells at coordinates (r, c1) and (r+1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

Example1:
Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.


Example2:
Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.

Constraints:
m == points.length
n == points[r].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
0 <= points[r][c] <= 10^5
"""

"""
Note:
1. DP+SuffixMax+PrefixMax: O(m*n) time | O(m*n) space
"""




from typing import List
import unittest
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0] = points[0]

        for i in range(1, rows):
            suffixMax = [0] * cols
            suffixMax[-1] = dp[i-1][-1] - (cols-1)
            for k in range(cols-2, -1, -1):
                suffixMax[k] = max(suffixMax[k+1], dp[i-1][k] - k)

            prefixMax = [0] * cols
            prefixMax[0] = dp[i-1][0] + 0
            for k in range(1, cols):
                prefixMax[k] = max(prefixMax[k-1], dp[i-1][k] + k)

            dp[i][0] = points[i][0] + 0 + suffixMax[0]
            for j in range(1, cols):
                dp[i][j] = max(points[i][j] + j + suffixMax[j],
                               points[i][j] - j + prefixMax[j-1])
        return max(dp[-1])


# Unit Tests
funcs = [Solution().maxPoints]


class TestMaxPoints(unittest.TestCase):
    def testMaxPoints1(self):
        for func in funcs:
            points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
            self.assertEqual(func(points=points), 9)

    def testMaxPoints2(self):
        for func in funcs:
            points = [[1, 5], [2, 3], [4, 2]]
            self.assertEqual(func(points=points), 11)


if __name__ == "__main__":
    unittest.main()
