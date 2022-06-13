"""
120. Triangle
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example2:
Input: triangle = [[-10]]
Output: -10

Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4
"""

"""
Note:
1. DP + Greedy: O(n) time | O(1) space - where n is the number of elements in the triangle
"""

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        for row in range(rows-2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])
        return triangle[0][0]

# Unit Tests
import unittest
funcs = [Solution().minimumTotal]

class TestMinimumTotal(unittest.TestCase):
    def testMinimumTotal1(self):
        for func in funcs:
            triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
            self.assertEqual(func(triangle=triangle), 11)

    def testMinimumTotal2(self):
        for func in funcs:
            triangle = [[-10]]
            self.assertEqual(func(triangle=triangle), -10)

if __name__ == "__main__":
    unittest.main()
