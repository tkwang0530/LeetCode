"""
1267. Count Servers that Communicate
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""

"""
Note:
1. HashTable: O(mn) time | O(m+n) space - where m is the length of grid and n is the length of grid[i]
"""

from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rowCount = [0] * rows
        colCount = [0] * cols
        total = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    rowCount[row] += 1
                    colCount[col] += 1
                    total += 1
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and rowCount[row] == 1 and colCount[col] == 1:
                    total -= 1
        return total

# Unit Tests
import unittest
funcs = [Solution().countServers]

class TestCountServers(unittest.TestCase):
    def testCountServers1(self):
        for func in funcs:
            grid = [[1,0],[0,1]]
            self.assertEqual(func(grid=grid), 0)

    def testCountServers2(self):
        for func in funcs:
            grid = [[1,0],[1,1]]
            self.assertEqual(func(grid=grid), 3)

    def testCountServers3(self):
        for func in funcs:
            grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
            self.assertEqual(func(grid=grid), 4)

if __name__ == "__main__":
    unittest.main()