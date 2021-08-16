"""
417. Pacific Atlantic Water Flow
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[row][col] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's heigh is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean

Return a 2D list of grid coordinates result where result[i] = [r_i, c_i] denotes that rain water can flow from cell (r_i, c_i) to both the Pacific and Atlantic oceans

Example1:
Input: heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example2:
Input: heights = [
    [2,1],
    [1,2]
]
Output: [[0,0],[0,1],[1,0],[1,1]]

Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5
"""

"""
Note:
1. DFS from the sides: O(nm) time | O(nm) space
the idea is to start from the ocean and find how far it can go, track the previousHeight
if the currentHeight is less than the previousHeight, return
otherwise, add the coordinates Tuple to the specific ocean set
Finally, return the intersection of the two sets in List format
"""

from typing import List, Set, Tuple
import unittest
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        for col in range(cols):
            self.dfs(heights, 0, col, pac, 0)
            self.dfs(heights, rows - 1, col, atl, 0)

        for row in range(rows):
            self.dfs(heights, row, 0, pac, 0)
            self.dfs(heights, row, cols - 1, atl, 0)

        return [[row, col] for row,col in pac.intersection(atl)]
    
    def dfs(self, heights: List[List[int]], row: int, col: int, ocean: Set[Tuple[int]], prevHeight: int) -> None:
        if (row, col) in ocean or row < 0 or col < 0 or row == len(heights) or col == len(heights[0]) or heights[row][col] < prevHeight:
            return
        ocean.add((row, col))
        self.dfs(heights, row - 1, col, ocean, heights[row][col])
        self.dfs(heights, row + 1, col, ocean, heights[row][col])
        self.dfs(heights, row, col - 1, ocean, heights[row][col])
        self.dfs(heights, row, col + 1, ocean, heights[row][col])


# Unit Tests
funcs = [Solution().pacificAtlantic]


class TestPacificAtlantic(unittest.TestCase):
    def testPacificAtlantic1(self):
        for func in funcs:
            heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
            self.assertEqual(sorted(func(heights=heights)), sorted([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]))

    def testPacificAtlantic2(self):
        for func in funcs:
            heights = [[2,1],[1,2]]
            self.assertEqual(sorted(func(heights=heights)), sorted([[0,0],[0,1],[1,0],[1,1]]))


if __name__ == "__main__":
    unittest.main()
